from collections import defaultdict
from datetime import datetime
from django.db.models.functions import ExtractMonth, ExtractYear, ExtractDay
from django.shortcuts import render
from rest_framework import viewsets

from tracker.serializers import BudgetSerializer, ExpenseSerializer
from .models import Budget, Expense
from rest_framework.pagination import CursorPagination
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

# Create your views here.


class BudgetViewset(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    pagination_class = CursorPagination

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'])
    def monthly(self, request):
        """Return user's current month budget split into 'needs' and 'wants'."""
        month = request.query_params.get('month')
        year = request.query_params.get('year')
        user = request.user
        now = datetime.now()
        month = int(month) if month else now.month
        year = int(year) if year else now.year

        expenses = Expense.objects.annotate(
            month=ExtractMonth('created'),
            year=ExtractYear('created')
        ).filter(user=user, month=month, year=year)

        expense_summary = defaultdict(lambda: 0)
        for e in expenses:
            if e.type in ['needs', 'wants']:
                expense_summary[e.type] += e.amount

        budgets = Budget.objects.annotate(
            month=ExtractMonth('created'),
            year=ExtractYear('created')
        ).filter(user=user, month=month, year=year)

        data = {
            k: {
                'total': None,
                'balance': None
            } for k in ['needs', 'wants']
        }

        for b in budgets:
            if b.type in ['needs', 'wants']:
                total = data[b.type]['total'] = (data[b.type]['total'] or 0) + b.amount
                data[b.type]['balance'] = total - expense_summary[b.type]

        return Response({
            'next': None,
            'previous': None,
            'results': [data]
        })

class ExpenseViewset(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'created': ['gte', 'lte'],
    }
    ordering_fields = ['amount', 'created']
    ordering = ['-amount']

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    