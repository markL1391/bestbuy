class Product:
"""Represents a single product in the store."""

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = self.quantity > 0     # Product is active if there is stock

        # Validate inputs
        if not name:
            raise Exception("Name can not be empty.")
        if price < 0:
            raise Exception("Price cannot be negative.")
        if quantity < 0:
            raise Exception("Quantity cannot be negative.")

    def get_quantity(self):
        # Return current quantity in stock
        return self.quantity

    def set_quantity(self, quantity):
        # Validate quantity
        if quantity < 0:
            raise Exception("Quantity cannot be negative.")

        # Update quantity
        self.quantity = quantity

        # Update active state based on new stock
        self.active = self.quantity > 0

    def is_active(self):
        # Return whether the product is active
        return self.active

    def activate(self):
        # Reactivate the product
        self.active = True

    def deactivate(self):
        # Deactivate the product manually
        self.active = False

    def show(self):
        # Display product information
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity):

        # Quantity must be be positive and available
        if quantity <= 0:
            raise Exception("Quantity must be positive.")
        if quantity > self.quantity:
            raise Exception("Not enough quantity in stock.")

        # Calculate total price for this purchase
        total_price = self.price * quantity

        # Update quantity
        self.quantity -= quantity

        # Update activation based on new stock
        self.active = self.quantity > 0

        return total_price
