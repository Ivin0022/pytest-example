from tracker.models import Budget


def test_budget_creation(db, user, bulk_create_budget):
    bulk_create_budget(1)
    budget = Budget.objects.all()

    assert len(budget) == 1


def test_budget_listing(db, user, bulk_create_budget):
    bulk_create_budget(3)
    budget = Budget.objects.all()

    assert len(budget) == 3
