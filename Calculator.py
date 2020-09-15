
# Simple calculator. From line 4 - Simple version, from line 71 - hard version

# Simple version

while True:
    try:
        num1 = float(input("Enter the first digit\nOr enter 0, if your operation is unary\n"))
        sign = input("Enter the operator\n")
        num2 = float(input("Enter the second digit\n"))
    except ValueError:
        print("Something is wrong with your input\nDo you want to start again? [y/n]")
        if input() == "y":
            continue
        else:
            print("Good bye :)")
            exit()

    if num1 == 0:
        print("Your current operation is {} {} {}".format(num1, sign, num2))
        print("Are you sure that your operation is unary ? [y/n]")
        if input() == "y":
            pass
        else:
            print("Pleas, try again")
            continue

    try:
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
            raise SyntaxError

    except ArithmeticError:
        print("ERROR!!!", "I can't do this operation\nDo you want to start again? [y/n]")
        if input() == "y":
            continue
        else:
            print("Good bye :)")
            exit()

    except SyntaxError:
        print("ERROR!!!", "'{}' is an inappropriate operator\nDo you want to start again? [y/n]".format(sign))
        if input() == "y":
            continue
        else:
            print("Good bye :)")
            exit()

    else:
        if input("Do you want to start again? [y/n]\n") == "y":
            continue
        else:
            print("Good bye :)")
            exit()


# Hard version :) Something for the future to understand :)

# import re  # Gain regular expressions library
#
# while True:
#     try:
#         num1 = int(input("Enter the first digit\nOr enter 0, if your operation is unary\n"))
#         sign = input("Enter the operator\n")
#         num2 = int(input("Enter the second digit\n"))
#     except ValueError:
#         print("Something is wrong with your input\nDo you want to start again? [y/n]")
#         if input() == "y":
#             continue
#         else:
#             print("Good bye :)")
#             exit()
#
#     if num1 == 0:
#         print("Your current operation is {} {} {}".format(num1, sign, num2))
#         print("Are you sure that your operation is unary ? [y/n]")
#         if input() == "y":
#             pass
#         else:
#             print("Pleas, try again")
#             continue
#
#     try:
#         if re.match(r"[-+%*/]{1,2}", sign) and len(sign) <= 2:   # Check the operator
#             print(f"{num1} {sign} {num2} =", eval(f"{num1}{sign}{num2}"))
#             # Use special f-strings and eval function!!!
#             # In simple terms, eval() runs the python code (which is passed as an argument) within the program
#         else:
#             print("ERROR!!!", "'{}' is an inappropriate operator".format(sign))
#             if input("Do you want to start again? [y/n]\n") == "y":
#                 continue
#             else:
#                 print("Good bye :)")
#                 exit()
#
#     except SyntaxError:  # if operator begins with +,-,%,/,*, but still is not valid
#         print("ERROR!!!", "'{}' is an inappropriate operator".format(sign))
#         if input("Do you want to start again? [y/n]\n") == "y":
#             continue
#         else:
#             print("Good bye :)")
#             exit()
#
#     except ArithmeticError:  # if it is impossible
#         print("ERROR!!!", "I can't do this operation")
#         if input("Do you want to start again? [y/n]\n") == "y":
#             continue
#         else:
#             print("Good bye :)")
#             exit()
#
#     else:
#         if input("Do you want to start again? [y/n]\n") == "y":
#             continue
#         else:
#             print("Good bye :)")
#             exit()
