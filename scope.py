#global
#example
# x=20   #global can be used every where in the program
# print('outside function : ',x)
#
# def f():
#     print('inside function : ',x)  #x can be accessed in in where of program
# f()

#local

# def f():
#     x=20
#     print('inside function',x)
# f()
# print('outside function',x)  #error because x is defined inside the function so we cannot use it outside the function

#example

# def f():
#     global x  #used to change the local scope into global
#     x=20
#     print('inside function',x)
#
#
# def g():
#     y=20
#     print(x)
#     print('inside function',y)
#
# f()
# g()

#non local

def outer():
    x=20 #non local
    print('outer',x)
    def inner():
        y=30   #locaL
        print('inner',x)
        return
    inner()
outer()

