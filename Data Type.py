# Numbers

n1 = 10
n2 = 35.3
n3 = 1 + 5j

print(n1,'  Type is:',type(n1))
print('N1 is int:',isinstance(n1,int))

print(n2,'  Type is:',type(n2))
print('N2 is float:',isinstance(n2,float))

print(n3,'  Type is:',type(n3))
print('N3 is Complex:',isinstance(n3,complex))


#String

name='wonderland'

print(name)
print(name[0])
print(name[0:6])
print(name[6:])
print(name[:6])
print(name * 2)
print(name + " is grate place:")



#List

list=[10,20,21.5,'Rohit']

list[1] = 30

print(list)
print(list[1])
print(list[1:3])
print(list[1:])
print(list[:3])




#Tuple

tuple=[10,20,21.5,'Rohit']

list[1] = 30

print(tuple)
print(tuple[1])
print(tuple[1:3])
print(tuple[1:])
print(tuple[:3])


#Dictionary

d = {1:"rohan",2:"23","100":200}

print('d[1]:',d[1])
print('d[2]:',d[2])
print('100:',d["100"])