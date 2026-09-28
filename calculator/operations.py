#Create a package named Calculator containing single module operations.py

# in operations.py define
# add() --addition of two numbers
# sub()
# mul()
# div()

# write a program mymodule.py to import all these functions from the operations
# module and perform required operations using inputs:

def add(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    if b==0:
        print( 'error division by zero not possible')
    print(a/b)


# #Create a package named Shapes containing modules circle.py  and
# rectangle.py


#define functions to calculate the area and perimeter of  circle and rectangle.

# write a program mymodule.py to import all these functions from the circle and
# rectangle modules and perform required operations.