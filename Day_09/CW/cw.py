
name = "Avtandili"

i=0
while i < 5:
    print(name)
    i += 1
    

total_sum = 0
number = 0

while number <= 10:
    total_sum += number
    number += 1

print(total_sum)


user_num = int(input("Enter the number: "))

total_sum2 = 0
current = 0

while current <= user_num:
    total_sum2 += current
    current += 2

print(total_sum2)


saved_password = "Avtandili2009"

password_input = input("Enter password: ")

while password_input != saved_password:
    password_input = input("Wrong password! Try again: ")

print("Correct your in")


age = int(input("Enter your age: "))

if age > 18:
    print("You are adult!")
else:
    print("You are not adult!")


number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Your number is even!")
else:
    print("Your number is odd!")


num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Largest number is:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Largest number is:", num2)
else:
    print("Largest number is:", num3)