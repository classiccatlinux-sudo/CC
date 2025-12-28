#CC - classic calculator

from CASIC import *

used()
wait(3)
clear()
print("Welcome to CC - classic calculator")
wait(2)
clear()

a = float(input("enter first number: "))

b = float(input("enter second number: "))

operation = input("enter operation (+, -, x,): ")
clear()

if operation == "+":
    result = a + b
    print("the result is:", result)
elif operation ==  "-":
    result = a - b
    print("the result is:", result)
elif operation == "x":
    result = a * b
    print("the result is:", result)
else:
    print("invalid operation")

wait(5)   

clear()

#note this will not work in most IDEs/code editers.
return_to_menu = input("do you want to return to the main menu? (y/n): ");
if return_to_menu == "y":
    clear()
    os.system('rm -rf __pycache__') 
    wait(.1)
    os.system('python3 main.py') 
    clear()
else:
    used()
    wait(2)
    clear()




