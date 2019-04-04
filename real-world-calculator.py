import re     # importing regex lib

print("our magical calculator ")
print("press 'quit' to quit \n")

previous = 0
run = True

def performmath():         # defining a function for doing math
# global variable area

    global previous              # accessing the golbal variable inside a function by "global " atribute
    global run
# assigning variables
    equation = ""  # setting the value of equation as nothing
    if previous == 0:             # this take 0 as a default vale then only this will execute
        equation = input("enter equation: ")
    else:
        equation = input(str(previous))   # if equation is not 0 then that it will be empty just as previous variable but in string
# doing the math with help of regex lib
    if equation == 'quit':               # if quuation is equal to quit
        print("goodbye , human. ")       # then print goodbye human
        run = False                      # and make the run variable as false
    else:

        equation = re.sub('[a-zA-Z,:;"(){}!@#$^&]','  ',equation)     # if not quit then  perform regex  on the input

        if previous == 0:                 # if previous is equal to 0
            previous = eval(equation)    # perform eval function on equation or on the values those have been inputed
        else:
            previous = eval(str(previous) + equation)   #if previous is not 0 then previous will be
# reloading the function again and again
while run :
    performmath()



