from store import Store
from products import Product

# Initial list of products
PRODUCT_LIST = [
    Product("MacBook Air M2", price=1450, quantity=100),
    Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    Product("Google Pixel 7", price=500, quantity=250)
]

# Initialize the store with the product list
STORE = Store(PRODUCT_LIST)


def make_order_item(products):
    """
    Displays a list of products and prompts the user to choose a product and amount.

    Args:
        products (list): A list of Product instances.

    Returns:
        tuple: A tuple of (Product, quantity) if valid input is given.
        bool: False if input is empty or invalid.
    """
    index = 1
    print("---")
    for p in products:
        print(f"{index}. {p.show()}")
        index += 1
    print("---")
    print("When you want to finish order, enter empty text.")
    p_choice = input("Which product number do you want? ")
    am_choice = input("What amount do you want? ")

    if not am_choice:
        return False

    if int(p_choice) < 1 or int(p_choice) > len(products):
        print("Error adding product!")
        return False

    return products[int(p_choice) - 1], int(am_choice)


def make_order(store):
    """
    Collects order items from the user and processes the order using the store.

    Args:
        store (Store): The store instance from which to order products.
    """
    order_items = []
    while True:
        order_item = make_order_item(store.get_all_products())
        if order_item:
            order_items.append(order_item)
            print("Product added to list!")
            print("")
        else:
            break

    if len(order_items) > 0:
        print()
        print("*********")
        total_price = store.order(order_items)
        if total_price:
            print(f"Order made! Total Payment: {total_price}")
        else:
            return


def start(store):
    """
    Starts the CLI interface for interacting with the store.

    Args:
        store (Store): The store instance to interact with.
    """
    best_buy = store

    while True:
        print("   Store")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        try:
            choice = int(input("Please choose a number "))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            for p in best_buy.get_all_products():
                print(p.show())
            print()
        elif choice == 2:
            print(f"Total of {best_buy.get_total_quantity()} items in store")
            print()
        elif choice == 3:
            make_order(best_buy)
            print()
        elif choice == 4:
            exit()


if __name__ == '__main__':
    start(STORE)
