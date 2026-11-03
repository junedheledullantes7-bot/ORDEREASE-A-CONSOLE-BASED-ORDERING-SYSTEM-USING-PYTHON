#============================================
# ORDEREASE: A CONSOLE-BASED ORDERING SYSTEM USING PYTHON
# GROUP 9 - BELOW FIVE FEET
#============================================

from datetime import datetime

#============================================
# MENU
#============================================

food_menu = {
    1: ["Burger", 25],
    2: ["Jolly hotdog", 35],
    3: ["Banana cue", 15]
}

drink_menu = {
    1: ["Koolers", 15],
    2: ["Chuckie", 45],
    3: ["Coke", 25]
}

#============================================
# ORDER RECORDS
#============================================

orders = []
order_number = 1


# ============================================
# VIEW MENU
# ============================================

def display_menu():

    print("\n========================================")
    print("              ORDEREASE")
    print("          SCHOOL CANTEEN MENU")
    print("========================================")

    print("\n========== FOOD ==========")

    if len(food_menu) == 0:
        print("No food available.")
    else:
        for number, item in food_menu.items():
            print(number, ".", item[0], "- ₱", format(item[1], ".2f"))

    print("\n========= DRINKS =========")

    if len(drink_menu) == 0:
        print("No drinks available.")
    else:
        for number, item in drink_menu.items():
            print(number, ".", item[0], "- ₱", format(item[1], ".2f"))

    print("\n========================================")


# ============================================
# FOOD
# ============================================

def choose_food(cart):

    while True:

        print("\n========== FOOD ==========")

        for number, item in food_menu.items():
            print(number, ".", item[0], "- ₱", format(item[1], ".2f"))

        print("0. Back")

        try:
            choice = int(input("\nSelect food: "))

            if choice == 0:
                return

            if choice in food_menu:

                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue

                item = food_menu[choice]

                cart.append({
                    "name": item[0],
                    "price": item[1],
                    "quantity": quantity
                })

                print("\nItem added to cart!")

            else:
                print("Invalid food number.")

        except ValueError:
            print("Please enter a valid number.")


# ============================================
# DRINKS
# ============================================

def choose_drink(cart):

    while True:

        print("\n========= DRINKS =========")

        for number, item in drink_menu.items():
            print(number, ".", item[0], "- ₱", format(item[1], ".2f"))

        print("0. Back")

        try:
            choice = int(input("\nSelect drink: "))

            if choice == 0:
                return

            if choice in drink_menu:

                quantity = int(input("Enter quantity: "))

                if quantity <= 0:
                    print("Quantity must be greater than zero.")
                    continue

                item = drink_menu[choice]

                cart.append({
                    "name": item[0],
                    "price": item[1],
                    "quantity": quantity
                })

                print("\nItem added to cart!")

            else:
                print("Invalid drink number.")

        except ValueError:
            print("Please enter a valid number.")


# ============================================
# VIEW CART
# ============================================

def view_cart(cart):

    if len(cart) == 0:
        print("\nYour cart is empty.")
        return

    print("\n========== YOUR CART ==========")

    total = 0

    for number, item in enumerate(cart, 1):

        subtotal = item["price"] * item["quantity"]

        print("\n", number, ".", item["name"])
        print("   Quantity:", item["quantity"])
        print("   Price: ₱", format(item["price"], ".2f"))
        print("   Subtotal: ₱", format(subtotal, ".2f"))

        total = total + subtotal

    print("\n--------------------------------")
    print("GRAND TOTAL: ₱", format(total, ".2f"))
    print("--------------------------------")


# ============================================
# REMOVE FROM CART
# ============================================

def remove_from_cart(cart):

    if len(cart) == 0:
        print("\nYour cart is empty.")
        return

    view_cart(cart)

    try:
        choice = int(input("\nEnter item number to remove: "))

        if choice >= 1 and choice <= len(cart):

            removed = cart.pop(choice - 1)

            print("\n", removed["name"], "removed from cart.")

        else:
            print("Invalid item number.")

    except ValueError:
        print("Please enter a valid number.")


# ============================================
# CHECKOUT / CREATE PENDING ORDER
# ============================================

