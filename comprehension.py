# #normal code
# # l=[1,2,3,4]
# # new=[]
# # for i in l:
# #     new.append(i**2)
# # print(new)
# import math
#
# #using comprehension same code for above code
#
# # l=[1,2,3,4]
# # new=[i**2 for i in l]
# # print(new)
# #
# # l=[1,2,3,4]
# # new=[i**3 for i in l]
# # print(new)
# #
# # l=[1,2,3,4]
# # new=[5 for i in l]
# # print(new)
#
# l=[23,56,34,12,89,90,24]
#
# #create a new list with even values
# #normal code
#
# new=[]
# for i in l:
#     if i%2==0:
#         new.append(i)
# print(new,end=' ')
# print()
#
# #using list comprehension same code can be written like below
#
# new=[i for i in l if i%2==0]
# print(new)
#
# #create a new list with numbers grater than 50
#
# new=[i for i in l if i>50]
# print(new)
#
#
# #create a new list of cubes
# l=[1,2,3,4]
# new=[i**3 for i in l]
# print(new)
#
# #create a new list of square roots
# l=[25,36,81,100]
# new=[i**0.5  for i in l]
# print(new)
#
# #create a new list of lengths
# colors=['red','green','blue','yellow','black']
# #create a new list of first characters
#
# length=[len(c) for c in colors ]
# new=[c[0] for c in colors]
# print(new)
#
# #create a new list of last characters
#
# new=[c[-1] for c in colors]
# print(new)
# #create a new list of reverse of each element
#
# new=[i[::-1] for i in colors]
# print(new)
#
# #print length of colors
# new=[len(i) for i in colors]
# print(new)
#
# #Given a list l=[23,78,12,56]
# #Add 10 to each element in the given sequence
#
# l=[23,78,12,56]
# new=[i+10 for i in l]
# print(new)
#
# #given a list of dictionaries
# # l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
# #    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
# #    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# #
# # create a new list of emails
#
# l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
#   {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
#   {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
#
# new=[i['email'] for i in l]
# print(new)
#
#
# # #Given a dictionary
# d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # # create a list of names
#
# new=[i for i in d]
# print(new)
# # # create a list of marks
#
# new=[i for i in d.values()]
# print(new)
#
#
# # #Given a list
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
#
# # #create a list of string values
#
# new=[i for i in l if type(i)==str]
# print(new)
#
# # #create a list of floats
#
# new=[i for i in l if type(i)==float]
# print(new)
# # #create a list of positive numbers
#
# l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
# new=[i for i in l if type(i)!=str and i>0]
# print(new)
#
#
# #
# # #Given a list
# fruits=['apple','orange','pineapple','avocado','grapes']
# # #create a new list with elements whose length is greater than 6
#
# new=[i for i in fruits if len(i)>6]
# print(new)
#
# # #create a new list with elements whose value is divisible by 3 in range(1,101)
#
# new=[i for i in range(1,101) if i%3==0]
# print(new)
# # Given
# s="python coding  is easy and fun"
# # # create a new list with only vowels
#
# vowels='aeiouAEIOU'
# new=[i for i in s if i in vowels]
# print(new)

#set

# s="python coding  is easy and fun"
# new={i for i in s if i in 'aeiouAEIOU'}
# print(new)

#dictionary

#crate a new dictionary where keys are numbers and values are squares of each number

# l=[1,2,3,4]
# new={i:i**2 for i in l}
# print(new)

#normal code for above code

# l=[1,2,3,4]
# new={}
# for i in l:
#     new[i]=i**2
# print(new)

#given a list
# l=[10,20,30,40]
#  0   1  2  3
#create a new dictionary where keys are the indexes and values are numbers
#o/p {0:10,1:20,2:30,3:30}

# l=[10,20,30,40]
# new={i:l[i] for i in range(0,len(l))}
# print(new)

# to iterate in charaters
# s='hello world'
# for i in s:
#     print(i,end=' ')
# print()

# to iterate in words
# s='hello world'
# for i in s.split():
#     print(i,end=' ')
# print()

#given a string
# s='python coding is easy and fun'
# create a new dictionary where keys are words and values are the length of each word
#o/p {'python': 6, 'coding': 6, 'is': 2, 'easy': 4, 'and': 3, 'fun': 3}

#s='python coding is easy and fun'
# new={i:len(i) for i in s.split()}
# print(new)