def calculate_final_quantity(starting_quantity, quantity_used, quantity_received):
    return starting_quantity - quantity_used + quantity_received

item_name = input("Enter item name: ")
starting_quantity = int(input("Enter starting quantity: "))
quantity_used = int(input("Enter quantity used: "))
quantity_received = int(input("Enter quantity received: "))

final_quantity = calculate_final_quantity(starting_quantity, quantity_used, quantity_received)

print()
print("Inventory Summary")
print(f"Item: {item_name}")
print(f"Starting Quantity: {starting_quantity}")
print(f"Used Quantity: {quantity_used}")
print(f"Received Quantity: {quantity_received}")
print(f"Final Quantity: {final_quantity}")
