import pytest
from helpers.driver_manager import DriverManager
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage

@pytest.fixture(scope="function")
def driver():
    driver_instance = DriverManager.start_driver()
    yield driver_instance
    DriverManager.quit_driver()

def test_empty_required_fields_error(driver):
    # 1. Login and add a product to the cart
    login_page = LoginPage(driver)
    login_page.click_standard_user()
    login_page.tap_login_button()

    products_page = ProductsPage(driver)
    products_page.add_product_to_cart("Sauce Labs Backpack")

    cart_page = CartPage(driver)
    cart_page.tap_cart_icon()
    cart_page.checkout()

    # 2. Attempt checkout without filling fields
    checkout_page = CheckoutPage(driver)
    checkout_page.tap_continue()

    # 3. Verify error message
    error_message = checkout_page.get_error_message()
    assert "First Name is required" in error_message, f"Expected 'First Name is required' but got '{error_message}'"
