from products import Product
from store import Store


def display_menu() -> None:
    """
    Print the main store menu.
    """
    print("\nStore Menu")
    print("----------")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")
    print("----------")

def list_products(store: Store) -> None:
    """
    Print all active products with an index.
    """
    products = store.get_all_products()
    print("----------")
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product.show()}")
    print("----------")

def show_total_quantity(store: Store) -> None:
    """
    Print the total quantity of all products in the store.
    """
    total_quantity = store.get_total_quantity()
    print(f"\nTotal of {total_quantity} items in store")

def build_shopping_list(store: Store) -> list[tuple[Product, int]]:
    """
    Collect user order input and build a shopping list.

    Returns:
        list[tuple[Product, int]]: List of (Product, quantity).
    """
    products = store.get_all_products()
    if not products:
        print("No active products available.")
        return []

    print("\n----------")
    print("Available products:")
    for index, product in enumerate(products, start=1):
        print(f"{index}. {product.show()}")
    print("----------")

    shopping_list: list[tuple[Product, int]] = []

    while True:
        print("When you want to finish order, enter empty text.")
        product_input = input("Which product # do you want? ").strip()

        # Empty input = finish order.
        if product_input == "":
            break

        amount_input = input("What amount do you want? ").strip()

        try:
            product_index = int(product_input) - 1
            amount = int(amount_input)

            # Check if product is valid.
            if product_index < 0 or product_index >= len(products):
                print("⚠️ Invalid product number.")
                continue
            if amount <= 0:
                print("⚠️ Amount must be positive.")
                continue

            # If everything's correct --> add product to shopping list.
            shopping_list.append((products[product_index], amount))
            print("✅ Product added to list!")

        except ValueError:
            print("⚠️ Invalid input. Please enter numbers only.")

    return shopping_list

def make_order(store: Store) -> None:
    """
    Handle order creation and processing.
    """
    shopping_list = build_shopping_list(store)
    if not shopping_list:
        print("No items ordered.")
        return

    try:
        total_price = store.order(shopping_list)
        print("\n********")
        print(f"Order made. Total payment ${total_price:.2f}")
    except Exception as e:
        print(f"⚠️ Error while making order! {e} ⚠️")

def handle_choice(choice: str, store: Store) -> bool:
    """
    Execute a menu choice.

    Returns:
        bool: True to continue, False to quit.
    """
    if choice == "1":
        list_products(store)                        # List all active products.
    elif choice == "2":
        show_total_quantity(store)                  # Show quantity in store.
    elif choice == "3":
        make_order(store)                           # Make order and process it.
    elif choice == "4":
        print("Goodbye! 👋")
        return False
    else:
        print("⚠️ Invalid choice, please select a number between 1 and 4. ⚠️")
    return True

def start(store: Store) -> None:
    """
    Starts the interactive store menu loop.
    """
    running = True
    while running:
        display_menu()
        choice = input("Please choose a number: ").strip()
        running = handle_choice(choice, store)

def main():
    """
    Create initial products and run the store app.
    """
    # Setup initial stock of inventory.
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()
