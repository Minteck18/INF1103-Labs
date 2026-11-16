import inspect
import unittest
from supplier import Supplier
from digital_products import DigitalProducts
from physical_products import PhysicalProducts
from Order import Order
from contextlib import redirect_stdout
from io import StringIO
from unittest.mock import patch
from validators import parse_price, parse_stock, get_valid_input
from bulk_discount import BulkDiscount
from percentage_discount import PercentageDiscount
from discount_strategy import DiscountStrategy
from product_factory import ProductFactory
import tempfile
from pathlib import Path

from supplier import Supplier
from inventory import Inventory
from file_handler import load_products

# TEST THIS WITH python -m unittest discover -s tests -v   

HEADER = "product_type,product_id,name,price,stock_quantity,weight,download_size\n"

PROJECT_ROOT = Path(__file__).resolve().parents[1]   


class DiscountStrategyTests(unittest.TestCase):
    def setUp(self):
        supplier = Supplier(1, "ABC", "abc@acme.com")
        item = DigitalProducts("D1001", "Anti-virus software", 150,15,400, supplier)
        self.order = Order(1)
        self.order.add_order_line(item, 2)   

    def test_no_discount(self):
        self.assertEqual(self.order.calculate_total(), 300)

    def test_bulk_discount(self):
        self.order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(self.order.calculate_total(), 280)

    def test_percentage_discount(self):
        self.order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(self.order.calculate_total(), 270)

    def test_no_if_logic_in_calculate_total(self):
        source = inspect.getsource(Order.calculate_total)
        self.assertNotIn("if ", source)
        self.assertNotIn("isinstance", source)

    def test_new_strategy_without_changing_order(self):
        class StudentDiscount(DiscountStrategy):
            def apply(self, total: float) -> float:
                return total * 0.95

        self.order.set_discount(StudentDiscount())
        self.assertAlmostEqual(self.order.calculate_total(), 285)

    def test_set_discount_changes_strategy(self):
        self.order.set_discount(BulkDiscount(200, 20))
        self.assertEqual(self.order.calculate_total(), 280)

        self.order.set_discount(PercentageDiscount(10))
        self.assertAlmostEqual(self.order.calculate_total(), 270)

class ProductFactoryTests(unittest.TestCase):
    def setUp(self):
        self.supplier = Supplier(1, "ABC", "abc@example.com")

    def test_factory_creates_physical(self):
        product = ProductFactory.create(
            "physical", "P001", "Laptop", 1550.0, 10, self.supplier, weight=1.2
        )
        self.assertIsInstance(product, PhysicalProducts)

    def test_factory_creates_digital(self):
        product = ProductFactory.create(
            "digital", "D001", "Editor", 49.9, 5, self.supplier, download_size=250
        )
        self.assertIsInstance(product, DigitalProducts)

    def test_unknown_type_raises_value_error(self):
        with self.assertRaisesRegex(ValueError, "Unknown product type: service"):
            ProductFactory.create("service", "S001", "Install", 30.0, 1, self.supplier)

class ValidatorTests(unittest.TestCase):
    def setUp(self):
        supplier = Supplier(1, "ABC", "abc@acme.com")
        self.item = DigitalProducts("D1001", "Anti-virus software", 150,15,400, supplier)

    def test_invalid_price_rejected(self):
        for price in ("abc", "-5", "0", ""):
            with self.subTest(price=price):
                with self.assertRaises(ValueError):
                    parse_price(price)

    def test_valid_price_accepted(self):
            self.assertEqual(parse_price("12.50"), 12.5)

    def test_invalid_stock_rejected(self):
        for stock in ("abc", "-1", "2.5", ""):
            with self.subTest(stock=stock):
                with self.assertRaises(ValueError):
                    parse_stock(stock)

    def test_valid_stock_accepted(self):
        for text, expected in (("1", 1), ("2", 2), ("5", 5), ("10", 10), ("0", 0)):
            with self.subTest(stock=text):
                self.assertEqual(parse_stock(text), expected)

    def test_invalid_order_quantity_rejected(self):
        for quantity in (0, -1):
            with self.subTest(quantity=quantity):
                order = Order(1)
            with self.assertRaises(ValueError):
                order.add_order_line(self.item, quantity)

    def test_ask_reprompts_until_valid(self):
        answers = iter(["abc", "-5", "12.50"])
        output = StringIO()
        with patch("builtins.input", lambda prompt="": next(answers)):
            with redirect_stdout(output):
                result = get_valid_input("Enter price: ", parse_price)

        self.assertEqual(result, 12.5)
        out = output.getvalue()
        self.assertIn("Price must be a number", out)
        self.assertIn("Price must not be less than 0", out)

class CsvLoaderTests(unittest.TestCase):
        def setUp(self):
            self.supplier = Supplier(1, "ABC", "abc@acme.com")
            self.inventory = Inventory()
            self._tmp = tempfile.TemporaryDirectory()
            self.addCleanup(self._tmp.cleanup)
            self.tmp_path = Path(self._tmp.name)

        def test_missing_file_handled(self):
            output = StringIO()
            with redirect_stdout(output):
                load_products(str(self.tmp_path / "missing.csv"), self.inventory, self.supplier)   

            out = output.getvalue()
            self.assertIn("Product does not exists on", out)
            self.assertIn("Load attempt finished.", out)

        def test_bad_rows_skipped_valid_rows_load(self):
            csv_file = self.tmp_path / "products.csv"
            csv_file.write_text(
                HEADER
                + "physical,1,Desk Lamp,25.00,10,1.2,0\n"
                + "digital,2,Photo Editor,49.90,100,0,250\n"
                + "service,3,Installation,30.00,5,0,0\n"
                + "physical,4,Office Chair,abc,3,8.5,0\n"
                + "physical,5,Monitor Stand,39.50,7,2.0,0\n"
            )

            output = StringIO()
            with redirect_stdout(output):
                load_products(str(csv_file), self.inventory, self.supplier)

            self.assertTrue(self.inventory.find_product("1"))
            self.assertTrue(self.inventory.find_product("2"))
            self.assertTrue(self.inventory.find_product("5"))
            self.assertFalse(self.inventory.find_product("3"))   # unknown type
            self.assertFalse(self.inventory.find_product("4"))   # bad price

            out = output.getvalue()
            self.assertIn("Unknown product type: service", out)
            self.assertIn("could not convert string to float", out)
            self.assertIn("3 products loaded.", out)
            self.assertIn("Load attempt finished.", out)

        def test_every_except_is_specific(self):
            for filename in ("file_handler.py", "validators.py", "main.py"):
                with self.subTest(filename=filename):
                    source = (PROJECT_ROOT / filename).read_text()
                    self.assertNotIn("except:", source)
                    self.assertNotIn("except Exception", source)
                    self.assertNotIn("except BaseException", source)

if __name__ == "__main__":
    unittest.main()