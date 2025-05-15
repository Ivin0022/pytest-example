import factory
from factory.django import DjangoModelFactory

from .models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f"user{n}")
    email = factory.LazyAttribute(lambda o: f"{o.username}@example.com")
    # password = factory.PostGenerationMethodCall("set_password", "password")
    is_active = True