def checkout(cart, customer_name):

    if len(cart) == 0:
        print("\nYour cart is empty.")
        return False

    total = 0

    for item in cart:
        total = total + (item["price"] * item["quantity"])

    now = datetime.now()

    order_id = "ORD-" + str(len(orders) + 1).zfill(3)

    # Create order as PENDING first
    order = {
        "id": order_id,
        "customer": customer_name,
        "items": list(cart),
        "total": total,
        "cash": 0,
        "change": 0,
        "payment": "NOT PAID",
        "date": now.strftime("%B %d, %Y"),
        "time": now.strftime("%I:%M %p"),
        "datetime": now,
        "status": "PENDING"
    }

    orders.append(order)

    print("\n========================================")
    print("          ORDER CREATED")
    print("========================================")

    print("Order ID:", order["id"])
    print("Customer:", order["customer"])
    print("Status:", order["status"])

    print("\nItems:")

    for item in order["items"]:

        subtotal = item["price"] * item["quantity"]

        print(
            "-",
            item["name"],
            "x",
            item["quantity"],
            "= ₱",
            format(subtotal, ".2f")
        )

    print("\n----------------------------------------")
    print(
        "CURRENT TOTAL: ₱",
        format(order["total"], ".2f")
    )
    print("----------------------------------------")

    print("\nOrder is currently PENDING.")
    print("You may update the order before completing it.")

    return True

# ============================================
# RECEIPT
# ============================================

def print_receipt(order):

    print("\n========================================")
    print("              ORDEREASE")
    print("               RECEIPT")
    print("========================================")

    print("Order ID:", order["id"])
    print("Customer:", order["customer"])
    print("Date:", order["date"])
    print("Time:", order["time"])

    print("----------------------------------------")

    for item in order["items"]:

        subtotal = item["price"] * item["quantity"]

        print("\nItem:", item["name"])
        print("Quantity:", item["quantity"])
        print("Price per item: ₱", format(item["price"], ".2f"))
        print("Subtotal: ₱", format(subtotal, ".2f"))

    print("----------------------------------------")

    print("GRAND TOTAL:   ₱", format(order["total"], ".2f"))
    print("CASH RECEIVED: ₱", format(order["cash"], ".2f"))
    print("CHANGE:        ₱", format(order["change"], ".2f"))
    print("PAYMENT:       ", order["payment"])

    print("----------------------------------------")
    print("          THANK YOU!")
    print("========================================")

    print("\nOrder successfully recorded.")


# ============================================
# PLACE ORDER
# ============================================

def place_order():

    cart = []

    while True:

        print("\n========================================")
        print("              ORDEREASE")
        print("       SCHOOL CANTEEN ORDERING")
        print("========================================")

        print("\n1. Food")
        print("2. Drinks")
        print("3. View Cart")
        print("4. Create Pending Order")
        print("5. Cancel Cart")
        print("6. Back")

        try:

            choice = int(input("\nEnter choice: "))

            if choice == 1:

                choose_food(cart)

            elif choice == 2:

                choose_drink(cart)

            elif choice == 3:

                view_cart(cart)

            elif choice == 4:

                if len(cart) == 0:

                    print("\nYour cart is empty.")

                else:

                    name = input("\nEnter customer name: ")

                    if name == "":
                        name = "Walk-in Customer"

                    created = checkout(cart, name)

                    if created:
                        break

            elif choice == 5:

                cart.clear()

                print("\nCart cancelled.")

                break

            elif choice == 6:

                break

            else:

                print("Invalid choice.")

        except ValueError:

            print("Please enter a valid number.")



# ============================================
# DISPLAY ALL ORDERS
# ============================================

def display_orders():

    print("\n========================================")
    print("           ALL ORDER RECORDS")
    print("========================================")

    if len(orders) == 0:
        print("No orders recorded yet.")
        return

    for order in orders:

        print("\nOrder ID:", order["id"])
        print("Customer:", order["customer"])
        print("Date:", order["date"])
        print("Time:", order["time"])

        print("Items:")

        for item in order["items"]:

            subtotal = item["price"] * item["quantity"]

            print(
                " -",
                item["name"],
                "x",
                item["quantity"],
                "= ₱",
                format(subtotal, ".2f")
            )

        print("Grand Total: ₱", format(order["total"], ".2f"))
        print("Payment:", order["payment"])
        print("Status:", order["status"])

        print("----------------------------------------")



# ============================================
# SEARCH ORDER
# ============================================

