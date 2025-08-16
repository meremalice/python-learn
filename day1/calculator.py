#addition
def add(x, y):
    return x + y

#subract
def sub(x, y):
    return x - y

#Multiply
def multiply(x, y):
    return x * y

#Divide
def divide(x, y):
    return x / y

#inputs

x = int(input('Enter your First number: '))
y = int(input('Enter your Second number: '))
 
operation = input('What operation would you like to do?') 

res = 0
if operation == "+":
    res = add(x, y)
elif operation == "-":
    res = sub(x, y)
elif operation == '*':
    res = multiply(x, y)
elif operation == '/':
    res = divide(x, y)
else:
    res = "Wrong"


print(res)







