import random
import factory
from factory.django import DjangoModelFactory

from users.models import User
from .models import Budget, Expense

CATEGORY_CHOICES = ["needs", "wants"]


def _get_random_user():
    users = list(User.objects.all()[:100])
    if not users:
        raise ValueError("No users exist in the database.")
    return random.choice(users)


class BudgetFactory(DjangoModelFactory):
    class Meta:
        model = Budget

    type = factory.LazyFunction(lambda: random.choice(CATEGORY_CHOICES))
    amount = factory.LazyFunction(lambda: random.randint(100, 1000))
    user = factory.LazyFunction(_get_random_user)


class ExpenseFactory(DjangoModelFactory):
    class Meta:
        model = Expense

    type = factory.LazyFunction(lambda: random.choice(CATEGORY_CHOICES))
    amount = factory.LazyFunction(lambda: random.randint(10, 500))
    description = factory.Faker("sentence")
    user = factory.LazyFunction(_get_random_user)
