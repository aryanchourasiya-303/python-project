items = []

def Add_Item():
    Item_ID = int(input("\nEnter Item ID : "))

    for item in items:
        if item["Item_ID"] == Item_ID:
            print("Item ID already exists")
            return

    Name = input("Enter Item Name : ")
    Price = float(input("Enter Price : "))
    Quantity = int(input("Enter Quantity : "))
    Category = input("Enter Category : ")

    item = {
        "Item_ID": Item_ID,
        "Name": Name,
        "Price": Price,
        "Quantity": Quantity,
        "Category": Category
    }

    items.append(item)
    print("\nItem added successfully.\n")


def View_Items():
    if items:
        print("\n------ Grocery Items ------\n")
        for item in items:
            print(
                f"ID : {item['Item_ID']} | "
                f"Name : {item['Name']} | "
                f"Price : ₹{item['Price']} | "
                f"Quantity : {item['Quantity']} | "
                f"Category : {item['Category']}"
            )
    else:
        print("\nNo items found.")


def Search_Item():
    Item_ID = int(input("\nEnter Item ID : "))

    for item in items:
        if item["Item_ID"] == Item_ID:
            print(
                f"\nID : {item['Item_ID']} | "
                f"Name : {item['Name']} | "
                f"Price : ₹{item['Price']} | "
                f"Quantity : {item['Quantity']} | "
                f"Category : {item['Category']}"
            )
            return

    print("\nItem not found.")


def Update_Item():
    Item_ID = int(input("\nEnter Item ID : "))

    for item in items:
        if item["Item_ID"] == Item_ID:
            print("\nWhat do you want to update?")
            print("1. Name")
            print("2. Price")
            print("3. Quantity")
            print("4. Category")

            choice = input("\nEnter choice : ")

            if choice == '1':
                item["Name"] = input("Enter New Name : ")
            elif choice == '2':
                item["Price"] = float(input("Enter New Price : "))
            elif choice == '3':
                item["Quantity"] = int(input("Enter New Quantity : "))
            elif choice == '4':
                item["Category"] = input("Enter New Category : ")
            else:
                print("Invalid choice")
                return

            print("\nItem updated successfully")
            return

    print("\nItem not found.")


def Delete_Item():
    Item_ID = int(input("\nEnter Item ID : "))

    for item in items:
        if item["Item_ID"] == Item_ID:
            items.remove(item)
            print("\nItem deleted successfully")
            return

    print("\nItem not found.")


def Show_Item_Count():
    print(f"\nTotal Items Available : {len(items)}")


def main_menu():
    while True:
        print("\n------ Grocery Store Management System ------\n")
        print("1. Add Item")
        print("2. View Items")
        print("3. Search Item")
        print("4. Update Item")
        print("5. Delete Item")
        print("6. Show Item Count")
        print("7. Exit")

        choice = input("\nEnter your choice : ")

        if choice == '1':
            Add_Item()
        elif choice == '2':
            View_Items()
        elif choice == '3':
            Search_Item()
        elif choice == '4':
            Update_Item()
        elif choice == '5':
            Delete_Item()
        elif choice == '6':
            Show_Item_Count()
        elif choice == '7':
            print("\nExiting Grocery Store System. Goodbye!")
            break
        else:
            print("\nInvalid choice. Try again.")


main_menu()