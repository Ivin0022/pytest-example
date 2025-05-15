from tracker.models import Budget
``

def test_budget_creation1(db, user):
        pass

def test_budget_creation2(db, user):
    from users.models import User

    assert User.objects.count() == 1


# def test_budget_listing(db, user, bulk_create_budget):
#     bulk_create_budget(3)
#     budget = Budget.objects.all()

#     assert len(budget) == 3
