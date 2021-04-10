print('Hello Amol')
if 5>2:
 print("5 is greater than 2")

x=3
y="Var Y"
z=int(5)
a=str('AA')
A=str("aa")
b=float(2.5)
#Printing x and y values
print(x)
print(y)
print(z)
print(a)
print(A)
print(b)
print(type(z))
print(type(b))
""" Done with execution, 
now time to 
exit the program
"""

p,q,r=100,'ABC',12.3

print(p)
print(q)
print(r)

l=m=n=200.01

print(l)
print(m)
print(n)

fruits = ['Apple',"Banana",'Green Apple']
o,r,p=fruits
print(o)
print(r)
print(p)

s="Awesome"

def myfunc():
 global s
 s="Handsome"
 print("I am "+ s)

myfunc()
print('I am still '+s)

print("Exiting")