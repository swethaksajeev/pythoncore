#while

#1,2,3,4,5,6,7,8,9,10

# i=1
# while(i<=10):
#     print(i)
#     i=i+1

#1,3,5,7,9,11
#
# i=1
# while(i<=11):
#     print(i)
#     i=i+2

#2,4,6,8,10

# i=2
# while(i<=10):
#     print(i)
#     i=i+2

#1,4,9,16,25

# i=1
# while(i<=5):
#     print(i**2)
#     i=i+1

#5,4,3,2,1

# i=5
# while(i>=1):
#     print(i)
#     i=i-1

#while


# # #1,2,3,4,5,.....100
# i=1
# while(i<=100):
#     print(i)
#     i=i+1

# # #1,3,5,7,9,11,13,15

# i=1
# while(i<=15):
#     print(i)
#     i=i+2

# #2,4,6,8,10,12
#
# i=2
# while(i<=12):
#     print(i)
#     i=i+2

# #1,4,7,10,13,16
#
# i=1
# while(i<=16):
#     print(i)
#     i=i+3


#10,20,30,40,50,60,70,80

# i=10
# while(i<=80):
#     print(i,end='')
#     i=i+10
#
#
# #3,6,9,12,15,18,21
#
# i=3
# while(i<=21):
#     print(i)
#     i=i+3
#
# #5,4,3,2,1
#
# i=5
# while(i>=1):
#     print(i)
#     i=i-1
#
# #8,6,4,2,0
#
# i=8
# while(i>=0):
#     print(i)
#     i=i-2
#
# #100,101,102,.....200
#
# i=100
# while(i<=200):
#     print(i)
#     i=i+1
#
# #print all 4 digit numbers(1000-9999)
#
# i=1000
# while(i<=9999):
#     print(i,end=" ")
#     i=i+1
# print()

#print those number are divisible by 3 in the range(1,50)
#
# i=1
# while(i<=50):
#     if(i%3==0):
#         print(i,end=" ")
#     i=i+1
# print()
#
# #print those 3 digit numbers that are divisible by 5 and 7
#
# i=100
# while(i<=999):
#     if(i%5==0 and i%7==0):
#         print(i,end=" ")
#     i=i+1
# print()
#
# #print those numbers in the range(100,200) which contains digit '3'
#
# i=100
# while(i<=200):
#     if "3" in str(i):
#         print(i,end=" ")
#     i=i+1
# print()
#
# #count those number are divisible by 3 in the range(1,50)
#
# count=0
# i=1
# while(i<=50):
#     if(i%3==0):
#         # print(i,end=" ")
#         count=count+1
#     i=i+1
# print('count is : ',count)
# print()

#print count those numbers in the range(100,200) which contains digit '3'

# count=0
# i=100
# while(i<=200):
#     if "3" in str(i):
#         # print(i,end=" ")
#         count=count+1
#     i=i+1
# print('count is : ',count)

#print sum of series 1,2,3,4,5

# sum=0
# i=1
# while(i<=5):
#     sum=sum+i
#     i=i+1
# print('sum is ',sum)

#print product of series 1,2,3,4,5

# product=1
# i=1
# while(i<=5):
#     product=product*i
#     i=i+1
# print('product is = ', product)

#print sum of first 10 even numbers

# sum=0
# i=2
# while(i<=20):
#     sum=sum+i
#     i=i+2
# print('sum = ',sum)

#print product of first 10 even numbers

# pro=1
# i=2
# while(i<=20):
#     pro=pro*i
#     i=i+2
# print('product = ', pro)

#print series 4,9,14,19,29,34,39

# i=4
# while(i<=39):
#     print(i,end=' ')
#     i=i+5
# print()

#print sum of series 1,3,5,7,9,11

# i=1
# sum=0
# while(i<=11):
#     sum=sum+i
#     i=i+2
# print('sum is ',sum)
# print()

#product of numbers that are divisible by 3 and 5 in the range (1,50)

# i=1
# pro=1
# while(i<=50):
#     if(i%3==0 and i%5==0):
#         pro=pro*i
#     i=i+1
# print('product is : ',pro)
# print()

#count of 3 digit number that are divisible by 7

# i=100
# count=0
# while (i<=999):
#     if(i%7==0):
#         count=count+1
#     i=i+1
# print('count is :',count)

#print factorial of a number

# i=1
# fact=1
# n=int(input('enter a number : '))
# while(i<=n):
#     fact=fact*i
#     i=i+1
# print('Factorial of the number is = ',fact)

#multiplication table of a number

n=int(input('enter a number : '))
i=1
while(i<=10):
    print(n,'*',i,'=',n*i)
    i=i+1