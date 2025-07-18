#Define menu pf restaurant
# Restaurant ordering script

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
for item, price in menu.items():
    print(f"{item}: Rs.{price}")

order_total = 0

while True:
    item = input("\nEnter the name of the item you want to order: ").strip().title()
    if item in menu:
        order_total += menu[item]
        print(f" Added '{item}' to your order. (Rs.{menu[item]})")
    else:
        print(f" Sorry, '{item}' is not on the menu.")

    more = input("Do you want to add another item? (yes/no): ").strip().lower()
    if more != 'yes':
        break

print(f"\nYour total amount to pay is Rs. {order_total}.")
print("Thanks for your order! ")
