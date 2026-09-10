menu = {
    1: {"name": "Pizza", "price": 250},
    2: {"name": "Burger", "price": 120},
    3: {"name": "Pasta", "price": 180},
    4: {"name": "Sandwich", "price": 100},
    5: {"name": "Cold Drink", "price": 60}
}

orders = []


def display_menu():
    print("\n========== RESTAURANT MENU ==========")
    print("ID\tItem\t\tPrice")
    print("-------------------------------------")

    for item_id, item in menu.items():
        print(f"{item_id}\t{item['name']:<15} ₹{item['price']}")


def take_order():
    while True:
        display_menu()

        item_id = int(input("\nEnter Item ID (0 to finish): "))

        if item_id == 0:
            break

        if item_id not in menu:
            print("Invalid Item ID!")
            continue

        quantity = int(input("Enter Quantity: "))

        order = {
            "name": menu[item_id]["name"],
            "price": menu[item_id]["price"],
            "quantity": quantity
        }

        orders.append(order)

        print("Item added to order!")


def calculate_bill():
    subtotal = 0

    for order in orders:
        subtotal += order["price"] * order["quantity"]

    gst = subtotal * 0.05
    total = subtotal + gst

    return subtotal, gst, total


def generate_receipt():
    if not orders:
        print("\nNo items ordered!")
        return

    subtotal, gst, total = calculate_bill()

    print("\n=====================================")
    print("          RESTAURANT RECEIPT")
    print("=====================================")
    print("Item\t\tPrice\tQty\tAmount")
    print("-------------------------------------")

    for order in orders:
        amount = order["price"] * order["quantity"]
        print(
            f"{order['name']:<15}"
            f"₹{order['price']:<7}"
            f"{order['quantity']:<7}"
            f"₹{amount}"
        )

    print("-------------------------------------")
    print(f"Subtotal:\t\t\t₹{subtotal:.2f}")
    print(f"GST 5%:\t\t\t\t₹{gst:.2f}")
    print(f"Total Bill:\t\t\t₹{total:.2f}")
    print("=====================================")
    print("       Thank You! Visit Again")
    print("=====================================")


def main():
    while True:
        print("\n========== RESTAURANT SYSTEM ==========")
        print("1. Display Menu")
        print("2. Take Order")
        print("3. Generate Receipt")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_menu()

        elif choice == "2":
            take_order()

        elif choice == "3":
            generate_receipt()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice!")


main()