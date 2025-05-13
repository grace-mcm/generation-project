import pytest
from unittest.mock import patch, MagicMock
from src.main_menu import main_menu

@pytest.fixture
def mock_db():
    with patch("src.main_menu.connection") as mock_connection,\
    patch("src.main_menu.cursor") as mock_cursor:
        mock_connection.commit = MagicMock()
        mock_connection.close = MagicMock()
        mock_cursor.close = MagicMock()
        mock_connection = MagicMock()
        mock_cursor = MagicMock()
        mock_connection.cursor.return_value = mock_cursor
        yield mock_connection, mock_cursor

@pytest.fixture(autouse=True)
def patch_db(mock_db, monkeypatch):
    mock_connection, mock_cursor = mock_db
    monkeypatch.setattr("psycopg2.connect", MagicMock(return_value=mock_connection))
    monkeypatch.setattr("src.main_menu.cursor", mock_cursor)
    monkeypatch.setattr("src.main_menu.cursor", mock_connection)

def mock_menus():
    with patch("src.main_menu.products_menu") as mock_products_menu, \
        patch("src.main_menu.order_menu") as mock_order_menu, \
        patch("src.main_menu.courier_menu") as mock_courier_menu:
        yield mock_products_menu, mock_order_menu, mock_courier_menu

def test_main_menu_products(mock_menus, monkeypatch, capsys):
    mock_products_menu, _, _ = mock_menus
    monkeypatch.setattr("builtins.input", lambda _: "1")
    with pytest.raises(SystemExit):
        main_menu()
    
    captured = capsys.readouterr()
    assert "[1] - Products Menu" in captured.out
    mock_products_menu.assert_called_once()

def test_main_menu_orders(mock_menus, monkeypatch, capsys):
    _, mock_order_menu, _ = mock_menus
    monkeypatch.setattr("builtins.input", lambda _: "2")
    with pytest.raises(SystemExit):
        main_menu()
    captured = capsys.readouterr()
    assert "[2] - Orders Menu" in captured.out 
    mock_order_menu.assert_called_once()

def test_main_menu_couriers(mock_menus, monkeypatch, capsys):
    _, _, mock_courier_menu = mock_menus
    monkeypatch.setattr("builtins.input", lambda _: "3")
    with pytest.raises(SystemExit):
        main_menu()
    captured = capsys.readouterr()
    assert "[3] - Couriers Menu" in captured.out 
    mock_courier_menu.assert_called_once()

def test_main_menu_exit(mock_db, monkeypatch, capsys):
    mock_connection, mock_cursor = mock_db
    monkeypatch.setattr("builtins.input", lambda _: "0")
    with pytest.raises(SystemExit):
        main_menu()
    captured = capsys.readouterr()
    assert "[0] - Exit App" in captured.out 
    mock_connection.commit.assert_called_once()
    mock_cursor.close.assert_called_once()
    mock_connection.close.assert_called_once()
