from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.utils import timezone
from core.models import BaseModel
from users.models import User

CATEGORY_CHOICES = [("needs", "Needs"), ("wants", "Wants")]


class Budget(BaseModel):
    """
    Maximum available money for a user spending per month
    """

    type = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="budget")


class Expense(BaseModel):
    """Daily expense"""

    type = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    amount = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="expenses")


@receiver(post_save, sender=Expense)
def post_save_single_expense(sender, instance, created, **kwargs):
    if created:
        print(f"A new SingleExpense was created by user: {instance.user}")
