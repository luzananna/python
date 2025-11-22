# TASK: Grocery Manager (Lists & Tuples)

# Requirements
# 1.	Add items
# 	Ask the user how many items they want to add.
# 	For each item, ask for:
# 	item name (string)
# 	quantity (integer)
# 	price per unit (float)
# 	Store each item as a tuple:
# (name, quantity, price)
# Add all tuples into a list.

# 	2.	Display the list
# 	Print all items in a clean format, e.g.:
# Bread  x1 — €2.50

# 	3.	Calculate total cost
# 	Compute the sum of quantity * price for all items.
# 	Print:
# Total cost: €...

# 	4.	Remove an item (optional)
# 	Ask: "Do you want to remove an item? (yes/no)"
# 	If yes: ask for the item name and remove the matching tuple if it exists.

# 	5.	Sort items (optional)
# 	Ask: "Sort by name, quantity, or price?"
#   Sort the list accordingly. 

def ask_item_count():
    """Ask how many grocery items the user wants to add."""
    while True:
        count = input("How many items do you want to add? ")
        
        if count.isdigit() and int(count) > 0:
            return int(count)
        print("Please enter a positive number.")


def add_items():
    """Ask the user for item details and return a list of tuples (name, quantity, price)."""
    items = []
    count = ask_item_count()

    for i in range(1, count + 1):
        print(f"\nItem {i}:")

        name = input("Enter item name: ").strip()

        # quantity
        while True:
            q = input("Enter quantity: ")
            if q.isdigit():
                quantity = int(q)
                break
            print("Quantity must be a number.")

        # price
        while True:
            p = input("Enter price: ")
            try:
                price = float(p)
                break
            except ValueError:
                print("Price must be a number.")

        items.append((name, quantity, price))

    return items


def display_items(items):
    """Print all items in a clean, consistent format."""
    print("\n=== Grocery List ===")
    if not items:
        print("No items.")
        return

    for name, quantity, price in items:
        print(f"{name.ljust(15, '.')} x{quantity} — €{price:.2f}")


def calculate_total(items):
    """Return the total cost of all items."""
    return sum(quantity * price for _, quantity, price in items)


def remove_item(items):
    """Remove an item by name if the user wants to."""
    answer = input("\nDo you want to remove an item? (yes/no): ").lower().strip()

    if answer not in ("yes", "y"):
        return

    name_to_remove = input("Enter the item name to remove: ").strip()

    for item in items:
        if item[0].lower() == name_to_remove.lower():
            items.remove(item)
            print(f"Removed '{name_to_remove}'.")
            return

    print("Item not found.")


def sort_items(items):
    """Sort the list by name, quantity, or price."""
    answer = input("\nSort by name, quantity, or price? ").lower().strip()

    if answer == "name":
        items.sort(key=lambda x: x[0])
    elif answer == "quantity":
        items.sort(key=lambda x: x[1])
    elif answer == "price":
        items.sort(key=lambda x: x[2])
    else:
        print("Unknown sorting option.")


def main():
    print("=== Grocery Manager ===")

    items = add_items()

    display_items(items)

    total = calculate_total(items)
    print(f"\nTotal cost: €{total:.2f}")

    remove_item(items)

    sort_items(items)

    print("\nFinal items:")
    display_items(items)


if __name__ == "__main__":
    main()