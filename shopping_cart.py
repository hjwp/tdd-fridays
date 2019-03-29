class ShoppingCart:
    def __init__(self):
        self.products = []
        self.total_price = 0
        self.chair_counter = 0
        self.cushion_counter = 0

    def scan(self, product):
        self.products.append(product)
        if product == 'Chair':
            self.chair_counter += 1
            if self.chair_counter == 3:
                self.total_price += 70
            elif self.chair_counter > 3:
                self.total_price += 90
            else:
                self.total_price += 100
        elif product == 'Cushion':
            self.cushion_counter += 1
            if self.cushion_counter % 2 == 1:            
                self.total_price += 25
        elif product == 'Sofa':
            self.total_price += 500
