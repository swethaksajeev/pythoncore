# # # #
# # # # # i=1
# # # # # fact=1
# # # # # n=int(input('enter a number : '))
# # # # # while(i<=n):
# # # # #     fact=fact*i
# # # # #     i=i+1
# # # # # print('Factorial of the number is = ',fact)
# # # #
# # # # #multiplication table of a number
# # # #
# # # # #
# # # # # n=int(input('enter a number : '))
# # # # # i=1
# # # # # while(i<=10):
# # # # #     print(n,'*',i,'=',n*i)
# # # # #     i=i+1
# # # #
# # # # #
# # # # # #reverse of a string without using slicing
# # # # #
# # # # # s='hello'
# # # # # rev=''
# # # # # for i in s:
# # # # #     rev=i+rev
# # # # # print(rev)
# # # #
# # # # # s='hello'
# # # # # rev=('')
# # # # # for i in s:
# # # # #     rev=i+rev
# # # # # print(rev,end=' ')
# # # # # print()
# # # # #
# # # # # #reverse of a number
# # # # # n=1234
# # # # # rev=''
# # # # # for i in str(n):
# # # # #     rev=i+rev
# # # # # print(rev)
# # # #
# # # # # n=int(input('enter a number : '))
# # # # # i=1
# # # # # while(i<=10):
# # # # #     print(n,'*',i,'=',n*i)
# # # # #     i=i+1
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # #
# # # # # # # 1.Write a program that prints all numbers between 1 and 100 that are divisible by 3 or 5
# # # #
# # # # for i in range(1,101,1):
# # # #     if(i%3==0  or i%5==0):
# # # #         print(i,end=' ')
# # # # print()
# # # #
# # # # # # 2.Print the cumulative sum of a list.
# # # # # # Example: [1, 2, 3, 4] → Output: [1, 3, 6, 10]
# # #
# # #
# # # # l=[1,2,3,4]
# # # # sum=0
# # # # new=[]
# # # # for i in l:
# # # #     sum=sum+i   #1,1+2,3+3,6+4
# # # #     new.append(sum) #[1,3,6,10]
# # # # print(new)
# # # #
# # # # l=[1,2,3,4]
# # # # new=[]
# # # # sum=0
# # # # for i in l:
# # # #     sum=sum+i
# # # #     new.append(sum)
# # # # print(new,end=' ')
# # # # print()
# # # #
# # # # # # 3.Given two numbers a and b, calculate the sum of all numbers between them (inclusive). Use a for loop.
# # # # # # Example: a = 3, b = 7 → Output: 25
# # #
# # # # sum=0
# # # # for i in range(3,8,1):
# # # #     sum=sum+i
# # # # print(sum)
# # # # # sum=0
# # # # for i in range(3,8,1):
# # # #     sum=sum+i
# # # # print(sum,end=' ')
# # # # print()
# # # #
# # # #
# # # # # 4.Given a list, sum only the elements at even indices.
# # # # l=[10,20,30,40,50]
# # # # # # Example:
# # # # # #  → Sum = 10 + 30 + 50 = 90
# # # # sum=0
# # # # for i in range(0,len(l),2):
# # # #     sum=sum+l[i]
# # # # print(sum)
# # #
# # #
# # # # sum=0
# # # # for i in range(0,len(l),2):
# # # #     sum=sum+l[i]
# # # # print(sum)
# # # # print()
# # # #
# # # #
# # # #
# # # #
# # # # #5.Given a list, sum the elements until a 0 is encountered (stop at 0).
# # # # l=[4,9,1,0,6,7]
# # # # sum=0
# # # # for i in l:
# # # #     sum=sum+i
# # # #     if i==0:
# # # #         break
# # # # print(sum)
# # # # sum=0
# # # # for i in l:
# # # #     sum = sum + i
# # # #     if i==0:
# # # #         break
# # # # print(sum,end=' ')
# # # # print()
# # # #
# # # #
# # # # # 6.Loop from 1 to 1000 and find the first number divisible by both 7 and 11. Use break to stop once found.
# # # #
# # # # for i in range(1,1001,1):
# # # #     if(i%7==0 and i%11==0):
# # # #         break
# # # # print(i ,end=' ')
# # # # print()
# # # #
# # # #
# # # # # 7.Given a list of strings, print only those with length ≥ 5. Use continue to skip shorter ones.
# # # #
# # # # l=['red','blue','yellow','green','brown']
# # # # for i in l:
# # # #     if len(i)>=5:
# # # #         print(i, end=' ')
# # # #         continue
# # # # print()
# # # #
# # # #
# # # #
# # # #
# # # # # 8.From a list of numbers, create a new list containing the squares of each element.
# # # # # Input: [1, 2, 3] → Output: [1, 4, 9]
# # # #
# # # # l=[1,2,3]
# # # # new=[]
# # # # for i in l:
# # # #     new.append(i**2)
# # # # print(new,end=' ')
# # # # print()
# # # #
# # # #
# # # # # 9.Given a string, construct a new string with all vowels removed using a loop.
# # # # # Input: "hello world" → Output: "hll wrld"
# # # #
# # # # s='hello world'
# # # # vowels='aeiouAEIOU'
# # # # new=' '
# # # # for i in s:
# # # #     if i not in vowels:
# # # #         new=new+i
# # # # print(new,end=' ')
# # # # print()
# # # #
# # # # #
# # # # # 10.Given a list of numbers, create a new list where each number is doubled, but stop if any doubled number is greater than 50 (use break).
# # # # l=[5,2,8,2]
# # # # new=[]
# # # # for i in l:
# # # #     double=i*2
# # # #     if double>50:
# # # #         break
# # # #     new.append(double)
# # # # print(new)
# # # # for i in l:
# # # #     double=i * 2
# # # #     if double>50:
# # # #         break
# # # #     new.append(double)
# # # # print(new,end=' ')
# # # # print()
# # # #
# # # #
# # # # # 11.From a string containing mixed characters, create a new string containing only digits.
# # # # # Input: "abc123x7z" → Output: "1237"
# # # #
# # # # digits="0123456789"
# # # # s="abc123x7z"
# # # # new=''
# # # # for i in s:
# # # #     if i in digits:
# # # #         new=new+i
# # # # print(new)
# # # # for i in s:
# # # #     if i in digits:
# # # #         new=new+i
# # # # print(new,end=' ')
# # # # print()
# # # #
# # # #
# # # #
# # # # # 12.Given a list of strings, create a new list containing the length of each string.
# # # # # Input: ["cat", "banana", ""] → Output: [3, 6, 0]
# # # #
# # # # s=["cat", "banana", ""]
# # # # new=[]
# # # # for i in s:
# # # #     l=len(i)
# # # #     new.append(l)
# # # # print(new)
# # # # for i in s:
# # # #     l=len(i)
# # # #     new.append(l)
# # # # print(new,end=' ')
# # # # print()
# # # #
# # # #
# # # # # 13.Given a list of words, create a string made of the first letter of each word.
# # # # # Input: ["Python", "Is", "Great"] → Output: "PIG"
# # # #
# # # # s=["Python", "Is", "Great"]
# # # # new=''
# # # # for i in s:
# # # #     new=new+i[0]
# # # # print(new)
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # # new=''
# # # # for i in s:
# # # #     l=i[0]
# # # #     new=new+l
# # # # print(new,end=' ')
# # # # print()
# # # #
# # # #
# # # #
# # # # # 14.Replace Negative Numbers with 0
# # # # # Given a list of integers, create a new list where all negative numbers are replaced with 0.
# # # # # # Input: [4, -3, 2, -1] → Output: [4, 0, 2, 0]
# # # # #
# # # # s=[4, -3, 2, -1]
# # # # new=[]
# # # # for i in s:
# # # #     if i<0:
# # # #         i=0
# # # #     new.append(i)
# # # # print(new)
# # #
# # #
# # #
# # #
# # # # new=[]
# # # # for i in s:
# # # #     if i<0:
# # # #         i=0
# # # #     new.append(i)
# # # # print(new,end=' ')
# # # # print()
# # # #
# # # #
# # # # # 15.
# # # # d={101:['Arun',23,'ekm'], 102:['Amal',25,'tvm'],103:['Anu',26,'tcr'],104:['Kiran',27,'ekm']}
# # # # # # #print all names of students
# # # # for i in d.values():
# # # #     print(i[0])
# # #
# # # # for i in d.values():
# # # #     print(i[0])
# # # #
# # # # #
# # # # # 16.Write a program to print the numbers from 1 to 100.
# # # # # But for multiples of: 3, print “Fizz” instead of the number 5, print “Buzz” instead of the number. Both 3 and 5, print “FizzBuzz”
# # # # # Otherwise, print the number itself
# # # # # Output format example:
# # # # # 1, 2, Fizz, 4, Buzz, … , FizzBuzz, …
# # #
# # # # for i in range(1,101,1):
# # # #     if i%3==0:
# # # #         if i%5==0:
# # # #             print('fizzbuzz')
# # # #         else:
# # # #             print('fizz')
# # # #     else:
# # # #         if i%5==0:
# # # #             print('buzz')
# # # #         else:
# # # #             print(i)
# # #
# # #
# # # #
# # # # for i in range(1,101,1):
# # # #     if  i%3==0 and i%5==0:
# # # #         print('fizzbuzz',end=' ')
# # # #     elif i%5==0:
# # # #         print('buzz',end=' ')
# # # #     elif i%3==0:
# # # #         print('fizz',end=' ')
# # # #     else:
# # # #         print(i,end=' ')
# # # # print()
# # # # # 17.Write a Python program that prints numbers from 1 to 50:
# # # # #     Skip multiples of 5 using continue
# # # #
# # # # for i in range(1,51,1):
# # # #     if i%5==0:
# # # #         continue
# # # #     print(i,end=' ')
# # # # print()
# # # # #     Stop the loop if the number becomes greater than 40 using break
# # # # for i in range(1,51,1):
# # # #     if i%5==0:
# # # #         continue
# # # #     elif i>40:
# # # #         break
# # # #     print(i,end=' ')
# # # # print()
# # # #
# # # # # 18.Write a program to find
# # # # #     Reverse of a number(without[::-1])
# # # # x=1234
# # # # rev=''
# # # # for i in str(x):
# # # #     rev=i+rev
# # # # print(rev,end=' ')
# # # # print()
# # # # #     count the number of digits in a given number
# # #
# # # #
# # # # x=12345
# # # # count=0
# # # # for i in str(x):
# # # #     count=count+len(i)
# # # # print(count)
# # # # x=12345
# # # # count=0
# # # # for i in str(x):
# # # #     count=count+len(i)
# # # # print(count,end=' ')
# # # # print()
# # # # #     sum of digits in  a number
# # # #
# # # # x=12345
# # # # sum=0
# # # # for i in str(x):
# # # #     sum=sum+int(i)
# # # # print(sum)
# # # # for i in str(x):
# # # #     sum=sum+int(i)
# # # # print(sum,end=' ')
# # # # print()
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # #
# # # # # #normal code
# # # # # s='hello'
# # # # # for i in s:
# # # # #     print(i,end=' ')
# # # # # print()
# # # # #
# # # # # #using break
# # # # #
# # # # # for i in s:
# # # # #     if i=='l':
# # # # #         break
# # # # #     print(i,end=' ')
# # # # # print()
# # # # #
# # #
# # # # # #using continue
# # # # #
# # # # # for i in s:
# # # # #     if i=='l':
# # # # #         continue
# # # # #     print(i,end=' ')
# # # # # print()
# # # #
# # # # #1.given a list of numbers
# # # # l=[25,67,34,78,17,44,82]
# # # # #print all the numbers
# # # #
# # # # for i in l:
# # # #     print(i,end=" ")
# # # # print()
# # # #
# # # # #stops the loop when i>50
# # # # for i in l:
# # # #     if i>50:
# # # #         break
# # # #     print(i,end=' ')
# # # # print()
# # # #
# # # # #skip all even numbers
# # # #
# # # # for i in l:
# # # #     if i%2==0:
# # # #         continue
# # # #     print(i,end=' ')
# # # # print()
# # # #
# # # # #2. given a list of colors
# # # # colors=['red','green','yellow','blue','orange','black']
# # # #
# # # # #print all colors
# # # #
# # # # for i in colors:
# # # #     print(i,end=' ')
# # # # print()
# # # # #print those colors starting with 'b'
# # # #
# # # # for i in colors:
# # # #     if i[0]=='b':
# # # #         print(i,end=' ')
# # # # print()
# # # # #print the first color starting with 'b'
# # # #
# # # # for i in colors:
# # # #     if i[0]=="b":
# # # #         print(i,end=' ')
# # # #         break
# # # # print()
# # # # #skip all colors starting with 'b'
# # # #
# # # # for i in colors:
# # # #     if i[0]=='b':
# # # #         continue
# # # #     print(i,end=' ')
# # # # print()
# # # #
# # # # #3.given
# # # # s='python coding is easy and fun'
# # # # #print all characters upto specific character(including that character)
# # # #
# # # # char=input('enter a character : ')
# # # # for i in s:
# # # #      print(i,end=' ')
# # # #      if i == char:
# # # #         break
# # # # print()
# # #
# # # #write a program to check whether a number is armstrong number
# # #
# # #
# # # #
# # # # sum=0
# # # # num=153
# # # # s=str(num)
# # # # l=len(s)
# # # # for i in s:
# # # #     sum=sum+int(i)**l
# # # # if sum==num:
# # # #     print('arm')
# # # # else:
# # # #     print('no')
# # #
# # # # sum=0
# # # # num=int(input('enter a number : '))
# # # # s=str(num)
# # # # l=len(s)
# # # # for i in s:
# # # #     sum=sum+int(i)**l
# # # # if sum==num:
# # # #     print(num,' is armstrong')
# # # # else:
# # # #     print('not armstrong')
# # #
# # # #print factors of a number
# # #
# # # # num=3
# # # # for i in range(1,5+1,1):
# # # #     if num%i==0:
# # # #         print(i,end=' ')
# # #
# # # # num=int(input('enter a number : '))
# # # # for i in range(1,num+1,1):
# # # #     if num%i==0:
# # # #         print(i,end=' ')
# # # # print()
# # #
# # # #for else statement
# # #
# # # # for i in range(1,6,1):
# # # #     print(i)
# # # # else:   #it works only after the normal execution loop
# # # #     print('hello')
# # #
# # # #check whether a number is prime or not
# # #
# # # # num=8
# # # #
# # # # if(num>1):
# # # #     for i in range(2,num):
# # # #         if num%i==0:
# # # #             print('not prime')
# # # #             break
# # # #     else:
# # # #         print('prime')
# # # # else:
# # # #     print('not')
# # #
# # # # num=int(input('enter a number : '))
# # # # if(num>1):
# # # #     for i in range(2, num):
# # # #         if num % i == 0:
# # # #             print(num, 'is not prime')
# # # #             break
# # # #     else:
# # # #         print(num, 'is prime')
# # # # else:
# # # #     print('number is neither prime nor composite ')
# # # #
# # #
# # # # NESTED LOOP
# # # #
# # # # l=[10,20,30]
# # # # for i in l:
# # # #     for j in range(1,4):
# # # #         print(i,end=' ')
# # # #     print()
# # #
# # # #PATTERN PRINTING
# # #
# # # # for i in range(1,4,1):
# # # #     for j in range(1,4):
# # # #         print(i,end=' ')
# # # #     print(i)
# # #
# # # # for i in range(1,4,1):
# # # #     for j in range(1,4):
# # # #         print(i,end=' ')
# # # #     print(i)
# # # # for i in range(1,4):
# # # #     for j in range(1,5):
# # # #         print(j,end=' ')
# # # #     print()
# # #
# # #
# # # # for i in range(1,5):
# # # #     for j in range(1,5):
# # # #         print('*',end=' ')
# # # #     print()
# # #
# # #
# # # # l=[['lion','tiger'],['cat','elephant']]
# # # # for i in l:
# # # #     print(i,end=' ')
# # # #     for j in i:
# # # #         print(j,end=' ')
# # # #     print()
# # #
# # # # #1.given list
# # # names=['kelly','alan','jeny']
# # # # #print
# # # # #kelly kelly kelly
# # # # #alan alan alan
# # # # #jeny jeny jeny
# # #
# # # # for i in names:
# # # #     for j in range(1,4):
# # # #         print(i,end=' ')
# # # #     print()
# # #
# # # #
# # # # for i in names:
# # # #     for j in range(1,4):
# # # #         print(i,end=' ')
# # # #     print()
# # # #
# # # #
# # # # #2.given list
# # # # n=[1,2,3]
# # # # q=['what','when','why']
# # # #
# # # # # print
# # # # # 1
# # # # # what when why
# # # # # 2
# # # # # whatwhen why
# # # # # 3
# # # # # what when why
# # # #
# # # # n=[1,2,3]
# # # # q=['what','when','why']
# # # #
# # # # for i in n:
# # # #     print(i)
# # # #     for j in q:
# # # #         print(j,end=' ')
# # # #     print()
# # #
# # #
# # # #
# # # # for i in n:
# # # #     print(i)
# # # #     for j in q:
# # # #         print(j,end=' ')
# # # #     print()
# # # #
# # # #
# # # #
# # # # #3.given a list
# # # #
# # # # # d=[{'id':101,'name':'arun','age':23},{'id':102,'name':'amal','age':24}
# # # # #    {'id':103,'name':'anu','age':25}]
# # # # #print each student details
# # # # #id name age
# # # #
# # # d=[{'id':101,'name':'arun','age':23},{'id':102,'name':'amal','age':24},
# # #     {'id':103,'name':'anu','age':25}]
# # #
# # # # for i in d:
# # # #     for j in i.values():
# # # #         print(j,end=' ')
# # # #     print()
# # # # for i in d:
# # # #     for j in i.values():
# # # #         print(j,end=' ')
# # # #     print()
# # # #
# # # # #next ques
# # # # d={'id':101,'name':'arun','age':23}
# # # # for i,j in d.items():
# # # #     print(i,j)
# # # #
# # # # #next ques
# # # # d=[{'id':101,'name':'arun','age':23},{'id':102,'name':'amal','age':24},
# # # #     {'id':103,'name':'anu','age':25}]
# # # # for i in d:
# # # #      for k,j in i.items():
# # # #          print(k,j,end=' ')
# # # #      print()
# # # #
# # # # #pattern
# # # #
# # # # for i in range(1,5):
# # # #     for j in range(1,i+1):
# # # #         print('*',end=' ')
# # # #     print()
# # # #
# # # #
# # # # for i in range(1,5):
# # # #     for j in range(1,i+1):
# # # #         print('*',end=' ')
# # # # # #
# # # # # *
# # # # # * *
# # # # *
# # # # # * * * * *
# # # # # * * * * * * *
# # # #
# # # # for i in range(1,8,2):
# # # #     for j in range(1,i+1):
# # # #         print('*',end=' ')
# # # #     print()
# # # #
# # # # # 1
# # # # # 2 2
# # # # # 3 3 3
# # # # # 4 4 4 4
# # # #
# # # # for i in range(1,5):
# # # #     for j in range(1,i+1):
# # # #         print(i,end=' ')
# # # #     print()
# # # #
# # # # # 1
# # # # # 1 2
# # # # # 1 2 3
# # # # # 1 2 3 4
# # # #
# # # # for i in range(1,5):
# # # #     for j in range(1,i+1):
# # # #         print(j,end=' ')
# # # #     print()
# # # #
# # # #
# # # # for i in range(4,0,-1):
# # # #     for j in range(i):
# # # #         print('*',end=' ')
# # # #     print()
# # #
# # # #print all prime numbers
# # # #
# # # # l=[23,45,78,90,12,13,91]
# # # # for i in l:
# # # #     for j in range(2,i):
# # # #         if i%j==0:
# # # #             break
# # # #     else:
# # # #         print(i)
# # #
# # # #find all prime numbers in the range (1,100)
# # #
# # # # for i in range(2,101):
# # # #     for j in range(2,i):
# # # #         if i%j==0:
# # # #             break
# # # #     else:
# # # #         print(i,end=' ')
# # # # print()
# # #
# # # #find all armstrong numbers in the range (100,1000)
# # #
# # #
# # # # for i in range(100,1001):
# # # #     s = str(i)
# # # #     l = len(s)
# # # #     sum = 0
# # # #     for j in s:
# # # #         sum=sum+int(j)**l
# # # #     if sum==i:
# # # #         print(i,end=' ')
# # # # print()
# # #
# # # #eg
# # #
# # # # for i in range(1,5):
# # # #     for j in range(1,6):
# # # #         print(j,end=' ')
# # # #     print()
# # #
# # # #eg
# # #
# # # # for i in range(4,0,-1):
# # # #     for j in range(1,i+1):
# # # #         print('*',end=' ')
# # # #     print()
# # #
# # #
# # # # k=1
# # # # for i in range(1,5):
# # # #     for j in range(1,i+1):
# # # #         print(k,end=' ')
# # # #         k=k+1
# # # #     print()
# # #
# # # # k=ord('A')
# # # # for i in range(1,5):
# # # #     for j in range(1,i+1):
# # # #         print(chr(k),end=' ')
# # # #         k=k+1
# # # #     print()
# # #
# # #
# # #
# # # # A
# # # # B B
# # # # C C C
# # # # D D D D
# # #
# # #
# # #
# # # # for i in range(1,5):
# # # #
# # # #     k = ord('A')
# # # #     for j in range(1,i+1):
# # # #         print(chr(k),end=' ')
# # # #         k=k+1
# # # #     print()
# # # # k=ord('A')
# # # # for i in range(1,5):
# # # #     for j in range(1,i+1):
# # # #         print(chr(k),end=' ')
# # # #     k=k+1
# # # #     print()
# # #
# # #
# # # # A
# # # # A B
# # # # A B C
# # # # A B C D
# # #
# # # # for i in range(1,5):
# # # #     k = ord('A')
# # # #     for j in range(1,i+1):
# # # #         print(chr(k),end=' ')
# # # #         k=k+1
# # # #     print()
# # #
# # # # for i in range(1,5):
# # # #     for j in range(1,5):
# # # #         print(i,end=' ')
# # # #     print()
# # #
# # # # 1 0 0 0
# # # # 0 2 0 0
# # # # 0 0 3 0
# # # # 0 0 0 4
# # #
# # # # for i in range(1,5):
# # # #     for j in range(1,5):
# # # #         if i==j:
# # # #             print(i,end=' ')
# # # #         else:
# # # #             print(0,end=' ')
# # # #
# # # #     print()
# # #
# # # # for i in range(1,5):
# # # #     for j in range(1,5):
# # # #         if i==j:
# # # #             print(i,end=' ')
# # # #         else:
# # # #             print(0,end=' ')
# # # #     print()
# # #
# # # # 1
# # # # 1 0
# # # # 1 0 1
# # # # 1 0 1 0
# # #
# # #
# # #
# # # # for i in range(1,5):
# # # #     for j in range(1,i+1):
# # # #         if j%2!=0:
# # # #             print(1,end=' ')
# # # #         else:
# # # #             print(0,end=' ')
# # # #     print()
# # # # for i in range(1,5):
# # # #     for j in range(1,i+1):
# # # #         if(j%2!=0):
# # # #             print(1,end=' ')
# # # #         else:
# # # #             print(0,end=' ')
# # # #     print()
# # #
# # #
# # # # 0
# # # # 0 1
# # # # 0 1 2
# # # # 0 1 2 3
# # # # 0 1 2 3 4
# # #
# # # # for i in range(0,5):
# # # #     for j in range(0,i+1):
# # # #         print(j,end=' ')
# # # #     print()
# # #
# # #
# # # # h
# # # # h e
# # # # h e l
# # # # h e l l
# # # # h e l l o
# # # # h e l l o
# # # # h e l l o   w
# # # # h e l l o   w o
# # # # h e l l o   w o r
# # # # h e l l o   w o r l
# # # # h e l l o   w o r l d
# # #
# # #
# # #
# # # s='hello wrold'
# # # for i in range(len(s)):
# # #     for j in range(i+1):
# # #         print(s[j],end=' ')
# # #     print()
# # # # s='hello world'
# # # # for i in range(len(s)):
# # # #     for j in range(i+1):
# # # #         print(s[j],end=' ')
# # # #     print()
# # #
# # #
# # # #       *
# # # #     * *
# # # #   * * *
# # # # * * * *
# # #
# # # # k=3*2
# # # # for i in range(1,5):
# # # #     for p in range(1,k+1):  #for printing space in each line
# # # #         print(end=' ')
# # # #     for j in range(1,i+1): #for printing stars in each line
# # # #         print('*',end=' ')
# # # #     k=k-2
# # # #     print()
# # #
# # #
# # # #       *
# # # #     *   *
# # # #   *   *   *
# # # # *   *   *   *
# # #
# # #
# # # # k=3*2
# # # # for i in range(1,5):
# # # #     for p in range(1,k+1):  #for printing space in each line
# # # #         print(end=' ')
# # # #     for j in range(1,i+1): #for printing stars in each line
# # # #         print('*',end='   ')
# # # #     k=k-2
# # # #     print()
# # #
# # #
# # # #       *
# # # #     * *
# # # #   * * *
# # # # * * * *
# # # #   * * *
# # # #     * *
# # # #       *
# # #
# # #
# # # # k=3*2
# # # # for i in range(1,5):
# # # #     for p in range(1,k+1):
# # # #         print(end=' ')
# # # #     for j in range(1,i+1):
# # # #         print('*',end=' ')
# # # #     k=k-2
# # # #     print()
# # # # k=2
# # # # for i in range(3,0,-1):
# # # #     for p in range(1,k+1):
# # # #         print(end=' ')
# # # #     for j in range(1,i+1):
# # # #         print('*',end=' ')
# # # #     k=k+2
# # # #     print()
# # #
# # # #       *
# # # #     *   *
# # # #   *   *   *
# # # # *   *   *   *
# # # #   *   *   *
# # # #     *   *
# # # #       *
# # #
# # # # k=3*2
# # # # for i in range(1,5):
# # # #     for p in range(1,k+1):
# # # #         print(end=' ')
# # # #     for j in range(1,i+1):
# # # #         print('*',end='   ')
# # # #     k=k-2
# # # #     print()
# # # # k=2
# # # # for i in range(3,0,-1):
# # # #     for p in range(1,k+1):
# # # #         print(end=' ')
# # # #     for j in range(1,i+1):
# # # #         print('*',end='   ')
# # # #     k=k+2
# # # #     print()
# # #
# # #
# # # #       1
# # # #     1   2
# # # #   1   2   3
# # # # 1   2   3   4
# # # #   1   2   3
# # # #     1   2
# # # #       1
# # #
# # #
# # # # k=3*2
# # # # for i in range(1,5):
# # # #     for p in range(1,k+1):
# # # #         print(end=' ')
# # # #     for j in range(1,i+1):
# # # #         print(j,end='   ')
# # # #     k=k-2
# # # #     print()
# # # # k=2
# # # # for i in range(3,0,-1):
# # # #     for p in range(1,k+1):
# # # #         print(end=' ')
# # # #     for j in range(1,i+1):
# # # #         print(j,end='   ')
# # # #     k=k+2
# # # #     print()
# # #
# # # #comprehension
# # #
# # #
# # # # #normal code
# # # # # l=[1,2,3,4]
# # # # # new=[]
# # # # # for i in l:
# # # # #     new.append(i**2)
# # # # # print(new)
# # # # import math
# # # #
# # # # #using comprehension same code for above code
# # # #
# # # l=[1,2,3,4]
# # # new=[i**2 for i in l]
# # # print(new)
# # # # # l=[1,2,3,4]
# # # # # new=[i**2 for i in l]
# # # # # print(new)
# # # # #
# # # # # l=[1,2,3,4]
# # # # # new=[i**3 for i in l]
# # # # # print(new)
# # # # #
# # # # # l=[1,2,3,4]
# # # # # new=[5 for i in l]
# # # # # print(new)
# # # #
# # l=[23,56,34,12,89,90,24]
# # # #
# # # # #create a new list with even values
# # # # #normal code
# # # #
# # # # new=[]
# # # # for i in l:
# # # #     if i%2==0:
# # # #         new.append(i)
# # # # print(new,end=' ')
# # # # print()
# # # #
# # # new=[i for i in l if i%2==0]
# # # print(new)
# # # # #using list comprehension same code can be written like below
# # # #
# # # # new=[i for i in l if i%2==0]
# # # # print(new)
# # # #
# # # # #create a new list with numbers grater than 50
# # # #
# # # new=[i for i in l if i>50]
# # # print(new)
# # # # new=[i for i in l if i>50]
# # # # print(new)
# # # #
# # # #
# # # # #create a new list of cubes
# # # l=[1,2,3,4]
# # # new=[i**3 for i in l]
# # # print(new)
# # # # new=[i**3 for i in l]
# # # # print(new)
# # # #
# # # # #create a new list of square roots
# # # l=[25,36,81,100]
# # # new=[i**0.5 for i in l]
# # # print(new)
# # # # new=[i**0.5  for i in l]
# # # # print(new)
# # # #
# # # # #create a new list of lengths
# # colors=['red','green','blue','yellow','black']
# # # # #create a new list of first characters
# # new=[len(c) for c in colors]
# # print(new)
# # new=[c[0] for c in colors]
# # print(new)
# # # #
# # # # length=[len(c) for c in colors ]
# # # # new=[c[0] for c in colors]
# # # # print(new)
# # # #
# # # # #create a new list of last characters
# # # #
# # new=[c[-1] for c in colors]
# # print(new)
# # # # new=[c[-1] for c in colors]
# # # # print(new)
# # # # #create a new list of reverse of each element
# # # #
# # new=[c[::-1] for c in colors]
# # print(new)
# # # # new=[i[::-1] for i in colors]
# # # # print(new)
# # # #
# # # # #print length of colors
# # # # new=[len(i) for i in colors]
# # # # print(new)
# # new=[len(i) for i in colors]
# # print(new)
# # # #
# # # # #Given a list l=[23,78,12,56]
# # # # #Add 10 to each element in the given sequence
# # # #
# # # # l=[23,78,12,56]
# # # # new=[i+10 for i in l]
# # # # print(new)
# # # #
# # # # #given a list of dictionaries
# # # # # l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
# # # # #    {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
# # # # #    {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# # # # #
# # # # # create a new list of emails
# # # #
# # # # l=[{'empid':100,'name':'arun','salary':20000,'email':'arun@gmail.com'},
# # # #   {'empid':101,'name':'amal','salary':25000,'email':'amal@gmail.com'},
# # # #   {'empid':102,'name':'anu','salary':30000,'email':'anu@gmail.com'}]
# # # #
# # # # new=[i['email'] for i in l]
# # # # print(new)
# # # #
# # # #
# # # # # #Given a dictionary
# # # # d={'arun':25,'amal':34,'akhil':26,'anu':21}
# # # # # # create a list of names
# # # #
# # # # new=[i for i in d]
# # # # print(new)
# # # # # # create a list of marks
# # # #
# # # # new=[i for i in d.values()]
# # # # print(new)
# # # #
# # # #
# # # # # #Given a list
# # # # l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
# # # #
# # # # # #create a list of string values
# # # #
# # # # new=[i for i in l if type(i)==str]
# # # # print(new)
# # # #
# # # # # #create a list of floats
# # # #
# # # # new=[i for i in l if type(i)==float]
# # # # print(new)
# # # # # #create a list of positive numbers
# # # #
# # # # l=[23,56,12,89,-34,-23,-67,-43,9.7,4.5,'hello','world']
# # # # new=[i for i in l if type(i)!=str and i>0]
# # # # print(new)
# # # #
# # # #
# # # # #
# # # # # #Given a list
# # # # fruits=['apple','orange','pineapple','avocado','grapes']
# # # # # #create a new list with elements whose length is greater than 6
# # # #
# # # # new=[i for i in fruits if len(i)>6]
# # # # print(new)
# # # #
# # # # # #create a new list with elements whose value is divisible by 3 in range(1,101)
# # # #
# # # # new=[i for i in range(1,101) if i%3==0]
# # # # print(new)
# # # # # Given
# # # # s="python coding  is easy and fun"
# # # # # # create a new list with only vowels
# # # #
# # # # vowels='aeiouAEIOU'
# # # # new=[i for i in s if i in vowels]
# # # # print(new)
# # #
# # # #set
# # #
# # # # s="python coding  is easy and fun"
# # # # new={i for i in s if i in 'aeiouAEIOU'}
# # # # print(new)
# # #
# # # #dictionary
# # #
# # # #crate a new dictionary where keys are numbers and values are squares of each number
# # #
# # # # l=[1,2,3,4]
# # # # new={i:i**2 for i in l}
# # # # print(new)
# # #
# # # #normal code for above code
# # #
# # # # l=[1,2,3,4]
# # # # new={}
# # # # for i in l:
# # # #     new[i]=i**2
# # # # print(new)
# # #
# # # #given a list
# # # # l=[10,20,30,40]
# # # #  0   1  2  3
# # # #create a new dictionary where keys are the indexes and values are numbers
# # # #o/p {0:10,1:20,2:30,3:30}
# # #
# #
# #
# # l=[10,20,30,40]
# #
# # new={i:l[i] for i in range(0,len(l))}
# # print(new)
# # # # new={i:l[i] for i in range(0,len(l))}
# # # # print(new)
# # #
# # # # to iterate in charaters
# # # # s='hello world'
# # # # for i in s:
# # # #     print(i,end=' ')
# # # # print()
# # #
# # # # to iterate in words
# # # # s='hello world'
# # # # for i in s.split():
# # # #     print(i,end=' ')
# # # # print()
# # #
# # # #given a string
# # s='python coding is easy and fun'
# # # # create a new dictionary where keys are words and values are the length of each word
# # # #o/p {'python': 6, 'coding': 6, 'is': 2, 'easy': 4, 'and': 3, 'fun': 3}
# # #
# # # #s='python coding is easy and fun'
# # # # new={i:len(i) for i in s.split()}
# # # # print(new)
# #
# # # new={i:len(i) for i in s.split()}
# # # # print(new)
# # #
# # # g=s.split()
# # # print(g)
# # new={i for i in s if i in 'aeiou'}
# # print(new)
#
#

