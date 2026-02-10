class Product:
    """
    Represents a single product in the store.
    """
    def __init__(self, name: str, price: float, quantity: int):
        """
        Create a product with validations.

        Args:
            name (str): Product name (non-empty).
            price (float): Product price (>= 0).
            quantity (int): Initial stock quantity (>=0).

        Raises:
             ValueError: If any input is invalid.
        """
        # Validate inputs first.
        if not name or not str(name).strip():
            raise ValueError("Name can not be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = self.quantity > 0         # Product is active if there is stock.

    def get_quantity(self) -> int:
        """
        Return current quantity in stock
        """
        return self.quantity

    def set_quantity(self, quantity: int) -> None:
        """
        Set the product quantity and update active state.

        Raises:
            ValueError: if quantity is negative.
        """
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.quantity = quantity                    # Update quantity
        self.active = self.quantity > 0             # Update active state based on new stock

    def is_active(self) -> bool:
        """
        Return whether the product is active.
        """
        return self.active

    def activate(self) -> None:
        """
        Activate the product
        """
        self.active = True

    def deactivate(self) -> None:
        """
        Deactivate the product manually.
        """
        self.active = False

    def show(self) -> str:
        """
        Return a readable product string for printing.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, desired_quantity: int) -> float:
        """
        Buy a given quantity and return the total price.

        Args:
            desired_quantity (int): Quantity to buy.

        Returns:
            float: Total price for this purchase.

        Raises:
            ValueError: if quantity is invalid or not enough stock.
        """
        if desired_quantity <= 0:                                # Quantity must be be positive and available.
            raise ValueError("Quantity must be positive.")
        if desired_quantity > self.get_quantity():
            raise ValueError("Not enough quantity in stock.")

        total_price = self.price * desired_quantity             # Calculate total price for this purchase.
        new_quantity = self.get_quantity() - desired_quantity   # Update quantity.
        self.set_quantity(new_quantity)                         # Update activation based on new stock.
        return total_price
