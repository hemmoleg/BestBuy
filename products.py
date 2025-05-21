class Product:
    """
    Represents a product with a name, price, quantity, and active status.
    """

    def __init__(self, name, price, quantity):
        """
        Initialize a Product instance.

        Args:
            name (str): The name of the product.
            price (float): The price per unit of the product.
            quantity (int): The initial quantity in stock.

        Raises:
            ValueError: If name is empty, or if price or quantity is negative.
        """
        self.active = True

        if not name:
            raise ValueError("name must not be empty")
        if price < 0:
            raise ValueError("price must not be negative")
        if quantity < 0:
            raise ValueError("quantity must not be negative")

        self.name = name
        self.price = price
        self.quantity = quantity

    def get_quantity(self):
        """
        Returns the current quantity in stock.

        Returns:
            int: The quantity of the product.
        """
        return self.quantity

    def set_quantity(self, quantity):
        """
        Sets a new quantity for the product.

        Args:
            quantity (int): The new quantity to set.

        Raises:
            ValueError: If quantity is negative.
        """
        if quantity < 0:
            raise ValueError("quantity must not be negative")
        self.quantity = quantity

        if self.quantity <= 0:
            self.deactivate()

    def is_active(self):
        """
        Checks if the product is currently active.

        Returns:
            bool: True if active, False otherwise.
        """
        return self.active

    def activate(self):
        """
        Marks the product as active.
        """
        self.active = True

    def deactivate(self):
        """
        Marks the product as inactive.
        """
        self.active = False

    def show(self):
        """
        Returns a string representation of the product.

        Returns:
            str: Product name, price, and quantity.
        """
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity):
        """
        buy a certain quantity of the product.

        Args:
            quantity (int): The number of units to buy.

        Returns:
            float: The total price for the purchase.

        Raises:
            ValueError: If quantity is negative or exceeds stock.
        """
        if quantity < 0:
            raise ValueError("quantity must not be negative")
        if quantity > self.quantity:
            raise ValueError("the quantity to buy is more than what is in stock")

        self.set_quantity(self.quantity - quantity)
        return quantity * self.price


def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))
    print(mac.buy(100))
    print(mac.is_active())
    print(bose.name)

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == '__main__':
    main()
