from tracker.models import Budget
from tracker.factories import BudgetFactory


def test_budget_creation(db, client):
    res = client.post(
        "/api/budgets/",
        {
            "type": "needs",
            "amount": 1000,
        },
    )

    assert res.status_code == 201
    assert "id" in res.data
    assert "type" in res.data
    assert Budget.objects.count() == 1


def test_budget_listing(db, client):
    num = 1000
    BudgetFactory.create_batch(num)

    res = client.get("/api/budgets/")
    data = res.data
    assert len(data['results']) == 100
    assert data['next'] is not None
