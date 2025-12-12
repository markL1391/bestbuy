from products import Product

class Store:
    """Rrepresents all product at the sore"""

    def __init__(self, products):
        # Products is expected to be a list of Product instances.
        self.products = products

    def add_product(self, product):
        # Add a new product to the store
        self.products.append(product)

    def remove_product(self, product):
        # Remove a product from the store
        self.products.remove(product)

    def get_total_quantity(self):
        # Sum the quantities of all products in the store.
        total = 0
        for product in self.products:
            total += product.get_quantity()
        return total

    def get_all_products(self):
        # Return only active products
        active_products = []
        for product in self.products:
            if product.is_active():
                active_products.append(product)
        return active_products

    def order(self, shopping_list):
        """shopping_list is a list of tuples: (product, quantity)"""
        total_price = 0.0
        for product, quantity in shopping_list:
            # Product.buy handles validation and stock updates
            total_price += product.buy(quantity)
        return total_price


def main():
    product_list = [Product("MacBook Air M2", price=1450, quantity=100),
                    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    Product("Google Pixel 7", price=500, quantity=250),
                    ]

    best_buy = Store(product_list)
    products = best_buy.get_all_products()
    print(best_buy.get_total_quantity())
    print(best_buy.order([(products[0], 1), (products[1], 2)]))

if __name__ == "__main__":
    main()
