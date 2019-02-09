# this is to write the calculator 
# This function adds two numbers 
def add(x, y):
   return x + y

# This function subtracts two numbers 
def subtract(x, y):
   return x - y

# This function multiplies two numbers
def multiply(x, y):
   return x * y

# This function divides two numbers
def divide(x, y):
   return x / y

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == '1':
   print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
   print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
   print(num1,"/",num2,"=", divide(num1,num2))
else:
   print("hey i have a megic trick for you ")
# my code starts from here.
print("hey i have a megic trick for you ")

mgk = str(input("do you want to see it Y/N"))
if mgk == "y":
    number = int(input ("enter a number, any number"))

    print("the number you have written is " , number)

    while number <= 100:
        print (number)
        number = number + 2 
else:
    print('there is no magic trick for you ')
    
#my code ends here