def search_order():

    if len(orders) == 0:
        print("\nNo orders recorded yet.")
        return

    search = input("\nEnter Order ID or Customer Name: ")

    found = False

    for order in orders:

        if (
            search.lower() in order["id"].lower()
            or search.lower() in order["customer"].lower()
        ):

            found = True

            print("\n========================================")
            print("Order ID:", order["id"])
            print("Customer:", order["customer"])
            print("Date:", order["date"])
            print("Time:", order["time"])
            print("Total: ₱", format(order["total"], ".2f"))
            print("Payment:", order["payment"])
            print("Status:", order["status"])
            print("========================================")

    if found == False:
        print("\nOrder not found.")



# ============================================
# UPDATE ORDER
# ============================================

def update_order():

    if len(orders) == 0:
        print("\nNo orders recorded yet.")
        return

    order_id = input("\nEnter Order ID: ").upper()

    for order in orders:

        if order["id"] == order_id:

            print("\n========================================")
            print("             ORDER FOUND")
            print("========================================")

            print("Order ID:", order["id"])
            print("Customer:", order["customer"])
            print("Status:", order["status"])

            # COMPLETED ORDERS CANNOT BE UPDATED
            if order["status"] == "COMPLETED":

                print("\nThis order is already COMPLETED.")
                print("Completed orders can no longer be updated.")
                return

            # CANCELLED ORDERS CANNOT BE UPDATED
            if order["status"] == "CANCELLED":

                print("\nThis order is already CANCELLED.")
                print("Cancelled orders can no longer be updated.")
                return

            # PENDING ORDER
            while True:

                print("\n========== PENDING ORDER ==========")

                print("1. Change Customer Name")
                print("2. Edit Item Quantity")
                print("3. Add Food")
                print("4. Add Drink")
                print("5. Remove Item")
                print("6. Cancel Order")
                print("7. Complete Order")
                print("8. Back")

                try:

                    choice = int(input("\nEnter choice: "))

                    # --------------------------------
                    # CHANGE CUSTOMER NAME
                    # --------------------------------

                    if choice == 1:

                        new_name = input(
                            "Enter new customer name: "
                        )

                        if new_name != "":
                            order["customer"] = new_name

                            print(
                                "\nCustomer name successfully updated."
                            )

                    # --------------------------------
                    # EDIT ITEM QUANTITY
                    # --------------------------------

                    elif choice == 2:

                        if len(order["items"]) == 0:

                            print("\nNo items in this order.")
                            continue

                        print("\n========== ORDER ITEMS ==========")

                        for number, item in enumerate(
                            order["items"], 1
                        ):

                            print(
                                number,
                                ".",
                                item["name"],
                                "x",
                                item["quantity"]
                            )

                        try:

                            item_number = int(
                                input(
                                    "\nSelect item to edit: "
                                )
                            )

                            if (
                                item_number >= 1
                                and item_number <=
                                len(order["items"])
                            ):

                                item = order["items"][
                                    item_number - 1
                                ]

                                new_quantity = int(
                                    input(
                                        "Enter new quantity: "
                                    )
                                )

                                if new_quantity <= 0:

                                    print(
                                        "Quantity must be greater than zero."
                                    )

                                else:

                                    item["quantity"] = new_quantity

                                    # Recalculate total
                                    new_total = 0

                                    for order_item in order["items"]:

                                        new_total += (
                                            order_item["price"]
                                            * order_item["quantity"]
                                        )

                                    order["total"] = new_total

                                    print(
                                        "\nItem quantity updated."
                                    )

                            else:

                                print("Invalid item number.")

                        except ValueError:

                            print(
                                "Please enter a valid number."
                            )

                    # --------------------------------
                    # ADD FOOD
                    # --------------------------------

                    elif choice == 3:

                        print("\n========== FOOD ==========")

                        for number, item in food_menu.items():

                            print(
                                number,
                                ".",
                                item[0],
                                "- ₱",
                                format(item[1], ".2f")
                            )

                        print("0. Back")

                        try:

                            food_choice = int(
                                input("\nSelect food: ")
                            )

                            if food_choice == 0:
                                continue

                            if food_choice in food_menu:

                                quantity = int(
                                    input(
                                        "Enter quantity: "
                                    )
                                )

                                if quantity <= 0:

                                    print(
                                        "Quantity must be greater than zero."
                                    )

                                else:

                                    item = food_menu[
                                        food_choice
                                    ]

                                    order["items"].append({
                                        "name": item[0],
                                        "price": item[1],
                                        "quantity": quantity
                                    })

                                    print(
                                        "\nFood added to order."
                                    )

                            else:

                                print(
                                    "Invalid food number."
                                )

                        except ValueError:

                            print(
                                "Please enter a valid number."
                            )

                    # --------------------------------
                    # ADD DRINK
                    # --------------------------------

                    elif choice == 4:

                        print("\n========= DRINKS =========")

                        for number, item in drink_menu.items():

                            print(
                                number,
                                ".",
                                item[0],
                                "- ₱",
                                format(item[1], ".2f")
                            )

                        print("0. Back")

                        try:

                            drink_choice = int(
                                input("\nSelect drink: ")
                            )

                            if drink_choice == 0:
                                continue

                            if drink_choice in drink_menu:

                                quantity = int(
                                    input(
                                        "Enter quantity: "
                                    )
                                )

                                if quantity <= 0:

                                    print(
                                        "Quantity must be greater than zero."
                                    )

                                else:

                                    item = drink_menu[
                                        drink_choice
                                    ]

                                    order["items"].append({
                                        "name": item[0],
                                        "price": item[1],
                                        "quantity": quantity
                                    })

                                    print(
                                        "\nDrink added to order."
                                    )

                            else:

                                print(
                                    "Invalid drink number."
                                )

                        except ValueError:

                            print(
                                "Please enter a valid number."
                            )

                    # --------------------------------
                    # REMOVE ITEM
                    # --------------------------------

                    elif choice == 5:

                        if len(order["items"]) == 0:

                            print("\nNo items to remove.")
                            continue

                        print(
                            "\n========== ORDER ITEMS =========="
                        )

                        for number, item in enumerate(
                            order["items"], 1
                        ):

                            print(
                                number,
                                ".",
                                item["name"],
                                "x",
                                item["quantity"]
                            )

                        try:

                            item_number = int(
                                input(
                                    "\nSelect item to remove: "
                                )
                            )

                            if (
                                item_number >= 1
                                and item_number <=
                                len(order["items"])
                            ):

                                removed = order["items"].pop(
                                    item_number - 1
                                )

                                print(
                                    "\n",
                                    removed["name"],
                                    "removed from order."
                                )

                                # Recalculate total
                                new_total = 0

                                for order_item in order["items"]:

                                    new_total += (
                                        order_item["price"]
                                        * order_item["quantity"]
                                    )

                                order["total"] = new_total

                            else:

                                print(
                                    "Invalid item number."
                                )

                        except ValueError:

                            print(
                                "Please enter a valid number."
                            )

                    # --------------------------------
                    # CANCEL ORDER
                    # --------------------------------

                    elif choice == 6:

                        order["status"] = "CANCELLED"

                        print(
                            "\nOrder",
                            order["id"],
                            "has been CANCELLED."
                        )

                        print(
                            "This order can no longer be updated."
                        )

                        return

                                        # --------------------------------
                    # COMPLETE ORDER
                    # --------------------------------

                    elif choice == 7:

                        if len(order["items"]) == 0:

                            print("\nCannot complete an empty order.")

                            continue

                        # Recalculate final total
                        final_total = 0

                        for item in order["items"]:

                            final_total += (
                                item["price"] * item["quantity"]
                            )

                        order["total"] = final_total

                        print("\n========================================")
                        print("           FINAL CHECKOUT")
                        print("========================================")

                        print("Order ID:", order["id"])
                        print("Customer:", order["customer"])

                        print("\nFinal Items:")

                        for item in order["items"]:

                            subtotal = (
                                item["price"] * item["quantity"]
                            )

                            print(
                                "-",
                                item["name"],
                                "x",
                                item["quantity"],
                                "= ₱",
                                format(subtotal, ".2f")
                            )

                        print("\n----------------------------------------")
                        print(
                            "FINAL TOTAL: ₱",
                            format(order["total"], ".2f")
                        )
                        print("----------------------------------------")

                        # CASH PAYMENT
                        while True:

                            try:

                                cash = float(
                                    input("\nCash Received: ₱")
                                )

                                if cash < order["total"]:

                                    print(
                                        "Insufficient cash. You need ₱",
                                        format(
                                            order["total"] - cash,
                                            ".2f"
                                        ),
                                        "more."
                                    )

                                else:

                                    break

                            except ValueError:

                                print(
                                    "Please enter a valid amount."
                                )

                        change = cash - order["total"]

                        # Save payment information
                        order["cash"] = cash
                        order["change"] = change
                        order["payment"] = "CASH"
                        order["status"] = "COMPLETED"

                        print("\n========================================")
                        print("        PAYMENT SUCCESSFUL")
                        print("========================================")

                        print(
                            "Cash Received: ₱",
                            format(cash, ".2f")
                        )

                        print(
                            "Change: ₱",
                            format(change, ".2f")
                        )

                        print(
                            "\nOrder",
                            order["id"],
                            "is now COMPLETED."
                        )

                        print(
                            "This order can no longer be updated."
                        )

                        # Print final receipt
                        print_receipt(order)

                        return

                    # --------------------------------
                    # BACK
                    # --------------------------------

                    elif choice == 8:

                        return  

                    else:

                        print("Invalid choice.")

                except ValueError:

                    print(
                        "Please enter a valid number."
                    )

            return

    print("\nOrder not found.")


