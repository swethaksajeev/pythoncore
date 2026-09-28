# Q.Write Python Programs Using map(), filter(), or reduce()

# 1.Capitalize all names in a list
names = ['alin', 'arun', 'anu']
c_name=list(map(lambda name: name.capitalize(),names))
print(c_name)

# 2.Append "@gmail.com" to a list of usernames
users = ['user1', 'user2']
result=list(map(lambda name: name + "@gmail.com",users))
print(result)

# 3.Filter out all empty strings from a list
words = ['hello', ' ', 'world', ' ', 'python']
result=list(filter(lambda string: string !=" ",words))
print(result)

# 4.Filter names that start with the letter 'A'
names = ['Anu', 'Neenu', 'Arun', 'Ravi']
result=list(filter(lambda name: name[0]=='A',names))
print(result)

# 5.Concatenate all strings in a list
words = ['Python', 'is', 'fun']
import functools
result=functools.reduce(lambda a,b:a+' '+b,words)
print(result)

# 6.Multiply all numbers in a list
nums = [2, 3, 4]
import functools
result=functools.reduce(lambda a,b:a*b,nums)
print(result)

# 7.Extract First Character of Each Word
words = ["apple", "banana", "cherry"]
result=list(map(lambda word: word[0],words))
print(result)
# 8.Add 10 to Each Number
nums = [5, 10, 15]
result=list(map(lambda num: num + 10,nums))
print(result)

# 9.Given a list
l=[12,-4,78,-34,90,45,16,26,-2,-11,3]
 #Sum of positive even numbers
import functools
positive=list(filter(lambda num: num>0 and num%2==0,l))
result=functools.reduce(lambda a,b:a+b,positive)
print(result)

# #Sum of Positive Odd numbers

import functools
positive_odd=list(filter(lambda num: num>0 and num%2!=0,l))
result=functools.reduce(lambda a,b:a+b,positive_odd)
print(result)

# #Sum of Negative  odd numbers

import functools
num=list(filter(lambda num: num<0 and num%2!=0,l))
result=functools.reduce(lambda a,b:a+b,num)
print(result)

# #Sum of Negative Even numbers

import functools
num=list(filter(lambda num: num<0 and num%2==0,l))
result=functools.reduce(lambda a,b:a+b,num)
print(result)

# #Count of Positive numbers


n=list(filter(lambda num: num>0 ,l))
result=len(n)
print(result)

# #Count of negative numbers
n=list(filter(lambda num: num<0 ,l))
result=len(n)
print(result)

# 10.Given a list
nums = ["1", "2", "3", "4"]
# Convert all Strings to Integers [1,2,3,4]
result=list(map(lambda num: int(num),nums))
print(result)

# 11.
p= [{'name':'laptop','price':50000},
    {'name':'phone','price':20000},
    {'name':'watch','price':3000},
    {'name':'Tablet','price':25000}]

#print list of product names in Uppercase

result=list(map(lambda n:n['name'].upper(),p))   #n.get('names')
print(result)

#print products with price greater than 10000
n=list(filter(lambda item: item['price'] >10000 ,p))
print(n)

#Find the total price of all products
price=list(map(lambda l:l['price'],p))
total=functools.reduce(lambda a,b:a+b,price)
print(total)

#or

t=functools.reduce(lambda a,b:a+b['price'],p,0)
print(t)