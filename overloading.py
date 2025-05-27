class ShoppingCart:
    def __init__(self):
        self.items = []
        self.total = 0
    
    def add_item(self, product_name, price=0, quantity=1, discount=0):
        
        final_price = price * (1 - discount/100)
        total_cost = final_price * quantity
        
        item = {
            'name': product_name,
            'price': price,
            'quantity': quantity,
            'discount': discount,
            'total_cost': total_cost
        }
        self.items.append(item)
        self.total += total_cost
        
        if discount > 0:
            return f"Added {quantity}x {product_name} at ${price:.2f} each (${discount}% off) = ${total_cost:.2f}"
        else:
            return f"Added {quantity}x {product_name} at ${price:.2f} each = ${total_cost:.2f}"
    
    def show_cart(self):
        print("SHOPPING CART")
        for item in self.items:
            print(f"- {item['quantity']}x {item['name']}: ${item['total_cost']:.2f}")
        print(f"TOTAL: ${self.total:.2f}")
        print()

cart = ShoppingCart()

print("1. CALLING: add_item('Banana')")
print("   Result:", cart.add_item("Banana"))
print("   → Only product name provided, others use default values\n")

print("2. CALLING: add_item('Apple', 1.50)")
print("   Result:", cart.add_item("Apple", 1.50))
print("   → Product name + price provided\n")

print("3. CALLING: add_item('Orange', 2.00, 3)")
print("   Result:", cart.add_item("Orange", 2.00, 3))
print("   → Product name + price + quantity provided\n")

print("4. CALLING: add_item('Milk', 4.99, 2, 15)")
print("   Result:", cart.add_item("Milk", 4.99, 2, 15))
print("   → All parameters provided (with 15% discount)\n")

cart.show_cart()
