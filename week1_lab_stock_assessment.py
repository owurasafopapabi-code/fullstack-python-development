# Program helps a lab to check final stock quantity of an item 
# and interpret the stock status

def calculate_final_quantity(starting_quantity, quantity_used, quantity_received):
    return starting_quantity - quantity_used + quantity_received


def get_stock_status(final_quantity):
    if final_quantity <= 0:
        return "Out of Stock"
    elif 1 <= final_quantity <= 9:
        return "Low Stock"
    elif 10 <= final_quantity <= 50:
        return "Moderate Stock"
    else:
        return "Sufficient Stock"


# User inputs
item_name = input("Enter item name: ")
starting_quantity = int(input("Enter starting quantity: "))
quantity_used = int(input("Enter quantity used: "))
quantity_received = int(input("Enter quantity received: "))

final_quantity = calculate_final_quantity(starting_quantity, quantity_used, quantity_received)
stock_status = get_stock_status(final_quantity)

print()
print("Lab Stock Assessment")
print(f"Item: {item_name}")
print(f"Starting Quantity: {starting_quantity}")
print(f"Quantity Used: {quantity_used}")
print(f"Quantity Received: {quantity_received}")
print(f"Final Quantity: {final_quantity}")
print(f"Stock Status: {stock_status}")

print(f"Helo, welcome to the program")