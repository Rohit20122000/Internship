num1 = int(input('Enter No. to find Factorial : '))

factorial = 1

for i in range(1,num1+1):
    factorial = factorial*i

print('The Factorial is : ',factorial)