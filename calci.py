# this script is a calculator 
print("NOTE : THIS IS THE CALCULATION OF ONLY TWO NUMBERS") 
print("tell me this this a calculator and this can do any thing now tel me that what you want to do ")
operation = input("what do you want to do , 1 for addition , 2 for substraction, 3 for multiply , 4 for divide, 5 for calculating average  : ")
# addition function
def addition(x,y):
    return x + y
# substraction function
def substraction(x,y):
    return x * y
# multiply function
def multiply(x,y):
    return x * y
# divide function
def divide(x,y):
    return x / y

# inputting the numbers
num1 = int(input(" Please enter the first number : "))
num2 = int(input(" Please ente the second number : "))
#conditions
if operation == '1':
       print(num1,"+",num2,"=", addition(num1,num2))

elif operation == '2':
   print(num1,"-",num2,"=", substraction(num1,num2))

elif operation == '3':
   print(num1,"*",num2,"=", multiply(num1,num2))

elif operation == '4':
   print(num1,"/",num2,"=", divide(num1,num2))

elif operation == '5':
     avg1 = num1 + num2
     avg2 = (num1 + num2) / avg1
     print(num1 , " average" , num2,  " = " ,avg2)
     
    
else:
    print("hey !!!! re run the script you have to do somthing with this ")

       
    
