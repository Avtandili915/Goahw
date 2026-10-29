# 🧩 TASK 01 — AGE CHECKER
# ⭐ Difficulty: 1/5 | 🟢 EASY

# 📌 Your Mission:

# Create a program that asks the user to enter their age.

# Convert the entered age into an integer and determine their age category.

# 📋 Requirements:
# 👶 Under 13 → Print Child
# 🧑 Between 13 and 17 → Print Teenager
# 👨 18 or older → Print Adult

# 💻 Example:
# Enter your age: 16
# You are a Teenager!


# 🛠️ Concepts: input(), int(), if / elif / else


# user_age = int(input("Enter your age: "))

# if user_age < 13:
#     print("Child")
# elif user_age <17:
#     print("Teenager")
# else:
#     print("Adult")


# 🧩 TASK 02 — EVEN OR ODD?
# ⭐ Difficulty: 1/5 | 🟢 EASY

# 📌 Your Mission:

# Ask the user to enter a positive integer N.

# Use a for loop to check every number from 1 to N and determine whether it is even or odd.

# 📋 Requirements:
# 🔢 Ask the user for a positive integer.
# 🔁 Use a for loop.
# ✅ Print Even for even numbers.
# ❌ Print Odd for odd numbers.

# 💻 Example:
# Enter a number: 5

# 1 - Odd
# 2 - Even
# 3 - Odd
# 4 - Even
# 5 - Odd


# 🛠️ Concepts: input(), int(), for, if / else, %


# user_post = int(input("Enter possitive number :"))

# for i in range(1, user_post + 1):
#     if i%2==0:
#         print(i, "-Even")
#     else:
#         print(i, "-Odd")


# 🧩 TASK 03 — PASSWORD SECURITY
# ⭐⭐ Difficulty: 2/5 | 🟢 EASY

# 📌 Your Mission:

# Create a password verification system.

# The correct password is python123.

# The program must keep asking for a password until the user enters the correct one.

# 📋 Requirements:
# 🔐 Ask the user to enter a password.
# 🔁 Use a while loop to repeat the question.
# ❌ Incorrect password → Print Try again!
# ✅ Correct password → Print Access granted!
# 🛑 Stop the loop when the password is correct.

# 💻 Example:
# Enter password: hello
# ❌ Try again!

# Enter password: 12345
# ❌ Try again!

# Enter password: python123
# ✅ Access granted!


# 🛠️ Concepts: input(), while, if / else, strings



# correct_password = "python123"
# user_password = input("Enter your password: ")

# if user_password == correct_password:
#     print("Your Wrong,Try again!")
#     user_password = input("Enter your password: ")

# print("Access granted!")


# Additional Task:

# correct_password = "python123"
# input_password = ""
# wrong_try = 0

# while input_password != correct_password and wrong_try != 3:
#     input_password = input("Please enter correct password: ")

#     if input_password == correct_password:
#         print("✅ Access granted!")
#     else:
#         wrong_try += 1
#         print("❌ Try again!")
#     if wrong_try == 3:
#         print("Ur not him/her")


# თქვენი დავალებაა დაითალოთ რამდენჯერ შეეშალა მომხმარებელს პაროლი და თუ შეცდომების რაოდენობა გაუტოლდება 3 უნდა შეწყვიტოთ პროგრამა.


# დავალება 2 — PIN კოდი 📱
# სწორი PIN კოდია "2580".
# - მომხმარებელს მოსთხოვე PIN კოდის შეყვანა.
# - დაითვალე რამდენჯერ შეეშალა.
# - 3 არასწორი მცდელობის შემდეგ დაბეჭდე "Card blocked!".
# - სწორი კოდის შეყვანისას დაბეჭდე "Welcome!".


# pin_code = 5462
# user_pin = int(input("Enter your Pin code: "))
# attemp = 0

# while user_pin != pin_code:
#     user_pin = int(input("Enter your Pin code: "))

#     if user_pin == pin_code:
#         print("Welcome!")
#     else:
#         print("Card Blocked!")


