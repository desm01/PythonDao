import pytest

from app import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_student_by_id(client):
    rv = client.get("/students/id/1")
    assert b"[(1, 'Desmond', 'Madden', datetime.datetime(2001, 2, 26, 0, 0), 1, 'male', 1, 'Electronics School', '123 Education Street')]" == rv.data

def test_get_author_by_id(client):
    rv = client.get("/author/id/1")
    assert b"[(1, 'Edwina', 'Writer')]" == rv.data

def test_get_book_by_name(client):
    rv = client.get("/book/name/donut%20dreamin")
    assert b"[(4, 'Donut Dreamin', 83754, 4, 4, 4, 'Homer', 'Simpson', 4, 'Art')]" == rv.data

def test_get_all_where_loan_id(client):
    rv = client.get("/loans/id/1")
    assert b"[(1, 1, 1, datetime.datetime(2021, 6, 1, 0, 0), datetime.datetime(2021, 8, 1, 0, 0), 1, 'Desmond', 'Madden', datetime.datetime(2001, 2, 26, 0, 0), 1, 'male', 1, 'The Big Space Race', 435, 1, 1)]" == rv.data

def test_get_all_loans_not_returned(client):
    rv = client.get("/loans")
    assert b"[(4, 2, 2, datetime.datetime(2021, 10, 1, 0, 0), None, 2, 'Bart', 'Simpson', datetime.datetime(1990, 1, 1, 0, 0), 4, 'male', 2, 'Rolling Flame', 857, 2, 2)]" == rv.data