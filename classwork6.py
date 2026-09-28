# # # 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5

for i in range(1,101,1):
    if(i%3==0  or i%5==0):
        print(i,end=' ')
print()

# # 2.Print the cumulative sum of a list.
# # Example: [1, 2, 3, 4] → Output: [1, 3, 6, 10]

l=[1,2,3,4]
new=[]
sum=0
for i in l:
    sum=sum+i
    new.append(sum)
print(new,end=' ')
print()

# # 3.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # Example: a = 3, b = 7 → Output: 25
sum=0
for i in range(3,8,1):
    sum=sum+i
print(sum,end=' ')
print()


# 4.Given a list, sum only the elements at even indices.
l=[10,20,30,40,50]
# Example:
#  → Sum = 10 + 30 + 50 = 90
sum=0
for i in range(0,len(l),2):
    sum=sum+l[i]
print(sum)
print()




#5.Given a list, sum the elements until a 0 is encountered (stop at 0).
l=[4,9,1,0,6,7]
sum=0
for i in l:
    sum = sum + i
    if i==0:
        break
print(sum,end=' ')
print()


# 6.Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.

for i in range(1,1001,1):
    if(i%7==0 and i%11==0):
        break
print(i ,end=' ')
print()


# 7.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.

l=['red','blue','yellow','green','brown']
for i in l:
    if len(i)>=5:
        print(i, end=' ')
        continue
print()




# 8.From a list of numbers, create a new list containing the squares of each element.
# Input: [1, 2, 3] → Output: [1, 4, 9]

l=[1,2,3]
new=[]
for i in l:
    new.append(i**2)
print(new,end=' ')
print()


# 9.Given a string, construct a new string with all vowels removed using a loop.
# Input: "hello world" → Output: "hll wrld"

s='hello world'
vowels='aeiouAEIOU'
new=' '
for i in s:
    if i not in vowels:
        new=new+i
print(new,end=' ')
print()

#
# 10.Given a list of numbers, create a new list where each number is doubled, but stop if any doubled number is greater than 50 (use break).
l=[5,2,8,6,2]
new=[]
for i in l:
    double=i * 2
    if double>50:
        break
    new.append(double)
print(new,end=' ')
print()


# 11.From a string containing mixed characters, create a new string containing only digits.
# Input: "abc123x7z" → Output: "1237"

digits="0123456789"
s="abc123x7z"
new=''
for i in s:
    if i in digits:
        new=new+i
print(new,end=' ')
print()



# 12.Given a list of strings, create a new list containing the length of each string.
# Input: ["cat", "banana", ""] → Output: [3, 6, 0]

s=["cat", "banana", ""]
new=[]
for i in s:
    l=len(i)
    new.append(l)
print(new,end=' ')
print()


# 13.Given a list of words, create a string made of the first letter of each word.
# Input: ["Python", "Is", "Great"] → Output: "PIG"

s=["Python", "Is", "Great"]
new=''
for i in s:
    l=i[0]
    new=new+l
print(new,end=' ')
print()



# 14.Replace Negative Numbers with 0
# Given a list of integers, create a new list where all negative numbers are replaced with 0.
# # Input: [4, -3, 2, -1] → Output: [4, 0, 2, 0]

s=[4, -3, 2, -1]
new=[]
for i in s:
    if i<0:
        i=0
    new.append(i)
print(new,end=' ')
print()


# 15.
d={101:['Arun',23,'ekm'], 102:['Amal',25,'tvm'],103:['Anu',26,'tcr'],104:['Kiran',27,'ekm']}
# #print all names of students
for i in d.values():
    print(i[0])

#
# 16.Write a program to print the numbers from 1 to 100.
# But for multiples of: 3, print “Fizz” instead of the number 5, print “Buzz” instead of the number. Both 3 and 5, print “FizzBuzz”
# Otherwise, print the number itself
# Output format example:
# 1, 2, Fizz, 4, Buzz, … , FizzBuzz, …

for i in range(1,101,1):
    if  i%3==0 and i%5==0:
        print('fizzbuzz',end=' ')
    elif i%5==0:
        print('buzz',end=' ')
    elif i%3==0:
        print('fizz',end=' ')
    else:
        print(i,end=' ')
print()
# 17.Write a Python program that prints numbers from 1 to 50:
#     Skip multiples of 5 using continue

for i in range(1,51,1):
    if i%5==0:
        continue
    print(i,end=' ')
print()
#     Stop the loop if the number becomes greater than 40 using break
for i in range(1,51,1):
    if i%5==0:
        continue
    elif i>40:
        break
    print(i,end=' ')
print()

# 18.Write a program to find
#     Reverse of a number(without[::-1])
x=1234
rev=''
for i in str(x):
    rev=i+rev
print(rev,end=' ')
print()
#     count the number of digits in a given number
x=12345
count=0
for i in str(x):
    count=count+len(i)
print(count,end=' ')
print()
#     sum of digits in  a number

x=12345
sum=0
for i in str(x):
    sum=sum+int(i)
print(sum,end=' ')
print()