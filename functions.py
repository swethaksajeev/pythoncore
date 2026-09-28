# #sum of 2 numbers
#
# # plain code
#
# # n1=int(input('enter n1 : '))
# # n2=int(input('enter n2 : '))
# # s=n1+n2
# # print('Sum = ',s)
#
# # def add():
# #     'addition of 2 numbers'
# #     n1=int(input('enter n1 : '))
# #     n2=int(input('enter n2 : '))
# #     s=n1+n2
# #     print('Sum = ',s)
# #
# #     return
# #
# # add()
#
#
# #define a function to display 'hello your name'
#
# def name():
#     i=input('enter your name')
#     print(i)
#     return
# name()
#
# #define a function to find the factorial of a number
#
# def fact():
#     i=1
#     f=1
#     n=int(input('enter a number : '))
#     while(i<=n):
#         f=f*i
#         i=i+1
#     print('Factorial = ',f)
#     return
# fact()
#
# #define a function to find the count of  a specific character in a given string
#
# def count_ch():
#     s=input('enter a string : ')
#     char_to_find=input('enter character :  ')
#     count=0
#     for i in s:
#         if i == char_to_find:
#             count=count+1
#     print('Count = ',count)
#     return
# count_ch()
#
#
# #define a function to check whether a number is prime or not
#
# def prime():
#     n=int(input('enter a number : '))
#     if n>1:
#         for i in range(2,n):
#             if n%i==0:
#                 print('not prime')
#                 break
#         else:
#             print('prime')
#     else:
#         print('number is either prime nor composite')
#     return
# prime()
#


#define a function to find the factors of a number

# def fact():
#     num=int(input('enter a number'))
#     for i in range(1,num+1):
#         if num%i==0:
#             print(i)
#     return
# fact()

#with arguments and parameters

# sum of two numbers

# def add(n1,n2):
#     s=n1+n2
#     print('sum = ',s)
#     return
# add(12,12)
#
# a=int(input('enter number'))
# b=int(input('enter number'))
# add(a,b)


#define a function that takes amount,year,rate as arguments and find the simple interest value(dynamic input)


# def simple_interest(p,n,r):
#     si=(p*n*r)/100
#     print('simple interest',si)
#     return
# p=int(input('enter amount'))
# n = int(input('enter year'))
# r = int(input('enter rate'))
# simple_interest(p,n,r)

#return statement
#define a funtion that takes 2 numbers as arguments and return sum as result call the function at the end of the result

# def add(n1,n2):
#     s=n1+n2
#     return s
# n1=int(input('enter n1 : '))
# n2=int(input('enter n2 : '))
# a=add(n1,n2)
# print(a)
#
#
# #define a function that takes a string as argument and return a new dictionary where keys are words and values are length of each word call the function and print the dictionary
# #inputs : s='python coding is easy and fun'
# #o/p
#
# #new={i:len(i) for i in s.split()}
#
# s='python coding is easy and fun'
# def fun(s):
#     new={}
#     for i in s.split():
#         new[i]=len(i)
#     return new
#
# a=fun(s)
# print(a)

#define a function that takes a number as argument and check whether that number is spy number or not
#spy number means 'sum of digits =product of digits'
#eg: 22 : 2+2=2*2 , 1124  : 1+1+2+4=1*1*2*4

# num=int(input('enter a number : '))
# def spy(num):
#     sum=0
#     pro=1
#     for i in str(num):
#         sum=sum+int(i)
#         pro=pro*int(i)
#     if sum==pro:
#         print('spy number')
#     else:
#         print('not a spy number')
#     return
# spy(num)

#keyword argument

# def fun(n,a):
#     print('name : ',n)
#     print('age : ',a)
# fun(n='arun',a=23)
# fun(a=23,n='arun')

#default argument

# def fun(n,a=23):
#     print('name : ',n)
#     print('age : ',a)
# fun('arun',25)
# fun('arun')

# def fun(*args):
#     print(args)
# fun(10,20 )
# fun(1,2,3,4,5)


# def fun(**kwargs):
#     print(kwargs)
# fun(a=10,b=20)
# fun(a=10,b=20,c=30)


#define a functions find the sum of numbers using arbitary argument type

#positional argument
def add(*args):
    sum=0
    for i in args:
        sum=sum+i
    return sum
print(add(10,20))
print(add(1,2,3,4,5))


#keyword argument
def add(**kwargs):
    sum=0
    for i in kwargs.values():
        sum=sum+i
    return sum
print(add(a=10,b=20))
print(add(a=1,b=2,c=3,d=4,e=5))