# # #sum of 2 numbers
# #
# # # plain code
# #
# # # n1=int(input('enter n1 : '))
# # # n2=int(input('enter n2 : '))
# # # s=n1+n2
# # # print('Sum = ',s)


# def add(n1,n2):
#     s=n1+n2
#     print('sum :',s)
#     return
# add(20,30)


# #
# # # def add():
# # #     'addition of 2 numbers'
# # #     n1=int(input('enter n1 : '))
# # #     n2=int(input('enter n2 : '))
# # #     s=n1+n2
# # #     print('Sum = ',s)
# # #
# # #     return
# # #
# # # add()
# #
# #
# # #define a function to display 'hello your name'
# #

# def name(i):
#     print(i)
#     return
# name('swetha')


# # def name():
# #     i=input('enter your name')
# #     print(i)
# #     return
# # name()
# #
# # #define a function to find the factorial of a number
# #

# def fact():
#     i=1
#     f=1
#     n=5
#     while(i<=n):
#         f=f*i
#         i=i+1
#     print(f)
#     return
# fact()

# # def fact():
# #     i=1
# #     f=1
# #     n=int(input('enter a number : '))
# #     while(i<=n):
# #         f=f*i
# #         i=i+1
# #     print('Factorial = ',f)
# #     return
# # fact()
# #
# # #define a function to find the count of  a specific character in a given string
# #
#
# def count_ch():
#     count=0
#     s='hello'
#     ch='l'
#     for i in s:
#         if i==ch:
#             count=count+1
#     print(count)
#     return
# count_ch()


