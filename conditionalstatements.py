#write a program to check whether number is even

# x=int(input("enter a number :"))
# if(x%2==0):
#     print("The given number is even")

#write a program to check whether the number is positive or negative

# y=int(input("enter a number : "))
# if(y>0):
#     print('The number is positive')
# else:
#     print('The number is negative')


#write a program to check whether the number is even or odd

# x=int(input('enter a number : '))
# if(x%2==0):
#     print(f"{x} is even")
# else:
#     print(f"{x} is odd")

#write a program to check whether the entered number is divisible by 3 or not

# x=int(input('enter a number : '))
# if(x%3==0):
#     print(f"{x} is divisible by 3")
# else:
#     print(f"{x} is not divisible by 3")

#write a program to display a name  if entered name contain letter 'n' else print 'no'

# name=input('enter the name : ')
# if('n' in name):
#     print("Name is : ",name)
# else:
#     print('no')

#write a program to display a name if the entered name starts with letter 'n' else display 'no'

# name=input('enter a name : ')
# if(name[0]=='n'):
#     print("The name is :",name)
# else:
#     print('no')

#write a program to display a location name if the entered location contains the word 'land' else print 'no'

# name=input("enter the location : ")
# if('land' in name):
#     print(name)
# else:
#     print('no')


#write a program to check whether the number is divisble by 5 and ends with 5

# num=int(input('enter a number'))
# if(num%5==0 and num%10==5):
#     print('the number is  divisble by 5 and ends with 5 : ' ,num)
# else:
#     print('no satisfying the condition')

#write a program to find the greatest of two numbers

# num1=int(input('enter 1st number : '))
# num2=int(input('enter 2nd number :'))
# if(num1>num2):
#     print(f"{num1} is greater than ",num2)
# else:
#     print(f"{num2} is greater than", num12)


#write a program to check whether the number is positive,negative or zero

# num=int(input('enter a number : '))
# if(num>0):
#     print("number is positive")
# elif(num<0):
#     print("number is negative")
# else:
#     print("the number is zero")

#write a program to find the greatest of three numbers
#
# num1=int(input('enter 1st number'))
# num2=int(input('enter 2nd number'))
# num3=int(input('enter 3rd number'))
#
# if(num1>num2 and num1>num3):
#     print(num1,'is greater than ',num2,',',num3 )
# elif(num2>num1 and num2>num3):
#     print(num2,'is greater than ',num1,',',num3)
# else:
#     print(num3,'is greater than ',num1,',',num2)

#write a program to check whether a person is eligible to vote or not

# age=int(input("enter the age : "))
# if(age>=18):
#     print("eligible")
# else:
#     print('not eligible')

#write a program to check whether a number is even odd or invalid

num=int(input('Enter a number : '))
if(num%2==0):
    print(num,'is even')
elif(num%2!=0):
    print(num,'is odd')
else:
    print('invalid')