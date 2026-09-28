#1.write a program to check whether the user entered number is 2 digit/3digit/4digit number

# num=int(input('enter a number : '))
# if(num>=10 and num<=99):
#     print('2 digit')
# elif(num>=100 and num<=999):
#     print('3 digit')
# else:
#     print('4 digit')



#write a basic calculator program to preform arithmetic operations (+,-,*,%,/,//)

# n1=int(input("enter the number1 : "))
# n2=int(input("enter the number2 : "))
# op=input('enter the operator to use : ')
# if op=='+':
#     print(f'sum is : {n1+n2}')
# elif op=='-':
#     print(f'difference is : {n1-n2}')
# elif op=='*':
#     print(f'product is : {n1*n2}')
# elif op=='/':
#     print(f'divide is : {n1/n2}')
# elif op=='%':
#     print(f'remainder is : {n1%n2}')
# else:
#     print(f'floor division is : {n1//n2}')

#3.write a program to print the number of days in a month

# month=input('enter a month : ')
# l1={'january','march','may','july','august','october','december'}
# l2={'april','june','september','november'}
# l3={'february'}
# if month in l1:
#     print("the number of days is 31")
# elif month in l2:
#     print("the number of days is 30")
# else:
#     print("the number of days is 28")

#4.write a program to print the grades based on the following criteria
#91-100  Grade A
#81-90 Grade B
#71-80 Grade C
#61-70  Grade D
#below 61  Grade E

# mark=int(input('enter the mark : '))
# if 91 <= mark <=100:
#     print('Grade A')
# elif 81 <= mark <=90:
#     print('Grade B')
# elif 71 <= mark <=80:
#     print('Grade C')
# elif 61 <= mark <=70:
#     print('Grade D')
# else:
#     print("Grade E")


#nested if
#write a program to check the following
#1. a number is divisible by 2 and 3
#2. a number is divisible by 2 and not divisible by 3
#3. a number is divisible by 3 and not divisible by 2
#4. number is not divisible by 2 and 3
# n=int(input('enter a number : '))
# if n%2==0:
#     print("divisible by 2")
#     if n%3==0:
#         print('divisible by 3')
#     else:
#         print('not divisible by 3')
# else:
#     print('not divisible by 2')
#     if n%3==0:
#         print('divisible by 3')
#     else:
#         print('not divisible by 3')



#check whether entered  number is positive even or odd
#check whether entered  number is negative even or odd

n=int(input('enter a number : '))
if n>0:
    print('number is positive')
    if n%2==0:
        print('number is positive even')
    else:
        print('number is positive odd')
else:
    print('number is negative')
    if n%2==0:
        print('number is negative even')
    else:
        print('number is negative odd')

