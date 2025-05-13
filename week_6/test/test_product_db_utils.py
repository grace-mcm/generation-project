import pytest
from unittest.mock import MagicMock, patch

@pytest.fixture
def mock_db():
    mock_connection = MagicMock()
    mock_cursor = MagicMock()
    mock_connection.cursor.return_value = mock_cursor
    return mock_connection, mock_cursor

@pytest.fixture(autouse=True)
def patch_db(mock_db, monkeypatch):
    mock_connection, mock_cursor = mock_db
    monkeypatch.setattr("psycopg2.connect", MagicMock(return_value=mock_connection))
    monkeypatch.setattr("src.product_db_utils.cursor", mock_cursor)
    monkeypatch.setattr("src.product_db_utils.cursor", mock_connection)
    

def test_get_product(mock_db, capsys):
    _, mock_cursor = mock_db
    mock_cursor.fetchall.return_value = [(1, "test product 1", 9.99), (2, "test product 2", 9.99)]
    print(mock_cursor.fetchall())
    from src.product_db_utils import get_product
    get_product(1)
    captured = capsys.readouterr()
    assert "(1, 'test product 1', 9.99)" in captured.out

def test_add_new_product(mock_db):
    mock_cursor, mock_connection = mock_db
    
    from src.product_db_utils import add_new_product
    with patch("src.product_db_utils.cursor", mock_cursor), patch("src.product_db_utils.connection", mock_connection):
        add_new_product("test product", 9.99)

        print("execute was called:", mock_cursor.execute.call_count)
        print("commit was called:", mock_connection.commit.call_count)

        expected_sql = """INSERT INTO products(product_name, price) VALUES(%s, %s) RETURNING product_id, product_name, price"""
        expected_params = ("test product", 9.99)

        actual_sql, actual_params = mock_cursor.execute.call_args[0]
        assert expected_params == actual_params, "SQL parameters mismatched"
        mock_cursor.execute.assert_any_call(expected_sql.strip(), expected_params)

        mock_connection.commit.assert_called_once()

def test_add_new_product_fail(mock_db, capsys):
    mock_cursor, mock_connection = mock_db
    mock_cursor.execute.side_effect = Exception("database error")

    from src.product_db_utils import add_new_product
    with patch("src.product_db_utils.cursor", mock_cursor), patch("src.product_db_utils.connection", mock_connection):
        add_new_product("test product", 9.99)
    
        captured = capsys.readouterr()
        assert "Unable to add product!" in captured.out

        mock_connection.commit.assert_not_called()


        