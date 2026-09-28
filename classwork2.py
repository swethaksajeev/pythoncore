#1Given a string
s="Python coding is easy and fun"

# find the length of the string
print("length is :",len(s))
# find the reverse of the string

print('reverse is :',s[::-1])
# find the last character of the strings

print('last character is :',s[-1])
# #2.Given a list
l=['Guitar','Piano','Violin','Drums','Flute']
# Add a new item 'Veena' to the list

l.append('Veena')
print('Add a new item Veena to the list : ',l)

# #3Declare a list of 5 food items

lst=['salad','rice','cutlet','burger','biriyani']
print('Declare a list of 5 food items :' ,lst)
#     #Add new fooditem to the list
lst.append('pizza')
print('Add new fooditem to the list :', lst)
#     #change the second food item
lst[1]='porotta'
#     #print the updated list
print('change the second food item :',lst)
#     #print the last food item
print('the last food item :',lst[-1])
#     #print the number of food items
print('the number of food items :',len(lst))
#
# #4.Given a string s="python is a programming language"
s='python is a programming language'
print(s)
# #Remove the first 10 characters and print the remaining
print('Remove the first 10 characters and print the remaining: ' ,s[10::])
# #print the last 5 characters
print('the last 5 characters :',s[-5::])


