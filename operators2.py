#logical operators

a=5
b=10
print(a&b)

a=30
b=50
print(a&b)

f=10
print('f =', f)
print('binary of f',bin(f))

print('interger of binary of f =',int('1010',2))


#compund assignment
a=10
a+=2
print(a)
a-=1
print(a)
a*=2
print(a)
a/=2
print(a)
a//=2
print(a)

#membership operator
s='hello'
print('e' in s)
print('e' not in s)

l=[1,2,3,4,5]
print(3 in l)
print(10 in l )

t=(1,2,3,4,5)
print(5 in t)
print(7 in t)

#identity operator - id

x=10
print('id of x = ',id(x))

y=25
print('id of y = ',id(y))

print('Is x is y = ',x is y)
print(x is not y)

#Bitwise operator

#. bitwise or = |

w=10
v=20
print('and =',w&v)

print('or =' ,w|v)

print('xor =',w^v)

#complement

a=2
print(~2)

#shift left

a=2

print('left swift =',a<<2)
print('right swift=',a>>2)

#Type conversion (Type casting) methods

a=10
print('tyoe of a =',type(a))

x=10.5
print(x)
print(type(x))
x=int(x)
print(x)
print(type(x))

x=float(x)
print(type(x))

print(complex(1,2))

a=10
a=str(a)
print(a) #it is converted to string but the output is shown as integer
print(type(a))

#list()

t=(1,2,3,4,5)
t=list(t)
print(t)
print(type(t))

t=tuple(t)
print(t)
print(type(t))

t=set(t)
print(t)
print(type(t))

seq=(('a',10),('d',15))
print(seq)
print(type(seq))
seq=dict(seq)
print(seq)
print(type(seq))

seq=tuple(seq)
print(seq)


sequ=[('name','ds'),('age',12)]
d=dict(sequ)
print(d)


#Ordinal

print(ord('a'))

print(chr(97))


