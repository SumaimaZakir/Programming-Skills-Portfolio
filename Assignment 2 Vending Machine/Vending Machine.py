import locale

# Set the locale for currency formatting
locale.setlocale(locale.LC_ALL, '')

# Define product dictionary with categories
products = {
    '1': {'name': 'Coke', 'price': 1.50, 'quantity': 10, 'category': 'Beverage'},
    '2': {'name': 'Sprite', 'price': 1.20, 'quantity': 15, 'category': 'Beverage'},
    '3': {'name': 'Chips', 'price': 1.00, 'quantity': 20, 'category': 'Snack'},
    '4': {'name': 'Chocolate', 'price': 1.00, 'quantity': 30, 'category': 'Snack'},
    '5': {'name': 'Water', 'price': 1.00, 'quantity': 40, 'category': 'Beverage'},
    '6': {'name': 'Orange Juice', 'price': 2.00, 'quantity': 50, 'category': 'Beverage'},
    '7': {'name': 'Granola Bar', 'price': 1.00, 'quantity': 60, 'category': 'Snack'},
    '8': {'name': 'Pretzels', 'price': 2.00, 'quantity': 70, 'category': 'Snack'},
    '9': {'name': 'Coffee', 'price': 1.00, 'quantity': 80, 'category': 'Beverage'},
    '10': {'name': 'Tea', 'price': 1.00, 'quantity': 90, 'category': 'Beverage'},
}

# Define functions
def display_menu():
    print("Welcome to the Vending Machine!")
    print("---------------------------")

    categories = set(product['category'] for product in products.values())
    for category in categories:
        print(f"\n{category}s:")
        for code, product in products.items():
            if product['category'] == category:
                print(f"{code}: {product['name']} - {locale.currency(product['price'], grouping=True)}")

def select_item():
    while True:
        code = input("Please enter the code of the item you wish to purchase (or 'finish' to complete the transaction): ")

        if code.lower() == 'exit':
            exit_program()

        if code.lower() == 'finish':
            return None  # Signal to finish the transaction

        if code not in products:
            print("Invalid code. Please enter a valid code.")
        else:
            product = products[code]
            if product['quantity'] == 0:
                print("Item out of stock. Please select another item.")
            else:
                quantity = int(input("Enter the quantity: "))
                if quantity <= product['quantity']:
                    product['quantity'] -= quantity
                    product['total_price'] = product['price'] * quantity
                    product['code'] = code  # Add the code to the product dictionary
                    return product
                else:
                    print("Insufficient stock. Please select a lower quantity.")

def process_payment(basket):
    total_price = sum(item['total_price'] for item in basket)

    while True:
        try:
            amount_str = input(f"Please enter the total amount of money for all items in your basket ({locale.currency(total_price, grouping=True)}): ")

            if amount_str.lower() == 'exit':
                exit_program()

            amount = float(amount_str)

            if amount < 0:
                print("Please enter a non-negative amount.")
            elif amount < total_price:
                print("Insufficient funds. Please enter the correct total amount.")
            else:
                change = amount - total_price
                return change
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def update_inventory(basket):
    for item in basket:
        code = item['code']
        product = products[code]
        product['quantity'] -= item['quantity']

def dispense_items(basket):
    for item in basket:
        print(f"Dispensing {item['name']}.")

def display_change(change, basket):
    formatted_change = locale.currency(change, grouping=True)
    print(f"Your change is {formatted_change}.")

    # Print the bill
    print("\n===== Receipt =====")
    for item in basket:
        print(f"Item: {item['name']}")
        print(f"Price: {locale.currency(item['price'], grouping=True)}")
        print(f"Quantity: {item['quantity']}")
        print(f"Total Price: {locale.currency(item['total_price'], grouping=True)}")
    print(f"Total Price: {locale.currency(sum(item['total_price'] for item in basket), grouping=True)}")
    print(f"Change: {formatted_change}")
    print("===================")

def exit_program():
    print("Exiting the Vending Machine. Thank you for using!")
    exit()

# Main program loop
while True:
    display_menu()

    basket = []
    while True:
        product = select_item()
        if product is None:  # Finish transaction
            break
        else:
            basket.append(product)
            dispense_items([product])

    total_change = process_payment(basket)
    display_change(total_change, basket)
    update_inventory(basket)

    print("Thank you for your purchase!")
    input("Press")
