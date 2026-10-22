user_num = int(input("Enter any number you want: "))

if user_num >= 1:
    print("Possitive")
elif user_num == 0:
    print("Zero")
else:
    print("Negative")

user_score = int(input("Enter your score: "))

if user_score <= 0 <= 100:
    print("Score is not correct")
elif user_score >= 90 <=100 :
    print("A")
elif user_score >=80  <= 89:
    print("B")
elif user_score >=70 <=79:
    print("C")
elif user_score >=60 <=69:
    print("D")
else:
    print("F")


enter_sec_num = int(input("Enter secret number: "))

sec_num = 9

while enter_sec_num != sec_num:
    print("Your wrong, try again")
    enter_sec_num = int(input("Enter secret number: "))
print("You guessed the number!")

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

