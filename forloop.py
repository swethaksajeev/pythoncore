# # s='hello'
# # for i in s:
# #     print(i)
#
# # l=['red','green','blue']
# # for i in l:
# #     print(i)
#
# # s={1,2,3,4}
# # for i in s:
# #     print(i)
#
# # d={'a':10,'b':20,'c':30}
# # for i in d:
# #     print(i)
#
# # d={'a':10,'b':20,'c':30}
# # for i in d.values():
# #     print(i)
#
# #print each number in a list
# #
# # l=[12,34,56,45,89,16,69,33]
# # for i in l:
# #     print(i)
# #
# #print even numbers
#
#
# # l=[12,34,56,45,89,16,69,33]
# # for i in l:
# #     if i%2==0:
# #         print(i)
#
# #print those numbers that are divisible by 5
#
# #
# # l=[12,34,56,45,89,16,69,33]
# # for i in l:
# #     if i%5==0:
# #         print(i)
#
# #print those numbers that contain digit 3
#
# # l=[12,34,56,45,89,16,69,33]
# # for i in l:
# #     if '3' in str(i):
# #         print(i)
#
# # s='hello world'
# #print each character
#
# # for i in s:
# #     print(i)
#
# #print those characters that are not vowel
# # vowels='aeiouAEIOU'
# # for i in s:
# #     if i not in vowels:
# #         print(i,end=' ')
# # print()
#
#
# # Given a dictionary
# # d={'n1':23,'n2':46,'n3':89,'n4':24}
# # print each value
#
# # for i in d.values():
# #     print(i)
#
# # print odd values
#
# # for i in d.values():
# #     if i%2!=0:
# #         print(i)
#
#
# # Given a list
# l=["red",'green','orange','blue','black','yellow']
# # print each color
# for i in l:
#     print(i,end=' ')
# print()
# # print color starting with 'b'
#
# for i in l:
#     if i[0]=='b':
#         print(i,end=' ')
# print()
# # print color whose length is greater than 5
#
# for i in l:
#     if len(i)>5:
#         print(i,end=' ')
# print()
# #
# #
# # Given a list
# l=[10,'arun','amal',35,3.6,6.9,89]
# # print  string values
# for i in l:
#     if type(i)==str:
#         print(i,end=' ')
# print()
# # print float values
#
# for i in l:
#     if type(i)==float:
#         print(i,end=' ')
# print()

#


# #sum of list
# sum=0
# for i in l:
#     sum=sum+i
# print(sum)
#
# #product of even values
# pro=1
# for i in l:
#     if i%2==0:
#         pro=pro*i
# print(pro)
#
# #count of odd values
#
# count=0
# for i in l:
#     if i%2!=0:
#         count=count+1
# print(count)
#
# for i in range(1,10,2):
#     print(i,end=' ')
# print()
#
# for i in range(2,11,2):
#     print(i,end=' ')
# print()
#
# for i in range(1,6,1):
#     print(i**2,end=' ')
# print()
#
# for i in range(4,40,5):
#     print(i,end=' ')
# print()
#
# for i in range(5,0,-1):
#     print(i,end=' ')
# print()
#
# for i in range(8,-1,-2):
#     print(i,end=' ')
# print()
#
# for i in range(7,43,7):
#     print(i,end=" ")
# print()
#
# for i in range(2,52,2):
#     print(i,end=' ')
# print()
#
# for i in range(3,31,3):
#     print(i,end=' ')
# print()

for i in range(100,1001,100):
    print(i,end=" ")
print()

for i in range(1,6,1):
    print(i**3,end=" ")
print()

#find all 3 digit numbers that are divisible by 3

for i in range(100,1000,1):
    if(i%3==0):
        print(i,end=" ")
print()

#colors=['red','green','blue','yellow','black'].print reverse of each color

colors=['red','green','blue','yellow','black']
for i in colors:
    print(i[::-1],end=' ')
print()

#print each digit in a number.n=1234

n=1234
for i in str(n):
    print(i,end=" ")
print()


#sum of digits in a number n=1234

n=1234
sum=0
for i in str(n):
    sum=sum+int(i)
    print(sum)
print()

#count of digits

#create a new list with squares of each number [1,2,3,4]

l=[1,2,3,4]
new=[]
for i in l:
    new.append(i**2)
print(new,end=" ")
print()
#create a new set with squares of each number [1,2,3,4]

newset=set()
for i in l:
    newset.add(i**2)
print(newset,end=" ")
print()

#create a new string with only vowels

new=''
vowels='aeiouAEIOU'
for i in s:
    if i in vowels:
        new=new+i
        print(i,end=" ")
print()

#given a list l=[1,2,3,4]
#create a dictionary where keys are numbers and values are square of each number
#o/p new={1:1,2:4,3:9,4:16}

l=[1,2,3,4]
new={}
for i in l:
    new[i]=i**2
print(new,end=' ')
print()

#reverse of a string without using slicing

s='hello'
rev=('')
for i in s:
    rev=i+rev
print(rev,end=' ')
print()

#reverse of a number
n=1234
rev=''
for i in str(n):
    rev=i+rev
print(rev,end=' ')
print()