cafe_name = "Python Cafe"
tax_rate = 0.08

menu = {
    "espresso": 3.50,
    "latte": 4.50,
    "cappuccino": 4.25,
    "mocha" : 5.00,
    "muffin" : 2.50,
    "croissant" : 3.25,
}

order = []

def greet(name):
    print(f"Welcome to {cafe_name}, {name}!")


def show_menu():
    for item, price in menu.items():
        print(f"{item.title()}: ${price:.2f}")


def show_order():
    if not order:
        print("Your order is currently empty.")
    else:
        print("Your current order:")
        for item in order:
            print(f"- {item.title()}: ${menu[item]:.2f}")


def calculate_subtotal(order, menu):
    subtotal = sum(menu[item] for item in order)
    return subtotal


def get_discount(subtotal, is_member): #add the proper discount and taxes
    if is_member:
        if subtotal >= 20:
            return subtotal * 0.15
        elif subtotal >= 10:
            return subtotal * 0.10
        else:
            return 0
    else:
        return subtotal * 0.05
    

def print_receipt(name, order, menu, is_member):
    subtotal = calculate_subtotal(order, menu)
    discount = get_discount(subtotal, is_member)
    tax = (subtotal - discount) * tax_rate
    total = subtotal - discount + tax

    print("\n--- Receipt ---")
    print(f"Customer: {name}")

    for item in menu:
        quantity = order.count(item)
        if quantity > 0:
            print(f"{item.title()} x{quantity}: ${menu[item] * quantity:.2f}")

    print(f"Subtotal: ${subtotal:.2f}")

    if discount > 0:
        if is_member:
            print(f"Member Discount: -${discount:.2f}")
        else:
            print(f" Discount: -${discount:.2f}")
      
    print(f"Tax: ${tax:.2f}")
    print(f"Total: ${total:.2f}")
    print("Thank you for visiting Python Cafe!")


def get_quantity():
    while True:
        quantity = input("Enter the quantity (must be greater than 0): ")
        if quantity.isdigit():
            quantity = int(quantity)
            if quantity > 0:
                return quantity
            else:
                print("Quantity must be greater than 0. Please try again.")
        else:
            print("Invalid input. Please enter a positive integer.")


def main():     
    print(f"Welcome to {cafe_name}!")
    name = input("Please enter your name: ")
    greet(name)
    is_member = input("Are you a member? (yes/no): ").strip().lower() == "yes"
    while True:
        choice = input("Would you like to (1) view the menu, (2) add an item to your order, (3) remove an item, (4) view your order, or (5) checkout? (Enter 1, 2, 3, 4, or 5): ")
        if choice == "1":
            show_menu()

        elif choice == "2":
            item = input("Enter the item you want to add: ").strip().lower()
            if item in menu:
                quantity = get_quantity()
                for _ in range(quantity):
                    order.append(item)
                print (f"{quantity} {item.title()}(s) have been added to your order.")

            else:
                print("Sorry, that item is not on the menu.")

        elif choice == "3":
            item = input("Enter the item you want to remove: ").strip().lower()
            if item in order:
                quantity = get_quantity()
                for _ in range(quantity):
                    order.remove(item)
                print(f"{quantity} {item.title()}(s) have been removed from your order.")
            else:
                print("That item is not in your order.")

        elif choice == "4":
            show_order()

        elif choice == "5":
            if not order:
                print("Your order is empty. Please add an item before checking out.")
            else:
                print_receipt(name, order, menu, is_member)
                break
        else:
            print("Invalid choice. Please try again.")

main()


