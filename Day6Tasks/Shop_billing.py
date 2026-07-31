products = {
    "Pen": 10,
    "Notebook": 50,
    "Pencil": 5
}

categories = {"Stationery", "Office Supplies"}

cart = []  # each item stored as a tuple: (product_name, quantity, price)


def display_products():
    print("Available Products:")
    for name, price in products.items():
        print(f"{name} : {price}")


def add_to_cart():
    name = input("Enter product name: ")

    try:
        if name not in products:
            raise NameError("Product not found in store.")

        quantity = int(input("Enter quantity: "))
        price = products[name]

        cart.append((name, quantity, price))
        print("Item added to cart successfully.")

    except NameError as e:
        print(e)
    except ValueError:
        print("Invalid quantity! Please enter a number.")


def total_price(cart_list):
    """Recursive function to calculate the total price of all items in the cart."""
    if not isinstance(cart_list, list):
        raise TypeError("Cart data type error.")
    if len(cart_list) == 0:
        return 0

    item = cart_list[0]
    if not isinstance(item, tuple) or len(item) != 3:
        raise TypeError("Cart data type error.")

    _, quantity, price = item
    return (quantity * price) + total_price(cart_list[1:])


def view_total_bill():
    try:
        if not cart:
            print("Your cart is empty.")
            return

        print("Items in Cart:")
        for name, quantity, price in cart:
            print(f"{name} x {quantity}")

        total = total_price(cart)
        average_per_item = total / len(cart)

        print(f"Total Bill: {total}")
        print(f"Average Bill per Item: {average_per_item:.2f}")

    except TypeError as e:
        print(e)
    except ZeroDivisionError:
        print("Calculation error: division by zero.")


def main():
    while True:
        print("\n1. Display Products")
        print("2. Add Item to Cart")
        print("3. View Total Bill")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            display_products()
        elif choice == "2":
            add_to_cart()
        elif choice == "3":
            view_total_bill()
        elif choice == "4":
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Please select a number between 1 and 4.")


if __name__ == "__main__":
    main()
    