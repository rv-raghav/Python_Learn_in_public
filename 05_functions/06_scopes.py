# Scopes and Name resolutions
# Local - inside a function
# enclosing - from outer function if nested
# global - top level script
# built in

def serve_chai():
    chai_type = "Masala" # local scope
    print(f"inside function {chai_type}")

chai_type = "lemon"
serve_chai()
print(f"outside function: {chai_type}")


def chai_counter():
    chai_order = "lemon" # enclosing scope

    def print_order():
        chai_order = "ginger"
        print("Inner", chai_order)
    print_order()
    print("outer", chai_order)

chai_order = "tulsi" # global scope
chai_counter()
print("global:", chai_order)