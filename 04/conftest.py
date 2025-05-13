import pytest
from celery import Celery
from pytest_factoryboy import register
from django.core.management import call_command

# local
from ondc.factories import LoanFactory, ProductFactory, ShopFactory, BorrowerFactory, MerchantFactory
from ondc.fsm import status_changed
from ondc.models.loans import Loan

# Register factories
register(MerchantFactory)
register(ProductFactory)
register(ShopFactory)
register(BorrowerFactory)
register(LoanFactory)



@pytest.fixture
def load_fixtures():
    def _load_fixtures(*fixture_names):
        for fixture in fixture_names:
            call_command('loaddata', fixture, verbosity=0)
    return _load_fixtures


@pytest.fixture
def celery_app():
    app = Celery('test')
    app.conf.update(
        broker_url='memory://',
        result_backend='cache+memory://',
        task_always_eager=True,  # Executes tasks immediately, bypassing the broker.
    )
    return app


@pytest.fixture
def celery_worker(celery_app, celery_worker_pool, celery_includes):
    return celery_app.Worker(pool=celery_worker_pool, includes=celery_includes)