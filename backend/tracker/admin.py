from django.contrib import admin
from django.contrib import messages

from django.http import HttpRequest
from django.shortcuts import redirect
from django.urls import reverse_lazy
from unfold.admin import ModelAdmin
from unfold.decorators import action

from .factories import BudgetFactory, ExpenseFactory
from .models import Budget, Expense


@admin.action(description="Generate 10 sample Budget")
def generate_budget(modeladmin, request, queryset):
    for _ in range(10):
        BudgetFactory()
    messages.success(request, "10 sample Budget generated successfully.")


@admin.register(Budget)
class BudgetAdmin(ModelAdmin):
    """Admin View for Budget"""

    actions_list = ["changelist_action"]

    @action(
        description="bulk create",
        icon="person",
        # permissions=["changelist_action"],
    )
    def changelist_action(self, request: HttpRequest):
        for _ in range(10):
            BudgetFactory()
        return redirect(reverse_lazy("admin:tracker_budget_changelist"))



@admin.register(Expense)
class ExpenseAdmin(ModelAdmin):
    """Admin View for Expense"""
