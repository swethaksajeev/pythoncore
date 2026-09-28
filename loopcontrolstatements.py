# # #normal code
# # s='hello'
# # for i in s:
# #     print(i,end=' ')
# # print()
# #
# # #using break
# #
# # for i in s:
# #     if i=='l':
# #         break
# #     print(i,end=' ')
# # print()
# #

# # #using continue
# #
# # for i in s:
# #     if i=='l':
# #         continue
# #     print(i,end=' ')
# # print()
#
# #1.given a list of numbers
# l=[25,67,34,78,17,44,82]
# #print all the numbers
#
# for i in l:
#     print(i,end=" ")
# print()
#
# #stops the loop when i>50
# for i in l:
#     if i>50:
#         break
#     print(i,end=' ')
# print()
#
# #skip all even numbers
#
# for i in l:
#     if i%2==0:
#         continue
#     print(i,end=' ')
# print()
#
# #2. given a list of colors
# colors=['red','green','yellow','blue','orange','black']
#
# #print all colors
#
# for i in colors:
#     print(i,end=' ')
# print()
# #print those colors starting with 'b'
#
# for i in colors:
#     if i[0]=='b':
#         print(i,end=' ')
# print()
# #print the first color starting with 'b'
#
# for i in colors:
#     if i[0]=="b":
#         print(i,end=' ')
#         break
# print()
# #skip all colors starting with 'b'
#
# for i in colors:
#     if i[0]=='b':
#         continue
#     print(i,end=' ')
# print()
#
# #3.given
# s='python coding is easy and fun'
# #print all characters upto specific character(including that character)
#
# char=input('enter a character : ')
# for i in s:
#      print(i,end=' ')
#      if i == char:
#         break
# print()

#write a program to check whether a number is armstrong number

# sum=0
# num=int(input('enter a number : '))
# s=str(num)
# l=len(s)
# for i in s:
#     sum=sum+int(i)**l
# if sum==num:
#     print(num,' is armstrong')
# else:
#     print('not armstrong')

#print factors of a number

# num=int(input('enter a number : '))
# for i in range(1,num+1,1):
#     if num%i==0:
#         print(i,end=' ')
# print()

#for else statement

# for i in range(1,6,1):
#     print(i)
# else:   #it works only after the normal execution loop
#     print('hello')

#check whether a number is prime or not

# num=int(input('enter a number : '))
# if(num>1):
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, 'is not prime')
#             break
#     else:
#         print(num, 'is prime')
# else:
#     print('number is neither prime nor composite ')
#

# NESTED LOOP

# l=[10,20,30]
# for i in l:
#     for j in range(1,4):
#         print(i,end=' ')
#     print()

#PATTERN PRINTING

# for i in range(1,4,1):
#     for j in range(1,4):
#         print(i,end=' ')
#     print(i)
#

# for i in range(1,4):
#     for j in range(1,5):
#         print(j,end=' ')
#     print()


# for i in range(1,5):
#     for j in range(1,5):
#         print('*',end=' ')
#     print()


# l=[['lion','tiger'],['cat','elephant']]
# for i in l:
#     print(i,end=' ')
#     for j in i:
#         print(j,end=' ')
#     print()

# #1.given list
# names=['kelly','alan','jeny']
# #print
# #kelly kelly kelly
# #alan alan alan
# #jeny jeny jeny
#
# for i in names:
#     for j in range(1,4):
#         print(i,end=' ')
#     print()
#
#
# #2.given list
# # n=[1,2,3]
# # q=['what','when','why']
#
# # print
# # 1
# # what when why
# # 2
# # whatwhen why
# # 3
# # what when why
#
# n=[1,2,3]
# q=['what','when','why']
#
# for i in n:
#     print(i)
#     for j in q:
#         print(j,end=' ')
#     print()
#
#
#
# #3.given a list
#
# # d=[{'id':101,'name':'arun','age':23},{'id':102,'name':'amal','age':24}
# #    {'id':103,'name':'anu','age':25}]
# #print each student details
# #id name age
#
# d=[{'id':101,'name':'arun','age':23},{'id':102,'name':'amal','age':24},
#     {'id':103,'name':'anu','age':25}]
# for i in d:
#     for j in i.values():
#         print(j,end=' ')
#     print()
#
# #next ques
# d={'id':101,'name':'arun','age':23}
# for i,j in d.items():
#     print(i,j)
#
# #next ques
# d=[{'id':101,'name':'arun','age':23},{'id':102,'name':'amal','age':24},
#     {'id':103,'name':'anu','age':25}]
# for i in d:
#      for k,j in i.items():
#          print(k,j,end=' ')
#      print()
#
# #pattern
#
# # for i in range(1,5):
# #     for j in range(1,i+1):
# #         print('*',end=' ')
# #     print()
#
# # *
# # * * *
# # * * * * *
# # * * * * * * *
#
# for i in range(1,8,2):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()
#
# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(i,end=' ')
#     print()
#
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
#
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(j,end=' ')
#     print()
#
#
# for i in range(4,0,-1):
#     for j in range(i):
#         print('*',end=' ')
#     print()