# # def count_ch():
# #     s=input('enter a string : ')
# #     char_to_find=input('enter character :  ')
# #     count=0
# #     for i in s:
# #         if i == char_to_find:
# #             count=count+1
# #     print('Count = ',count)
# #     return
# # count_ch()
# #
# #
# # #define a function to check whether a number is prime or not
# # #
#
# def prime():
#     num=10
#     if(num>1):
#         for i in range(2,num):
#             if num%i==0:
#                 print('not prime')
#                 break
#         else:
#             print('prime')
#     else:
#         print('not prime not composite')
#     return
# prime()



# # def prime():
# #     n=int(input('enter a number : '))
# #     if n>1:
# #         for i in range(2,n):
# #             if n%i==0:
# #                 print('not prime')
# #                 break
# #         else:
# #             print('prime')
# #     else:
# #         print('number is either prime nor composite')
# #     return
# # prime()
# #
#
#
# #define a function to find the factors of a number
#


# def fact():
#     n=45
#     for i in range(1,n+1):
#         if n%i==0:
#             print(i,end=' ')
#     return
# fact()







# # def fact():
# #     num=int(input('enter a number'))
# #     for i in range(1,num+1):
# #         if num%i==0:
# #             print(i)
# #     return
# # fact()
#
# #with arguments and parameters
#
# # sum of two numbers
#
# # def add(n1,n2):
# #     s=n1+n2
# #     print('sum = ',s)
# #     return
# # add(12,12)
# #
# # a=int(input('enter number'))
# # b=int(input('enter number'))
# # add(a,b)
#
#
# #define a function that takes amount,year,rate as arguments and find the simple interest value(dynamic input)
#
#

