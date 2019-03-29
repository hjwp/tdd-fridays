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

    def price_after_discounts(self):
        total_price = 0
        c = Counter(self.products)

        total_price += self._bulk_discounts(c)

        q, r = divmod(c['Cushion'], 2)
        total_price += (q + r) * 25

        total_price += c['Sofa'] * 500

        return total_price
    

    def _bulk_discounts(self, c):
        bulk_discount = 0

        if c['Chair'] >= 3:
            bulk_discount = c['Chair'] * 90
        elif c['Chair']:
            bulk_discount = c['Chair'] * 100
        
        return bulk_discount

    @property
    def total_price(self):
        return self.price_after_discounts()

