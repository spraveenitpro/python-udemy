def serve_tea():
    chai_type = "Masala" # Local scope
    print(f"Inside function {chai_type}")

chai_type = "lemon"
serve_tea()
print(f"Outside function: {chai_type}")

def chai_counter():
    chai_order = "lemon" # Enclosing scope
    def print_order():
        chai_order = "ginger"
        print("Inner: ", chai_order)
    print_order()
    print("Outer: ", chai_order)

chai_order = "Tulsi"
chai_counter()

print("Global: ", chai_order)