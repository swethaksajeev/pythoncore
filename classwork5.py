#write a program to find BMI(Body Mass Index)
#
# BMI= weight in (kg)/ height**2 in (m)
#
#
# BMI	                 Status
# ≤ 18.4	             Underweight
# 18.5 - 24.9	         Normal
# 25.0 - 39.9	         Overweight
# ≥ 40.0	             Obese

# weight=int(input('enter the weight : '))
# height=float(input('enter the height : '))
# bmi=weight/height**2
# if bmi<=18.4:
#     print('The person is underweight')
# elif 18.5<=bmi<=24.9:
#     print('The person is Normal')
# elif 25.0<=bmi<=39.9:
#     print('The person is overweight')
# elif bmi>=40 :
#     print('The person is obese')

#2.# A toy vendor supplies three types of toys:

# Battery Based Toys, Key-based Toys, and Electrical Charging Based Toys.

# The vendor gives a discount of 10% on orders for battery-based toys if the order is for more than Rs. 1000.

# On orders of more than Rs. 100 for key-based toys,a discount of 5% is given,

# and a discount of 10% is given on orders for electrical charging based toys of value more than Rs. 500.

# Assume that the numeric codes 1,2 and 3 are used for battery based toys, key-based toys, and electrical charging based toys respectively.

# Write a program that reads the product code and the order amount and prints out the net amount that the customer is required to pay after the discount.

code=int(input('enter the code : '))  #battery based code-1, key based code -2,electrical charging based -3
amount=int(input('enter the amount : '))
if code==1:
    if amount>=1000:
        d=amount-(amount*0.010)
        print('The discount price is : ',d)
    else:
        print('No discount')
elif code==2:
    if amount>100:
        d=amount-(amount*0.005)
        print('The discount price is : ',d)
    else:
        print('No discount')
elif code==3:
    if amount>500:
        d=amount-(amount*0.010)
        print('The discount price is : ',d)
    else:
        print('No discount')
else:
    print('Invalid code')




#3 FIZZBUZZ PRoblem

# if divisible by 3 only -print fizz
# if divisible by 5 only -print buzz
# if a number is divisible by 3 and 5
#     print fizzbuzz
#     otherwise -print the number

# num=int(input('enter a number : '))
# if num%3==0:
#     if num%5==0:
#         print('fizzbuzz')
#     else:
#         print('fizz')
# else:
#     if num%5==0:
#         print('buzz')
#     else:
#         print(num)