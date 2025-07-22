chai = "Ginger tea"

def prepare_chai(order):
    print("Preparing", order)

# prepare_chai(chai)
# print(chai)

chai = [1,2,3]
def edit_chai(cup): #parameter
    cup[1] = 42
edit_chai(chai) #arguments
print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "yes", "low")
make_chai(tea = "Green", sugar = "medium", milk= "no")

def special_chai(*ingredients, **extras): #kwargs
    print("ingrdients", ingredients)
    print("extras", extras)

special_chai("cinnamon", "cardmom", sweetener= "honey", foam= "yes")

# def chai_order(order=[]):
#     order.append("masala")
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()