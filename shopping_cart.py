from collections import Counter

class BulkDiscount:

    def __init__(self, products):
        self.products = products
    
    def discounted_price(self):
        pass


class ShoppingCart:
    def __init__(self):
        self.products = []

    def scan(self, product):
        self.products.append(product)

    def total_price(self):
        total_price = 0
        c = Counter(self.products)

        total_price += self._bulk_discounts(c, 'Chair')
        total_price += self._buy_one_get_one_free(c, 'Cushion')
        total_price += c['Sofa'] * 500

        return total_price
    
    def _bulk_discounts(self, c, item):
        bulk_discount = 0

        if c[item] >= 3:
            bulk_discount = c[item] * 90
        elif c[item]:
            bulk_discount = c[item] * 100
        
        return bulk_discount

    def _buy_one_get_one_free(self, c, item):
        q, r = divmod(c[item], 2)
        return (q + r) * 25