# ============================================
# ADD FOOD
# ============================================

def add_food():

    print("\n========== ADD FOOD ==========")

    name = input("Enter food name: ")

    try:
        price = float(input("Enter price: ₱"))

        if price <= 0:
            print("Invalid price.")
            return

    except ValueError:
        print("Please enter a valid price.")
        return

    if len(food_menu) == 0:
        number = 1
    else:
        number = max(food_menu.keys()) + 1

    food_menu[number] = [name, price]

    print("\nFood successfully added!")
    print(name, "- ₱", format(price, ".2f"))


# ============================================
# ADD DRINK
# ============================================

def add_drink():

    print("\n========== ADD DRINK ==========")

    name = input("Enter drink name: ")

    try:
        price = float(input("Enter price: ₱"))

        if price <= 0:
            print("Invalid price.")
            return

    except ValueError:
        print("Please enter a valid price.")
        return

    if len(drink_menu) == 0:
        number = 1
    else:
        number = max(drink_menu.keys()) + 1

    drink_menu[number] = [name, price]

    print("\nDrink successfully added!")
    print(name, "- P", format(price, ".2f"))



# ============================================
# EDIT FOOD PRICE
# ============================================

def edit_food_price():

    print("\n========== EDIT FOOD PRICE ==========")

    for number, item in food_menu.items():
        print(number, ".", item[0], "- ₱", format(item[1], ".2f"))

    try:

        choice = int(input("\nSelect food: "))

        if choice not in food_menu:
            print("Invalid food number.")
            return

        new_price = float(input("Enter new price: ₱"))

        if new_price <= 0:
            print("Invalid price.")
            return

        food_menu[choice][1] = new_price

        print("\nPrice successfully updated.")

    except ValueError:
        print("Please enter a valid number.")


