import pytest

from shopping_cart import ShoppingCart


@pytest.mark.parametrize("product,expected_price", [
    ('Chair', 100),
    ('Sofa', 500),
    ('Cushion', 25),
    ('Bed', 0),
])
def test_calculate_total_price_for_single_product_in_cart(product, expected_price):
    cart = ShoppingCart()
    cart.scan(product)
    assert cart.total_price() == expected_price


def test_add_multiple_products_to_cart():
    cart = ShoppingCart()

    product1 = 'Chair'
    product2 = 'Sofa'
    product3 = 'Cushion'

    cart.scan(product1)
    cart.scan(product2)
    cart.scan(product3)

    assert cart.total_price() == 625


def test_no_bulk_discount():
    cart = ShoppingCart()

    product = 'Chair'
    cart.scan(product)
    cart.scan(product)

    assert cart.total_price() == 200


def test_bulk_discount():
    cart = ShoppingCart()

    product = 'Chair'
    cart.scan(product)
    cart.scan(product)
    cart.scan(product)
    cart.scan(product)

    assert cart.total_price() == 90 + 90 + 90 + 90


def test_buy_1_get_1_free_cushion():
    cart = ShoppingCart()

    product = 'Cushion'

    cart.scan(product)
    cart.scan(product)

    assert cart.total_price() == 25

