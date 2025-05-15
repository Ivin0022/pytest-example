import pytest

from pytest_factoryboy import register
from django.core.management import call_command
from users.factories import UserFactory

register(UserFactory)

@pytest.fixture
def load_fixtures():
    def _load_fixtures(*fixture_names):
        for fixture in fixture_names:
            call_command("loaddata", fixture, verbosity=0)

    return _load_fixtures