# დავალება 3 — გამოცნობის თამაში 🎯
# პროგრამაში ჩაფიქრებული რიცხვია 7.
# - მომხმარებელმა უნდა გამოიცნოს რიცხვი.
# - ყოველი არასწორი პასუხის შემდეგ დაბეჭდე "Wrong guess!".
# - დაითვალე მცდელობები.
# - თუ მომხმარებელი სწორად გამოიცნობს, დაბეჭდე "You won!".


# program_num = 7
# user_num = int(input("Enter secret num: "))
# mcdeloba = 0

# while program_num != user_num:
#     mcdeloba+=1
#     print("Wrong guess!")
#     user_num = int(input("Enter secret num: "))

#     if program_num == user_num:
#         print("You won!")
#         print(mcdeloba)



# 🟡 TASK 04 — STUDENT GRADE CALCULATOR
# ⭐⭐⭐ Difficulty: 3/5 | 🟡 MEDIUM

# 📌 Your Mission:

# Create a program that calculates student grades.

# First, ask the user how many students are in the classroom.

# Then use a for loop to ask for each student's score.

# 📋 Requirements:
# 🔢 Ask how many students there are.
# 🔁 Use a for loop to enter each student's score.
# 📊 Convert each score into a grade.
# ❌ Scores must be between 0 and 100.
# ✅ Count how many students passed (60 or higher).
# 📢 Display the total number of students who passed and failed.

# 🎓 Grading System:
# 90–100 → A
# 80–89  → B
# 70–79  → C
# 60–69  → D
# 0–59   → F


# 💻 Example:
# How many students? 3

# Student 1 score: 95
# Grade: A

# Student 2 score: 72
# Grade: C

# Student 3 score: 45
# Grade: F

# Total passed: 2
# Total failed: 1


# 🛠️ Concepts: input(), int(), for, if / elif / else, counters


# student = int(input("Enter how many student you have: "))

# passed = 0
# faild =0

# for i in range(1, student + 1):
#     score = int(input(f"Student {i} score: "))

#     while score < 0 or score > 100:
#         print("გილოცავ შენ მონაწილე ხარ!")
#         score = int(input("Student score: "))

#     if score >= 90:
#         print("A")
#     elif score >=80 <=89:
#         print("B")
#     elif score >=70 <=79:
#             print("C")
#     elif score >=60 <=69:
#             print("D")
#     else:
#          print("F")

#     if score >= 60:
#          passed+=1
#     else:
#          faild+=1

# print("სულ ჩააბარა :", passed)
# print("ჩაიჭრა :", faild)


# 🟡 TASK 05 — ATM WITHDRAWAL SYSTEM
# ⭐⭐⭐ Difficulty: 3/5 | 🟡 MEDIUM

# 📌 Your Mission:

# Create a simple ATM simulator that allows users to withdraw money from their bank account.

# 💰 Starting Balance: 500 GEL

# 📋 Requirements:
# 🔁 Use a while loop to keep asking for withdrawal amounts.
# 💵 Convert the entered amount into a float.
# ❌ If the amount is greater than the balance, print Insufficient funds!
# ⚠️ If the amount is negative, print Invalid amount!
# 🛑 If the amount is zero, stop the program.
# ✅ Otherwise, subtract the amount from the balance.
# 📊 Display the remaining balance after each successful withdrawal.

# 💻 Example:
# ====== ATM SYSTEM ======
# Current Balance: 500 GEL

# Enter withdrawal amount: 100
# Withdrawal successful!
# Remaining Balance: 400 GEL

# Enter withdrawal amount: 450
# Insufficient funds!

# Enter withdrawal amount: -20
# Invalid amount!

# Enter withdrawal amount: 150
# Withdrawal successful!
# Remaining Balance: 250 GEL

# Enter withdrawal amount: 0
# ATM session ended.


# 🛠️ Concepts: input(), float(), while, if / elif / else, arithmetic


starting_balance = 500

while starting_balance != 0:
    print(starting_balance)
    gamotanili_tanxa = float(input("Enter how much money do u have? "))

    if gamotanili_tanxa < 0:
        print("არასწორი რაოდენობა!")
    elif gamotanili_tanxa ==0:
        print("საბანკო ოპერაცია დასრულებულია!")
        break
    elif gamotanili_tanxa > starting_balance:
        print("ბევრი მოგივიდა.")
    else:
        starting_balance -= gamotanili_tanxa
        print("გამოტანა შერულებულია!")

