inventory = [
    ["books", 10, 500],
    ["pens", 25, 20],
    ["pencils", 15, 40],
    ["ruler", 8, 200]
]

def display_inventory():
    print("\n--- INVENTORY ---")
    for i in range(len(inventory)):
        item = inventory[i]
        print(f"{i+1}. {item[0]} - Quantity: {item[1]} - Price: ${item[2]}")

def add_item():
    name = input("Enter item name: ")
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            break
        except ValueError:
            print("Please enter a valid number for quantity!")
    
    
    while True:
        try:
            price = float(input("Enter price: "))
            break
        except ValueError:
            print("Please enter a valid number for price!")
    
    inventory.append([name, quantity, price])
    print(f"Added {name} to inventory!")

def update_quantity():
    display_inventory()
    
    while True:
        try:
            item_num = int(input("\nEnter item number to update: ")) - 1
            break
        except ValueError:
            print("Please enter a valid number!")
    
    # Check if item exists
    if 0 <= item_num < len(inventory):
        while True:
            try:
                new_qty = int(input(f"Enter new quantity for {inventory[item_num][0]}: "))
                break
            except ValueError:
                print("Please enter a valid number!")
        
        inventory[item_num][1] = new_qty
        print(f"Updated {inventory[item_num][0]} quantity to {new_qty}")
    else:
        print("Invalid item number!")

def update_price():
    display_inventory()
    while True:
        try:
            item_num = int(input("\nEnter item number to update: ")) - 1
            break
        except ValueError:
            print("Please enter a valid number!")
    
    # Check if item exists
    if 0 <= item_num < len(inventory):
        while True:
            try:
                new_price = float(input(f"Enter new price for {inventory[item_num][0]}: "))
                break
            except ValueError:
                print("Please enter a valid number!")
        
        inventory[item_num][2] = new_price
        print(f"Updated {inventory[item_num][0]} price to ${new_price}")
    else:
        print("Invalid item number!")

def remove_item():
    display_inventory()
    while True:
        try:
            item_num = int(input("\nEnter item number to remove: ")) - 1
            break
        except ValueError:
            print("Please enter a valid number!")
    
    # Check if item exists
    if 0 <= item_num < len(inventory):
        removed_item = inventory.pop(item_num)
        print(f"Removed {removed_item[0]} from inventory!")
    else:
        print("Invalid item number!")

def main():
    while True:
        print("\n1. Display Inventory")
        print("2. Add Item")
        print("3. Update Quantity")
        print("4. Update Price")
        print("5. Remove Item")
        print("6. Exit")
        
        
        while True:
            try:
                choice = int(input("Choose option: "))
                break
            except ValueError:
                print("Please enter a valid number!")
        
        if choice == 1:
            display_inventory()
        elif choice == 2:
            add_item()
        elif choice == 3:
            update_quantity()
        elif choice == 4:
            update_price()
        elif choice == 5:
            remove_item()
        elif choice == 6:
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please choose 1-6.")


if __name__ == "__main__":
    main()