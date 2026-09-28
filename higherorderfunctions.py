# # #MAP
# #
# # l=[1,2,3,4]
# # #create a list of squares
# #
# # print(list(map(lambda x:x**2,l)))
# # print(tuple(map(lambda x:x**2,l)))
# # print(set(map(lambda x:x**2,l)))
#
# #create a new list of cubes
# l=[1,2,3,4]
# print(list(map(lambda x:x**3,l)))
#
#
# #create a new list of square roots #x**0.5
# l=[25,36,81,100]
# print(list(map(lambda x:x**0.5,l)))
#
# #create a new list of lengths
# colors=['red','green','blue','yellow','black']
# #create a new list of first characters
#
# print(list(map(lambda x:x[0],colors)))
#
# #create a new list of last characters
#
# print(list(map(lambda x:x[-1],colors)))
#
# #create a new list of reverse of each element
#
# print(list(map(lambda x:x[::-1],colors)))
#
# #Given a list
# l=[23,78,12,56]
# #Add 10 to each element in the given sequence
#
# print(list(map(lambda x:x+10,l)))
#
# ##given a list of dictionaries
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#     {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # # create a new list of emails
#
# print(list(map(lambda x:x['email'],l)))

l=[1,2,3,4,5,6,7,8,9,10]
print(list(map(lambda x:x%2==0,l)))

#FILTER

l=[1,2,3,4,5,6,7,8,9,10]
print(list(filter(lambda x:x%2==0,l)))

#given a list
l=[23,45,67,12,89,78]
#filter even values greater than 50

print(list(filter(lambda x:x>50,l)))

#given a list
colors=['red','green','blue','yellow','orange']
#filter the color whose length is greater than 5

print(list(filter(lambda x:len(x)>5,colors)))

#filter the color containing letter 'n'

print(list(filter(lambda x:'n' in x,colors)))

#reduce

#given a list

l=[1,2,3,4]
#sum of list using reduce()

import functools
print(functools.reduce(lambda x,y:x+y,0,1))
