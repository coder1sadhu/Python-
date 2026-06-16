#type function is used to find the data type of a variable in Python.

a = 22

t= type(a) #class <int>

print (t)

b = "Hello"

f= type(b) #class <str>

print (f)

c = 22.2

#g=float(c)
g= type(c) #class <float>

print (g)

e = "22.2" #changing string to float
z=float(e) #class <float>
h= type(z) #class <float>

print (h)