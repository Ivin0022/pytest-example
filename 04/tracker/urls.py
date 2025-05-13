from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tracker.views import BudgetViewset, ExpenseViewset



route = DefaultRouter()
route.register('budgets',BudgetViewset)
route.register('expenses', ExpenseViewset)

urlpatterns = [
    path('', include(route.urls))
]