from models.delivery_types import Express_Delivery, Standard_Delivery
orders = [
    Express_Delivery("laptop", 50),
    Standard_Delivery("Book", 50),
    Express_Delivery("Mobile", 30),

]

print("--- NexusLogistics Shipping Summary ---")

for i in orders :
    cost = i.calculate_shipping()
    print(f'item : {i.item_name} | ID : {i.tracking_id} | Cost : &{cost}')

# --- Testing Encapsulation ---
print(orders[0].__tracking_id) # Uncommenting this should give an ERROR