import queue
import unittest
from decimal import Decimal
from unittest.mock import MagicMock, patch

import psycopg2

from app.forms import GROUPS, LABELS, fields, validate
from app.gui import DataEntryApp
from repositories.product_repo import ProductRepository


class FormTests(unittest.TestCase):
    def test_all_fields_have_labels(self):
        for repository, methods in GROUPS.values():
            for method in methods.values():
                for field in fields(repository, method):
                    self.assertIn(field.name, LABELS)

    def test_decimal_precision(self):
        parameters = fields(ProductRepository, "insert_productvarints")
        raw = dict(variant_id="1", product_id="2", sku="ABC", name="Variante",
                   price="12,35", cost_price="10.01", weight_kg="0.25")
        self.assertEqual(validate(parameters, raw)["price"], Decimal("12.35"))
        for bad in ("NaN", "Infinity", "-1", "abc"):
            with self.assertRaises(ValueError):
                validate(parameters, dict(raw, price=bad))

    def test_optional_parent_and_required_name(self):
        parameters = fields(ProductRepository, "insert_category")
        raw = dict(category_id="1", name="Hogar", slug="hogar", parent_category_id="", description="")
        self.assertIsNone(validate(parameters, raw)["parent_category_id"])
        for changes in ({"name": " "}, {"category_id": "0"}):
            with self.assertRaises(ValueError):
                validate(parameters, dict(raw, **changes))

    @patch("app.gui.get_connection")
    def test_save_uses_repository_and_closes_connection(self, connect):
        app = MagicMock()
        app.results = queue.Queue()
        repository = MagicMock()
        DataEntryApp.insert(app, repository, "insert_product", {"name": "Mesa"})
        repository.return_value.insert_product.assert_called_once_with(name="Mesa")
        connect.return_value.close.assert_called_once()
        self.assertTrue(app.results.get_nowait()[0])

    @patch("app.gui.get_connection")
    def test_database_failure_rolls_back(self, connect):
        app = MagicMock()
        app.results = queue.Queue()
        repository = MagicMock()
        repository.return_value.insert_product.side_effect = psycopg2.IntegrityError()
        DataEntryApp.insert(app, repository, "insert_product", {})
        connect.return_value.rollback.assert_called_once()
        connect.return_value.close.assert_called_once()
        self.assertFalse(app.results.get_nowait()[0])


if __name__ == "__main__":
    unittest.main()
