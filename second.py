#this script prints out the table of the desire number
import re

print("hey do you want the table of some number ")

mgk = str(input("do you want to see it Y/N : "))
if mgk == "y":
    number = input(str ("enter a number, any number you want the table of : "))
    number = re.sub('[^1-9]', "  ", number)
    number2 = number
    number3 = number2
    print("the number you have written is " , number)
    ha = 1
    # noinspection PyRedundantParentheses,PyRedundantParentheses
    while (ha <= 20):
        print (number2 , "*" , ha , " = " , number)
        number = number + number3
        ha = ha + 1
else:
    print('there is not magic trick for you ')