# ============================================
# EDIT DRINK PRICE
# ============================================

def edit_drink_price():

    print("\n========== EDIT DRINK PRICE ==========")

    for number, item in drink_menu.items():
        print(number, ".", item[0], "- ₱", format(item[1], ".2f"))

    try:

        choice = int(input("\nSelect drink: "))

        if choice not in drink_menu:
            print("Invalid drink number.")
            return

        new_price = float(input("Enter new price: ₱"))

        if new_price <= 0:
            print("Invalid price.")
            return

        drink_menu[choice][1] = new_price

        print("\nPrice successfully updated.")

    except ValueError:
        print("Please enter a valid number.")

#============================================
# REMOVE ITEM
 #============================================

def remove_item():

    print("\n========== REMOVE ITEM ==========")

    print("1. Food")
    print("2. Drinks")
    print("3. Back")

    try:

        category = int(input("\nEnter choice: "))

        if category == 3:
            return

        if category == 1:

            for number, item in food_menu.items():
                print(
                    number,
                    ".",
                    item[0],
                    "- ₱",
                    format(item[1], ".2f")
                )

            choice = int(input("\nSelect food to remove: "))

            if choice in food_menu:

                name = food_menu[choice][0]

                del food_menu[choice]

                print(name, "removed.")

            else:
                print("Invalid food number.")

        elif category == 2:

            for number, item in drink_menu.items():
                print(
                    number,
                    ".",
                    item[0],
                    "- ₱",
                    format(item[1], ".2f")
                )

            choice = int(input("\nSelect drink to remove: "))

            if choice in drink_menu:

                name = drink_menu[choice][0]

                del drink_menu[choice]

                print(name, "removed.")

            else:
                print("Invalid drink number.")

        else:
            print("Invalid choice.")

    except ValueError:
        print("Please enter a valid number.")

