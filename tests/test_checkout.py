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

def test_checkout_flow(driver, logger):
    logger.info("Starting test_checkout_flow")

    # 1. Login
    login_page = LoginPage(driver)
    logger.info("Clicking on standard user")
    login_page.click_standard_user()
    logger.info("Tapping on Login button")
    login_page.tap_login_button()

    # 2. Add product to cart
    products_page = ProductsPage(driver)
    logger.info("Adding 'Sauce Labs Backpack' to cart")
    products_page.add_product_to_cart("Sauce Labs Backpack")

    # 3. Check the cart
    cart_page = CartPage(driver)
    logger.info("Opening the cart")
    cart_page.tap_cart_icon()
    product_name = "Sauce Labs Backpack"
    product_element = cart_page.get_product_item(product_name)
    logger.info(f"Verifying product '{product_name}' is present in the cart")
    assert product_element is not None, f"Product '{product_name}' was not found in the cart"
    assert product_name in product_element.text, f"Expected '{product_name}' but found '{product_element.text}'"
    cart_page.checkout()

    # 4. Going through checkout
    checkout_page = CheckoutPage(driver)
    logger.info("Filling personal data")
    checkout_page.fill_personal_data("Jan", "Kowalski", "00-001")
    logger.info("Tapping on continue")
    checkout_page.tap_continue()
    logger.info("Swiping up on checkout page")
    checkout_page.swipe_up()
    logger.info("Finalizing checkout")
    checkout_page.finish_checkout()

    # 5. Last assertion
    final_text = checkout_page.get_thank_you_message()
    logger.info("Verifying final confirmation text")
    assert "THANK YOU FOR YOU ORDER" in final_text.upper(), "Cannot find the final confirmation text"
