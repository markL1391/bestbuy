from products import Product
from store import Store

def start(store):
    while True:
        print("Store Menu")
        print("----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            # List all active products
            products = store.get_all_products()
            print("----------")
            for index, product in enumerate(products, start = 1):
                print(f"{index}. ", end="")
                product.show()
            print("----------")

        elif choice == "2":
            # Show quantity in store
            total_quantity = store.get_total_quantity()
            print(f"\nTotal of {total_quantity} items in store")

        elif choice == "3":
            # Make an order
            products = store.get_all_products()

            print("\n----------")
            print("Available products:")
            for index, product in enumerate(products, start = 1):
                print(f"{index}. ", end="")
                product.show()
            print("----------")

            shopping_list = []

            while True:
                print("When you want to finish order, enter empty text.")
                product_input = input("Which product # do you want? ")

                # Empty input = finish order
                if product_input == "":
                    break

                amount_input = input("What amount do you want? ").strip()

                try:
                    product_index = int(product_input) - 1
                    amount = int(amount_input)

                    # Check if product is valid
                    if product_index < 0 or product_index >= len(products):
                        raise Exception("Invalid product number")

                    # If everything's correct --> add product to shopping list
                    shopping_list.append((products[product_index], amount))
                    print("✅ Product added to list!")

                except Exception:
                    print("Error adding product")

            try:
                total_price = store.order(shopping_list)
                print("\n********")
                print(f"Order made. Total payment ${total_price}")
            except Exception as e:
                print(f"⚠️ Error while making order! {e} ⚠️")

        elif choice == "4":
            print("Goodbye! 👋")

        else:
            print("⚠️ Invalid choice, please select a number between 1 and 4. ⚠️")

def main():
    # Setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    start(best_buy)

if __name__ == "__main__":
    main()