# ============================================
# SALES RECORDS
# ============================================

def record_order():

    if len(orders) == 0:
        print("\nNo order records available.")
        return

    print("\n========================================")
    print("          ORDER / SALES RECORDS")
    print("========================================")

    print("1. Weekly Records")
    print("2. Monthly Records")
    print("3. Yearly Records")
    print("4. All Records")
    print("5. Back")

    try:
        choice = int(input("\nEnter choice: "))

    except ValueError:
        print("Please enter a valid number.")
        return

    if choice == 5:
        return

    now = datetime.now()

    selected_orders = []

    for order in orders:

        date = order["datetime"]

        if choice == 1:

            if (
                date.year == now.year
                and date.isocalendar()[1] == now.isocalendar()[1]
            ):
                selected_orders.append(order)

        elif choice == 2:

            if (
                date.year == now.year
                and date.month == now.month
            ):
                selected_orders.append(order)

        elif choice == 3:

            if date.year == now.year:
                selected_orders.append(order)

        elif choice == 4:

            selected_orders.append(order)

        else:

            print("Invalid choice.")
            return

    if len(selected_orders) == 0:

        print("\nNo records found.")
        return

    total_sales = 0

    print("\n========================================")

    if choice == 1:
        print("           WEEKLY RECORDS")

    elif choice == 2:
        print("          MONTHLY RECORDS")

    elif choice == 3:
        print("           YEARLY RECORDS")

    else:
        print("             ALL RECORDS")

    print("========================================")

    for order in selected_orders:

        print("\nOrder ID:", order["id"])
        print("Customer:", order["customer"])
        print("Date:", order["date"])
        print("Time:", order["time"])
        print("Total: ₱", format(order["total"], ".2f"))
        print("Payment:", order["payment"])
        print("Status:", order["status"])

        print("----------------------------------------")

        if order["status"] == "COMPLETED":
            total_sales = total_sales + order["total"]

    print("\nTOTAL ORDERS:", len(selected_orders))
    print("TOTAL SALES: ₱", format(total_sales, ".2f"))


# ============================================
# STAFF LOGIN
# ============================================

def staff_login():

    print("\n========================================")
    print("          ADMIN ")
    print("========================================")

    username = input("Username: ")
    password = input("Password: ")

    if username == "ADMIN" and password == "15234":

        print("\nLogin successful!")

        staff_menu()

    else:

        print("\nInvalid username or password.")


# ============================================
# STAFF MENU
# ============================================

def staff_menu():

    while True:

        print("\n========================================")
        print("              STAFF MENU")
        print("========================================")

        print("1. Add Food")
        print("2. Add Drink")
        print("3. Edit Food Price")
        print("4. Edit Drink Price")
        print("5. Remove Item")
        print("6. View Menu")
        print("7. View Order Records")
        print("8. Back")

        try:

            choice = int(input("\nEnter choice: "))

            if choice == 1:
                add_food()

            elif choice == 2:
                add_drink()

            elif choice == 3:
                edit_food_price()

            elif choice == 4:
                edit_drink_price()

            elif choice == 5:
                remove_item()

            elif choice == 6:
                display_menu()

            elif choice == 7:
                record_order()

            elif choice == 8:
                print("\nLogging out...")
                break

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")


# ============================================
# MAIN PROGRAM
# ============================================

while True:

    print("\n========================================")
    print("              ORDEREASE")
    print("       SCHOOL CANTEEN SYSTEM")
    print("========================================")

    print("\n1. View Menu")
    print("2. Place Order")
    print("3. Display All Orders")
    print("4. Search Order")
    print("5. Update Order")
    print("6. Record Order")
    print("7. Cashier / Staff Login")
    print("8. Exit")

    try:

        choice = int(input("\nEnter choice: "))

        if choice == 1:

            display_menu()

        elif choice == 2:

            place_order()

        elif choice == 3:

            display_orders()

        elif choice == 4:

            search_order()

        elif choice == 5:

            update_order()

        elif choice == 6:

            record_order()

        elif choice == 7:

            staff_login()

        elif choice == 8:

            print("\nThank you for using OrderEase!")
            break

        else:

            print("Invalid choice.")

    except ValueError:

        print("Please enter a valid number.")
