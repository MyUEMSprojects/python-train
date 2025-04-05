# 1. Fixtures (pytest)

import pytest


@pytest.fixture
def database_connection():
    conn = create_db_connection()
    yield conn  # Setup e teardown em um só
    conn.close()


def test_query(database_connection):
    result = database_connection.execute("SELECT 1")
    assert result == 1


# TODO
