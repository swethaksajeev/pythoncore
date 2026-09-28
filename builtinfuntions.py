# # import math
# # print(math.sqrt(81))
# # print(math.ceil(8.6))
# # print(math.floor(8.6))
# # print(math.factorial(5))
# # print(math.lcm(3,2,6))
# # print(math.gcd(3,2,6))
# #
# # s='helloworld'
# # print(s.split())
# # print(s.index('l'))
# # print(s.find('l'))
# # print(s.count('h'))
# # print(s.strip('h'))
# # print(s.lower())
# # print(s.upper())
# # print(s.capitalize())
# #
# # print(s.isalpha())
# # print(s.replace('world','python'))
#
#
# #Write a program to create a list of 5 random 3digit numbers
#
#
#
# # #Write a program to create a list of 5 random 3digit numbers
# #
# # import random
# # from itertools import count
# #
# # new=[]
# # for i in range(1,6):
# #     n=random.randint(100,999)
# #     new.append(n)
# # print(new)
# #
# #
# # #write a program to create a 5digit random otp number
# #
# # import random
# # new=[]
# # n=random.randint(10000,99999)
# # print("5 digit random OTP number :",n)
# #
# #
# # #write a program to find the position of a character in a string
# #
# # s='welcome to python programming'
# #ch=intput('char to find')
# #if ch in s:
# # position=s.index("p")
# #
# # pos=s.find("p")
# #
# # print(position)
# #
# # print(pos)
# #else:
# # print('ch not in s')
# #
# # #define a function that takes a string as argument and returns a new dictionary where keys are character and values are count of each character
# #
# # def new_dict(s):
# #     new={}
# #     for i in s:
# #         new[i]=s.count(i)
# #     return new
# #
# # s=input('enter a string :')
# # new_dict(s)
# #
# #
# #
#
# #Define a function that takes string as argument and print the count of digits,spaces,letters in that string
#
#
# def new_dict(s):
#
#     d_count=0
#     a_count=0
#     s_count=0
#
#     for i in s:
#         if i.isdigit():
#             d_count=d_count+1
#
#         elif i.isalpha():
#             a_count=a_count+1
#
#         elif i.isspace():
#             s_count=s_count+1
#
#     print("digit count :",d_count)
#     print("alphabet count :",a_count)
#     print("space count :",s_count)
#
# s=input('enter a string :')
# new_dict(s)


# l=[1,2,3,4]
# l.append(5)
# print(l)
# l.extend((6,7,8))
# print(l)
#
# l=[23,78,45,37,92]
# l.sort()
# print(l)
# l.reverse()
# print(l)
# l.pop()
# print(l)
# l.pop(1)
# print(l)
#
# l=[10,20,30,40,50,60]
# l.insert(2,70)
# print(l)
#
# l.remove(40)
# print(l)
#
# l.copy()
# print(l)


#given a list l=[1,2,2,3,4,4,5,6]
#create a new dictionary where keys are numbers and values are number of occurence of each number.
#
# l=[1,2,2,3,4,4,5,6]
# new={}
# count=0
# for i in l:
#     new[i]=l.count(i)
# print(new)
#
#
# #given a list l=[11,34,78,23,90,65]
# #find the largest number
# l=[11,34,78,23,90,65]
# maximum=max(l)
# print('max number is: ',maximum)
#
# #find the second largest number
#
# l.sort()
# print(l)
# print('second largest number is : ',l[-2])
#
#
# #find the smallest number
# minimum=min(l)
# print('smallest number is : ',minimum)
# #find the second smallest number max(l) min(l)
#
# second=l[1]
# print('second smallest number : ',second)
#
# # 3.given a list
# # l=[['arun',23,30000],['amal',25,'50000'],['anu',27,40000]]
# # find the maximum salary
# #find min age
#
# l=[['arun',23,30000],['amal',25,50000],['anu',27,40000]]
# new=[]
# for i in l:
#     new.append(i[-1])
# print(max(new))
#
# new=[]
# for i in l:
#     new.append(i[-2])
# print(min(new))

#given a list
#l=[23,45,67,12,90,78]
#find the largest and smallest number without using built in method

# l=[23,45,67,12,90,78]
# max=l[0]
# for i in l:
#     if i>max:
#         max=i
# print('maximum = ',max)
#
#
# min=l[0]
# for i in l:
#     if i<min:
#         min=i
# print('minimum = ',min)

#set

# s={1,2,3,4,5}
#
# s.add(6)
# print(s)
#
# s.update((6,7,8,9))  #duplicate 6 will not be printed
# print(s)
#
# s.pop()
# print(s)
#
# s.remove(2)
# print(s)
#
# s.discard(6)
# print(s)
#
# s={1,2,3}
# t={3,4,5}
# u=s.union(t)
# print(u)
# l=s.intersection(t)
# print(l)
# o=s.difference(t)
# print(o)
# e=s.symmetric_difference(t)
# print(e)


#1.given a list
# l=[1,1,2,3,3,4]
# #remove duplicates
#
# s=set(l)
# print(s)

#2.given a list
#remove duplicates without using set() order should be preserved

# l=[1,1,2,3,3,4]
# new=[]
# for i in l:
#     if i not in new:
#         new.append(i)
# print(new)
#
# #3.given a list
# l1=[13,27,30,42,57]
# l2=[13,57,89,33,80]
# #find common elements
# s=set(l1)
# t=set(l2)
# u=s.intersection(t)
#
# print(list(u))


#Dictionary

# d={'name':'arun','age':23}
# print(d.keys())
# d['course']='python'
# print(d)
# print(d.get('age'))
# print(d.items())
# print(d.popitem())
# print(d.pop('age'))
# print(d)

#lambda function

#define a afunction that takes a number as a argument and returns its square call the function and print the result

#normal user defined function

# def square(n):
#     s=n**n
#     return s
# a=square(5)
# print(a)

#using lambda

# a=lambda n:n**n
# print(a(5))

#sum of 2 numbers
# s=lambda a,b:a+b
# print(s(2,3))
# #product of 3 numbers
#
# s=lambda x,b,c:x*b*c
# print(s(3,4,5))
#
# #cube of a number
#
# s=lambda e:e*e*e
# print('cube',s(2))
#
# #first letter of a string
#
# a=lambda s:s[0]
# print(a('hello'))
# #length of a string
#
# a=lambda s:len(s)
# print(a('hello'))
# #reverse of a string
#
# a=lambda s:s[::-1]
# print('rev' ,a('hello'))
# #name value from a dictionary
#
# a=lambda d:d['name']
# print(a({'name':'arun'}))
#
# #second element from the list
#
# a=lambda s:s[1]
# print(a([1,2,3]))
#
# #add 10 to a number
#
# s=lambda a:a+10
# print(a(5))



