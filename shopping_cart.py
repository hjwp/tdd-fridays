from collections import Counter


class ShoppingCart:
    def __init__(self):
        self.products = []
        self.chair_counter = 0
        self.cushion_counter = 0

    def scan(self, product):
        self.products.append(product)

        # if product == 'Chair':
        #     self.chair_counter += 1
        #     if self.chair_counter == 3:
        #         self.total_price += 70
        #     elif self.chair_counter > 3:
        #         self.total_price += 90
        #     else:
        #         self.total_price += 100
        # elif product == 'Cushion':
        #     self.cushion_counter += 1
        #     if self.cushion_counter % 2 == 1:            
        #         self.total_price += 25
        # elif product == 'Sofa':
        #     self.total_price += 500

    def price_after_discounts(self):
        total_price = 0
        c = Counter(self.products)

        if c['Chair'] >= 3:
            total_price += c['Chair'] * 90
        elif c['Chair']:
            total_price += c['Chair'] * 100

        q, r = divmod(c['Cushion'], 2)
        total_price += (q + r) * 25

        total_price += c['Sofa'] * 500

        return total_price

    @property
    def total_price(self):
        return self.price_after_discounts()

