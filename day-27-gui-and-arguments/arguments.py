#Unlimited positional arguments into a function
def add(*args):
    print(sum(args))
    return True

add(2,5,6,20,34,3)

#Keyword Arguments **kwargs
def calculate(n,**kwargs):
    print(type(kwargs)) # A dictionary

    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2,add=3, multiply=5)