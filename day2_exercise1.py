# Sample E-commerce Inventory Database
inventory = {
    "SKU_101": {"name": "Wireless Mouse", "price": 25.00, "stock_count": 50, "category": "Electronics"},
    "SKU_102": {"name": "Gaming Keyboard", "price": 80.00, "stock_count": 0, "category": "Electronics"},
    "SKU_103": {"name": "Yoga Mat", "price": 30.00, "stock_count": 15, "category": "Fitness"},
    "SKU_104": {"name": "Bluetooth Speaker", "price": 120.00, "stock_count": 5, "category": "Electronics"},
    "SKU_105": {"name": "Protein Shaker", "price": 15.00, "stock_count": 0, "category": "Fitness"},
}

def apply_discount(inventory_data):
    for inv_item in inventory_data.values():
        if inv_item["category"] == "Electronics":
            inv_item["price"] *= 0.85  # Apply a 15% discount
            print(f"Applying discount to {inv_item['name']}, new price: {inv_item['price']}")
    return inventory_data

inventory = apply_discount(inventory)

def restock_alert(inventory_data):
    for inv_item in inventory_data.values():
        if inv_item["stock_count"] == 0:
            inv_item["restock_urgent"] = True
            print(f"Restock alert for {inv_item['name']}: stock is 0, marked as urgent.")
    return inventory_data

inventory = restock_alert(inventory)

def ensure_last_sold(inventory_data):
    for inv_item in inventory_data.values():
        if "last_sold" not in inv_item:
            inv_item.setdefault("last_sold", "Never")
            print(f"Setting last_sold for {inv_item['name']} to 'Never'.")
    return inventory_data

inventory = ensure_last_sold(inventory)

print(inventory)


# UPDATE (Flash Sale):  #    Apply a 15% discount to the 'price' of every item in the "Electronics" category.
# LOGIC (Restock Alert):  #    Loop through the inventory. If 'stock_count' is 0, add a new key  #    called 'restock_urgent' with the value True.
# SAFE ACCESS (Data Integrity):  #    Check for a 'last_sold' key. If it doesn't exist, use .setdefault()  #    to set it to "Never".
# VIEW: Print the final updated inventory.