def inventory_management_system():
    # Our main inventory storage - simple dictionary
    inventory = {}
    
    # Keep the system running until user exits
    while True:
        print("\n1. Add item")
        print("2. Update item")
        print("3. View inventory")
        print("4. Exit")
        
        # Get user choice - we'll handle invalid options
        choice = input("Choose option: ").strip()
        
        # Option 1: Add new item to inventory
        if choice == '1':
            item = input("Item name: ").lower().strip()
            
            # Check if item already exists
            if not item:  # Empty input check
                print("Hey, you need to enter an item name!")
                continue
                
            if item in inventory:
                print(f"Whoops! '{item}' is already in inventory.")
                continue
                
            # Get quantity with proper validation
            try:
                quantity = int(input("Quantity: ").strip())
                if quantity < 0:
                    print("Come on, we can't have negative items!")
                    continue
                inventory[item] = quantity
                print(f"Cool, added {quantity} of '{item}'")
            except ValueError:
                print("That's not a valid number, try again!")
                
        # Option 2: Update existing item quantity
        elif choice == '2':
            item = input("Item name: ").lower().strip()
            
            # Check if item exists first
            if not item:
                print("You forgot to enter an item name!")
                continue
                
            if item not in inventory:
                print(f"Sorry, '{item}' isn't in our inventory yet.")
                continue
                
            # Get new quantity with validation
            try:
                new_qty = int(input(f"New quantity for {item}: ").strip())
                if new_qty < 0:
                    print("Negative quantities don't make sense here!")
                    continue
                inventory[item] = new_qty
                print(f"Updated '{item}' to {new_qty}")
            except ValueError:
                print("Oops! That's not a proper number.")
                
        # Option 3: Show current inventory
        elif choice == '3':
            if not inventory:
                print("Our inventory is empty right now.")
            else:
                print("Current inventory:")
                for item, qty in inventory.items():
                    print(f"- {item}: {qty}")
                    
        # Option 4: Exit the program
        elif choice == '4':
            print("Alright, closing up shop. Bye!")
            break
            
        # Handle any other invalid options
        else:
            print("Hmm, that's not a valid option. Try 1-4.")

# Let's get this party started!
inventory_management_system()