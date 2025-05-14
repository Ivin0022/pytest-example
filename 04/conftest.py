import pytest

# from pytest_factoryboy import register
from django.core.management import call_command
from users.models import User
from tracker.models import Budget



@pytest.fixture
def load_fixtures():
    def _load_fixtures(*fixture_names):
        for fixture in fixture_names:
            call_command("loaddata", fixture, verbosity=0)

    return _load_fixtures


@pytest.fixture
def user(db):
    return User.objects.create(username="ivin", email="ivin@admin.com")


@pytest.fixture
def bulk_create_budget(db, user):
    def _func(num: int = 1):
        return [
            Budget.objects.create(
                type="needs",
                amount=100,
                user=user,
            )
            for i in range(num)
        ]

    return _func
