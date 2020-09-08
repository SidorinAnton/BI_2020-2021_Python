
# Simple calculator. From line 4 - Simple version, from line 27 - hard version

# Simple version
num1 = int(input("Enter the first digit\nOr enter 0, if your operation is unary\n"))
sign = input("Enter the operator\n")
num2 = int(input("Enter the second digit\n"))

if num1 == 0:
    print("Your current operation is {} {} {}".format(num1, sign, num2))
    print("Are you shure that your operation is unary ? [y/n]")
    if input() == "y":
        pass
    else:
        print("Pleas, try again")
        exit()

if num2 == 0 and ("/" in sign or "%" in sign):
    print("ERROR!!!\n", "I can't do this operation")
    exit()

if sign == "+":
    print("{0} + {1} =".format(num1, num2), num1 + num2)
elif sign == "-":
    print("{0} - {1} =".format(num1, num2), num1 - num2)
elif sign == "*":
    print("{0} * {1} =".format(num1, num2), num1 * num2)
elif sign == "**":
    print("{0} ** {1} =".format(num1, num2), num1 ** num2)
elif sign == "/":
    print("{0} / {1} =".format(num1, num2), num1 / num2)
elif sign == "//":
    print("{0} // {1} =".format(num1, num2), num1 // num2)
elif sign == "%":
    print("{0} % {1} =".format(num1, num2), num1 % num2)
else:
    print("ERROR!!!\n", "{} is an inappropriate operator".format(sign))


# Hard version :) Something for the future to understand :)
'''
import re  # Gain regular expressions library

num1 = int(input("Enter the first digit\nOr enter 0, if your operation is unary\n"))
sign = input("Enter the operator\n")
num2 = int(input("Enter the second digit\n"))

try:
    if re.match(r"[-+%*/]{1,2}", sign) and len(sign) <= 2:   # Check the operator
        print(f"{num1} {sign} {num2} =", eval(f"{num1}{sign}{num2}"))  # Use special f-strings and eval function!!!
        # In simple terms, eval() runs the python code (which is passed as an argument) within the program
    else:
        print("ERROR!!!\n", "{} is an inappropriate operator".format(sign))
except SyntaxError:  # if operator begins with +,-,%,/,*, but still is not valid
    print("ERROR!!!\n", "{} is an inappropriate operator".format(sign)) 
except ArithmeticError:  # if it is impossible 
    print("ERROR!!!\n", "I can't do this operation")
'''