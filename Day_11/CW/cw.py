# 🟡 TASK 06 — SMART MULTIPLICATION TABLE
# ⭐⭐⭐ Difficulty: 3/5 | 🟡 MEDIUM

# 📌 Your Mission:

# Create a multiplication table generator that also checks whether each result is divisible by 3.

# 📋 Requirements:
# 🔢 Ask the user to enter a positive integer.
# 🔁 Use a for loop to multiply the number by 1 through 10.
# 🧮 Calculate each multiplication result.
# ✅ If the result is divisible by 3, print Divisible by 3.
# ❌ Otherwise, print Not divisible by 3.
# 📊 At the end, display how many results were divisible by 3.

# 💻 Example:
# Enter a number: 2

# 2 x 1 = 2   | Not divisible by 3
# 2 x 2 = 4   | Not divisible by 3
# 2 x 3 = 6   | Divisible by 3
# 2 x 4 = 8   | Not divisible by 3
# 2 x 5 = 10  | Not divisible by 3
# 2 x 6 = 12  | Divisible by 3
# 2 x 7 = 14  | Not divisible by 3
# 2 x 8 = 16  | Not divisible by 3
# 2 x 9 = 18  | Divisible by 3
# 2 x 10 = 20 | Not divisible by 3

# Total divisible by 3: 3


# 🛠️ Concepts: input(), int(), for, if / else, %, counters

# possitive_integer = int(input("Enter whole number: "))

# count =0


# for k in range(1, 11,):
#     result = possitive_integer * k
#     print(possitive_integer, "x", k, "=", result)


#     if possitive_integer%3==0:
#         print(result, "|  Divisible by 3")
#         count += 1
        
#     else:
#         print(result, "|  Not divisible by 3")
                

# print("Total divisible by 3: ", count)






# 🔴 TASK 09 — BANKING MANAGEMENT SYSTEM
# ⭐⭐⭐⭐ Difficulty: 4/5 | 🔴 HARD

# 📌 Your Mission:

# Create an interactive banking program where users can manage their bank account, deposit money, withdraw money, and view transaction statistics.

# 💰 Starting Balance: 1,000 GEL

# 📱 MAIN MENU
# ====== BANK SYSTEM ======
# 1. Check Balance
# 2. Deposit Money
# 3. Withdraw Money
# 4. Transaction Summary
# 5. Exit
# =========================


# 📋 REQUIREMENTS
# 💳 OPTION 1 — CHECK BALANCE
# Display the user's current account balance.

# 💵 OPTION 2 — DEPOSIT MONEY
# Ask how much money the user wants to deposit.
# Convert the amount into float.
# Reject zero or negative amounts.
# Add valid deposits to the current balance.
# Count successful deposits.

# 🏧 OPTION 3 — WITHDRAW MONEY
# Ask how much money the user wants to withdraw.
# Reject zero or negative amounts.
# Reject withdrawals exceeding the available balance.
# Subtract valid withdrawals from the balance.
# Count successful withdrawals.

# 📊 OPTION 4 — TRANSACTION SUMMARY

# Display:
# 💰 Current account balance
# 📥 Total number of deposits
# 📤 Total number of withdrawals
# 💵 Total money deposited
# 💸 Total money withdrawn

# 🚪 OPTION 5 — EXIT
# Print a goodbye message.
# Stop the program.

# ⚠️ ADDITIONAL RULES
# 🔁 Use a while loop to keep the menu running.
# 🔢 Use int() for menu selection and float() for money amounts.
# ❌ Reject invalid menu options.
# ❌ Reject negative or zero transaction amounts.
# ❌ Never allow the balance to become negative.
# ✅ After every operation, return to the main menu.
# 🛑 Exit only when option 5 is selected.

# 🛠️ Concepts: input(), int(), float(), while, if / elif / else, counters, arithmetic, validation


balance = 1000
shetana = 0
gamotana = 0
jamshi_gatana = 0
jamhi_depoziti = 0

while True:
    print("📱 MAIN MENU")
    print("====== BANK SYSTEM ======")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction Summary")
    print("5. Exit")
    print("=========================")

    airchie = int(input("Choce a number"))

    if airchie == 1:
        print(f"Current Balance: {balance} GEL")
    elif airchie ==2:
        tanxa = float(input("Enter how much deposite u want: "))
        if tanxa <=0:
            print("0-s angarishze ver sheitan!")
        else:
            balance+=tanxa
            shetana+=1
            jamhi_depoziti+=tanxa
            print("Tanxa damatebulia")
    elif airchie ==3:
        tanxa = float(input("Enter how much Withdraw u want: "))
        if tanxa <=0:
            print("0-s ver gamoitan!")
        else:
            balance-=tanxa
            gatana+=1
            jamshi_gatana+=tanxa
            print("Gatana warmatebit ganxorcielda.")
    elif airchie ==4:
        print("=======Transaction Summary=======")
        print(f"Axlandeli balansia {balance} GEL")
        print(f"Sul shemotanili tanxa {jamhi_depoziti} GEL")
        print(f"Jamshi gatanili {jamshi_gatana} GEL")
        print("===================================")
    elif airchie ==5:
        print("Gmadlobt rom sargeblobt cveni apit<3")
        break
    else:
        print("Shen aircie araswori cifri!")
        break