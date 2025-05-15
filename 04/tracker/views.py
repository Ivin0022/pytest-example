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
from django.db.models import Sum
# Create your views here.


class BudgetViewset(viewsets.ModelViewSet):
    queryset = Budget.objects.all()
    serializer_class = BudgetSerializer
    pagination_class = CursorPagination

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    @action(methods=["get"], detail=False)
    def total(self, request):
        a = Budget.objects.aggregate(total=Sum("amount"))
        return Response(a)


class ExpenseViewset(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        "created": ["gte", "lte"],
    }
    ordering_fields = ["amount", "created"]
    ordering = ["-amount"]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
