user_num1 = float(input("Enter First number: "))
user_num2 = float(input("Enter Second number: "))
operatori = input("Enter operatori (+, -, *, /))")

if operatori == "+":
    print(user_num1 + user_num2)
elif operatori == "-":
    print(user_num1 - user_num2)

elif operatori == "*":
    print(user_num2 * user_num1)

elif operatori == "/":
    if user_num2 != 0:
        print(user_num1 / user_num2)
    else:
        print("Error")
else:
    print("Incorrect operatori")
