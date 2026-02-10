from products import Product

class Store:
    """
    Represents a store that contains all products.
    """

    def __init__(self, products: list[Product]):
        """
        Create a store with a list of Product instances.
        Args:
            products (list[Product]): Initial products.
        Raises:
            TypeError: If products is not a list or contains non-Product items.
        """
        if not isinstance(products, list):
            raise TypeError("Products must be a list of Product instances.")
        if not all(isinstance(p, Product) for p in products):
            raise TypeError("Products must contain only Product instances.")

        self.products = products

    def add_product(self, product: Product) -> None:
        """
        Add a new product to the store.
        """
        if not isinstance(product, Product):
            raise TypeError("Product must be a Product instance.")
        self.products.append(product)

    def remove_product(self, product: Product) -> None:
        """
        Remove a product from the store.
        """
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """
        Returns the total quantity of all products (active or not).
        For using only active products, filter by product.is_active().
        """
        return sum(product.get_quantity() for product in self.products)

    def get_all_products(self) -> list[Product]:
        """
        Return a list of active products only.
        """
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        """
        Process an order.
        Args:
            shopping_list is a list of tuples: (product, quantity)
        Returns:
            float: Total order price.
        """
        total_price = 0.0
        for product, quantity in shopping_list:

            # Product.buy handles validation and stock updates
            total_price += product.buy(quantity)
        return total_price