#print all prime numbers
#
# l=[23,45,78,90,12,13,91]
# for i in l:
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

#find all prime numbers in the range (1,100)

# for i in range(2,101):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i,end=' ')
# print()

#find all armstrong numbers in the range (100,1000)


# for i in range(100,1001):
#     s = str(i)
#     l = len(s)
#     sum = 0
#     for j in s:
#         sum=sum+int(j)**l
#     if sum==i:
#         print(i,end=' ')
# print()

#eg

# for i in range(1,5):
#     for j in range(1,6):
#         print(j,end=' ')
#     print()

#eg

# for i in range(4,0,-1):
#     for j in range(1,i+1):
#         print('*',end=' ')
#     print()


# k=1
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(k,end=' ')
#         k=k+1
#     print()

# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=' ')
#         k=k+1
#     print()



# A
# B B
# C C C
# D D D D

# k=ord('A')
# for i in range(1,5):
#     for j in range(1,i+1):
#         print(chr(k),end=' ')
#     k=k+1
#     print()


# A
# A B
# A B C
# A B C D

# for i in range(1,5):
#     k = ord('A')
#     for j in range(1,i+1):
#         print(chr(k),end=' ')
#         k=k+1
#     print()

# for i in range(1,5):
#     for j in range(1,5):
#         print(i,end=' ')
#     print()

# 1 0 0 0
# 0 2 0 0
# 0 0 3 0
# 0 0 0 4

# for i in range(1,5):
#     for j in range(1,5):
#         if i==j:
#             print(i,end=' ')
#         else:
#             print(0,end=' ')
#     print()

# 1
# 1 0
# 1 0 1
# 1 0 1 0

# for i in range(1,5):
#     for j in range(1,i+1):
#         if(j%2!=0):
#             print(1,end=' ')
#         else:
#             print(0,end=' ')
#     print()


# 0
# 0 1
# 0 1 2
# 0 1 2 3
# 0 1 2 3 4

# for i in range(0,5):
#     for j in range(0,i+1):
#         print(j,end=' ')
#     print()


# h
# h e
# h e l
# h e l l
# h e l l o
# h e l l o
# h e l l o   w
# h e l l o   w o
# h e l l o   w o r
# h e l l o   w o r l
# h e l l o   w o r l d

# s='hello world'
# for i in range(len(s)):
#     for j in range(i+1):
#         print(s[j],end=' ')
#     print()


#       *
#     * *
#   * * *
# * * * *

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):  #for printing space in each line
#         print(end=' ')
#     for j in range(1,i+1): #for printing stars in each line
#         print('*',end=' ')
#     k=k-2
#     print()


#       *
#     *   *
#   *   *   *
# *   *   *   *


# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):  #for printing space in each line
#         print(end=' ')
#     for j in range(1,i+1): #for printing stars in each line
#         print('*',end='   ')
#     k=k-2
#     print()


#       *
#     * *
#   * * *
# * * * *
#   * * *
#     * *
#       *


# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=' ')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     k=k-2
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=' ')
#     for j in range(1,i+1):
#         print('*',end=' ')
#     k=k+2
#     print()

#       *
#     *   *
#   *   *   *
# *   *   *   *
#   *   *   *
#     *   *
#       *

# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=' ')
#     for j in range(1,i+1):
#         print('*',end='   ')
#     k=k-2
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=' ')
#     for j in range(1,i+1):
#         print('*',end='   ')
#     k=k+2
#     print()


#       1
#     1   2
#   1   2   3
# 1   2   3   4
#   1   2   3
#     1   2
#       1


# k=3*2
# for i in range(1,5):
#     for p in range(1,k+1):
#         print(end=' ')
#     for j in range(1,i+1):
#         print(j,end='   ')
#     k=k-2
#     print()
# k=2
# for i in range(3,0,-1):
#     for p in range(1,k+1):
#         print(end=' ')
#     for j in range(1,i+1):
#         print(j,end='   ')
#     k=k+2
#     print()

