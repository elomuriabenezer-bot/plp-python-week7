# Week 7 Part B: Shopping List Manager

shopping_list = []

while True:
    print("\nShopping List Manager")
    print("Choose: add / remove / show / done")
    action = input("Your choice: ").strip().lower()

    if action == "add":
        item = input("Item to add: ").strip()
        if item:
            shopping_list.append(item)
            print(f"Added {item}.")

    elif action == "remove":
        item = input("Item to remove: ").strip()
        if item in shopping_list:
            shopping_list.remove(item)
            print(f"Removed {item}.")
        else:
            print("That item is not on your list.")

    elif action == "show":
        if shopping_list:
            print("Your shopping list:")
            for item in shopping_list:
                print(f"- {item}")
        else:
            print("Your shopping list is empty.")

    elif action == "done":
        print("Goodbye!")
        break

    else:
        print("Please choose add, remove, show, or done.")
