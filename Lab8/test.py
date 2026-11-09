from Order import Order
from supplier import Supplier
from product import Product
from physical_products import PhysicalProducts
from digital_products import DigitalProducts
from inventory import Inventory

# Task 2.2 association
def test_association()-> None:
    supplier = Supplier("S1001", "ABC Supplier", "abcsupplier@example.com") 
    physical = PhysicalProducts("P1001","Phone", 1200.0, 12, 1.00, supplier) 
    digital = DigitalProducts("D1001", "Anti-virus software", 150,15,400, supplier)
    del supplier
    physical.display_supplier_information()
    digital.display_supplier_information()
    print("Association TEST PASS: Product display individual supplier information independently\n")

# Task 3.2 aggregation
def test_aggregation()-> None:
    supplier = Supplier("S1001", "ABC Supplier", "abcsupplier@example.com") 
    product1 = PhysicalProducts("P1002", "Laptop", 1500.00, 12, 1.5, supplier)
    inventory_a = Inventory()
    inventory_b = Inventory()
    inventory_a.add_product(product1)
    assert inventory_a.find_product("P1002") is product1
    inventory_a.remove_product(product1)
    assert inventory_a.find_product("P1002") is product1
    product1.display_information()
    inventory_b.add_product(product1)
    assert inventory_b.find_product("P1002") is product1
    print("Aggregation TEST PASS: the product object still works when it is removed from inventory or transferred to inventory b\n")

# Task 4.3 Test Composition:
def test_composition() -> None:
    # create an order
    supplier = Supplier("S1001", "ABC Supplier", "abcsupplier@example.com") 
    physical = PhysicalProducts("P1001","Phone", 1200.0, 12, 1.00, supplier) 
    digital = DigitalProducts("D1001", "Anti-virus software", 150,15,400, supplier)
    new_order1 = Order("O1001")
    new_order2 = Order("O1002")
    # add two product to the order line
    new_order1.add_order_line(physical,2)
    new_order2.add_order_line(digital,3)
    assert new_order1.calculate_total() == 2400.00
    assert new_order2.calculate_total() == 450.00
    # Display each order line and calculate order total 
    print("Order 1:", new_order1.calculate_total())
    print("Order 2:", new_order2.calculate_total())
    # Add the second product to demonstrate multi order line total
    new_order1.add_order_line(digital,1)
    assert new_order1.calculate_total() == 2550.00
    # remove an order
    del new_order1
    assert physical.get_product_name() == "Phone"
    assert digital.get_product_name() == "Anti-virus software"
    print("Composition TEST PASS: Orders create their own lines, calculate independent totals and do not own the products\n")

# Task 6.2 Test Substitutability
def show_product_details(product:Product)-> None:
    product.display_information()
    print(product.get_fulfilment_info())

# Task 6.3 Test LSP 
def test_lsp_polymorphism()-> None:
    supplier = Supplier("S1001", "ABC Supplier", "abcsupplier@example.com") 
    physical = PhysicalProducts("P1001","Phone", 1200.0, 12, 1.00, supplier) 
    digital = DigitalProducts("D1001", "Anti-virus software", 150,15,400, supplier)
    inventory = Inventory() 
    inventory.add_product(physical)
    inventory.add_product(digital)
    # Task 7.2 Test Polymorphism 
    inventory.display_all_products()
    for product in inventory.get_products():
        show_product_details(product)
        product.update_stock(12)
        assert product.get_product_stock() == 12
        assert product.to_dict()["Stock"] == 12
    assert physical.get_fulfilment_info() == "Product requires physical shipping!"
    assert digital.get_fulfilment_info() == "Product delivered digitally"
    print("PASS, both subclasses work through the Product contract and has the expected behaviour\n")


if __name__ == "__main__":
    test_association()
    test_aggregation()
    test_composition()
    test_lsp_polymorphism()
    print("\nTest PASSED for all tasks!")
  