#1 Given a string

s='I am learning python'

#find the length of the string
print("The length of the string is :",len(s))
#find the reverse of the string
reverse=s[::-1]
print("The reverse of the string is :",reverse)

#find the last character of the strings
lastchar=s[-1]
print("The last character of the string is :",lastchar)

#find the 13 th character

char=s[12]
print('The 13 the character is :',char)

#print the character from 2nd index to 15th index

char2=s[2:16:]
print("The character from 2nd index to 15th index :",char2)

#combines the string s with word programming

combine=s+' programming'
print("The comined string is :",combine)

#given a string s='python is a programming language'
#remove the first 10 character and print the remaining

s='python is a programming language'
index=s[10::]
print("The remaining string after removing first 10 character is :",index)


#print the last 5 character

last5=s[-5:]
print('Last 5 character the string is :',last5)