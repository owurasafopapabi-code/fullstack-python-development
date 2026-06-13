item = input("Enter lab item: ")
starting_quantity = int(input("Enter starting quantity: "))
quantity_used = int(input("Enter quantity used: "))
quantity_received_today = int(input("Enter quantity received today: "))

final_quantity = starting_quantity - quantity_used + quantity_received_today

print()
print("Inventory Summary")
print(f"Item: {item}")
print(f"Starting Quantity: {starting_quantity}")
print(f"Used Quantity: {quantity_used}")
print(f"Received Today: {quantity_received_today}")
print(f"Final Quantity: {final_quantity}")