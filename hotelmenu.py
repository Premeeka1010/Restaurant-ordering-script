#Define menu pf restaurant
menu = {
    'Burger': 80,
    'Pizza': 100,
    'Salad': 70,
    'Sandwich': 90,
    'Fries': 20,
    'Coffee': 30,
}

print("Welcome to our restaurant!")
print("Here is our menu:")
print("Pizza: Rs.100 \nBurger: Rs.80 \nSalad: Rs.70 \nSandwich: Rs.90 \nFries: Rs.20 \nCoffee: Rs.30")

Order_total = 0

item_1 = input("Enter the name of item you want to order: ")
if item_1 in menu:
    Order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")
else:
    print(f"Sorry! Ordered item {item_1} is not available")

another_order = input("Do you want to add another item? (Yes/No): ").strip()
if another_order == "yes":
    item_2 = input("Enter the name of item you want to order: ")
    if item_2 in menu:
        Order_total += menu[item_2]
        print(f"Your item {item_2} has been added to your order")
    else:
        print(f"Sorry! Ordered item {item_2} is not available")

print(f"The total amount of items is Rs. {Order_total} to pay")