# def simpleint(p,n,r):
#     s=(p*n*r)/100
#     print(s)
#     return
# simpleint(1000,4,7)




# # def simple_interest(p,n,r):
# #     si=(p*n*r)/100
# #     print('simple interest',si)
# #     return
# # p=int(input('enter amount'))
# # n = int(input('enter year'))
# # r = int(input('enter rate'))
# # simple_interest(p,n,r)
#
# #return statement
# #define a funtion that takes 2 numbers as arguments and return sum as result call the function at the end of the result
#
# # def add(n1,n2):
# #     s=n1+n2
# #     return s
# # n1=int(input('enter n1 : '))
# # n2=int(input('enter n2 : '))
# # a=add(n1,n2)
# # print(a)
# #
# #
# # #define a function that takes a string as argument and return a new dictionary where keys are words and values are length of each word call the function and print the dictionary
# # #inputs : s='python coding is easy and fun'
# # #o/p
# #
# # #new={i:len(i) for i in s.split()}
# #
#


#
# #define a function that takes a number as argument and check whether that number is spy number or not
# #spy number means 'sum of digits =product of digits'
# #eg: 22 : 2+2=2*2 , 1124  : 1+1+2+4=1*1*2*4
#
# # num=int(input('enter a number : '))
# # def spy(num):
# #     sum=0
# #     pro=1
# #     for i in str(num):
# #         sum=sum+int(i)
# #         pro=pro*int(i)
# #     if sum==pro:
# #         print('spy number')
# #     else:
# #         print('not a spy number')
# #     return
# # spy(num)
#
# #keyword argument
#
# # def fun(n,a):
# #     print('name : ',n)
# #     print('age : ',a)
# # fun(n='arun',a=23)
# # fun(a=23,n='arun')
#
# #default argument
#
# def fun(n,a=23):
#     print('name : ',n)
#     print('age : ',a)
# # fun('arun',25)
# fun('arun')
#


# def fun(**kwargs):
#     print(kwargs)
#     return
# fun(a=20,b=30)


# # def fun(*args):
# #     print(args)
# # fun(10,20 )
# # fun(1,2,3,4,5)
#
#
# # def fun(**kwargs):
# #     print(kwargs)
# # fun(a=10,b=20)
# # fun(a=10,b=20,c=30)
#
#
# #define a functions find the sum of numbers using arbitary argument type
#

# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# print(add(23,45,67))

def add(**kwargs):
    sum=0
    for i in kwargs.values():
        sum=sum+i
    return sum
print(add(a=56,b=89))



# #positional argument
# def add(*args):
#     sum=0
#     for i in args:
#         sum=sum+i
#     return sum
# print(add(10,20))
# print(add(1,2,3,4,5))
#
#
# #keyword argument
# def add(**kwargs):
#     sum=0
#     for i in kwargs.values():
#         sum=sum+i
#     return sum
# print(add(a=10,b=20))
# print(add(a=1,b=2,c=3,d=4,e=5))
#
