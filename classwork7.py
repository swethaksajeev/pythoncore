# # # Q1.Define a function that takes 2 numbers and returns their product

# def fun(n1,n2):
#     s=n1*n2
#     return s
# n1=int(input('enter n1'))
# n2=int(input('enter n2'))
# a=fun(n1,n2)
# print(a)

# Q2.Define a function that takes a string and returns number of vowels

# def function_str(s):
#     vowels='aeiouAEIOU'
#     count=0
#     for i in s:
#         if i in vowels:
#             count=count+1
#     print(count)
#     return
# s=input('enter string : ')
# function_str(s)


# Q3.Define a function that takes length and breadth and returns area of
# #rectangle

# def rect(l,b):
#     area=l*b
#     print(area)
#     return
# l=int(input('enter length'))
# b=int(input('enter breadth'))
# rect(l,b)

# # Q4.Define a function that takes a list of numbers and creates a new list
# # with even numbers and returns the new list
# l=[45,78,90,12,35]

# l = [45, 78, 90, 12, 35]
# def list_num(l):
#
#     new=[]
#     for i in l:
#         if i%2==0:
#             new.append(i)
#     print(new)
#     return
# list_num(l)


# #Q5.Define a function that takes list of 3digit numbers and returns a new list where
# # each value is the sum of digits of corresponding number in the original list.

# l = [123, 345, 111, 678, 134, 809]
#
# def list_num(l):
#
#     new=[]
#     for i in l:
#         sum=0
#         for j in str(i):
#             sum=int(j)+sum
#         new.append(sum)
#
#     print(new)
#     return
# list_num(l)

#Q6.Define a function that takes a list and returns a new list containing unique elements from the given
# list
# l=[12,34,78,12,67,34,90,23]
#
# def list_rep(l):
#     new=[]
#     for i in l:
#         if i not in new:
#             new.append(i)
#     print(new)
#     return
# list_rep(l)


#Q7.Define a function that takes 2 list as arguments and returns a new list containing common elements

# list1=[12,34,56,78,90]
# list2=[90,34,11,57,45]
# def list_common(list1,list2):
#     new=[]
#     for i in list1:
#         if i in list2:
#             new.append(i)
#     print(new)
#     return
# list_common(list1,list2)


# l1=[12,34,56,78,90]
# l2=[90,89,12,56,34]
# def lis(l1,l2):
#     new=[]
#     for i in l1:
#         if i in l2:
#             new.append(i)
#     print(new)
#     return
# lis(l1,l2)


#define a function that takes a string as argument and return a new dictionary where keys are words and values are length of each word call the function and print the dictionary
#inputs : s='python coding is easy and fun'
#o/p

#new={i:len(i) for i in s.split()}

s='python coding is easy and fun'
def fun(s):
    new={}
    for i in s.split():
        new[i]=len(i)
    return new

a=fun(s)
print(a)


































