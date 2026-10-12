name = input("Whats your name")
age = input("Whats your age")
haight = input("Whats your haight")

print(name)
print(int(age))
print(haight)

num_1 = int(input("Name one number"))
num_2 = int(input("Name other number"))

print(num_1 + num_2)
print(num_1 - num_2)
print(num_1 * num_2)
print(num_1 / num_2)
print(num_1 // num_2)
print(num_1 % num_2)

fruit = input("Which product do you want")
price = float(input("Enter the product price"))
how_many = int(input("How many product do you want"))

print(fruit)
print(price)
print(price * how_many) 

User_name = input("Please enter yout name")
User_grade_in_English = int(input("Please enter your Enlish grade"))
User_grade_in_History = int(input("Please enter your History grade"))
User_grade_in_Geography = int(input("Please enter your Geography grade"))
print(User_grade_in_English + User_grade_in_Geography + User_grade_in_History)
User_average_grades = int(input("Enter the total number for all three of your subjects"))

print(User_name)
print("Your English grade is" + " " + str(User_grade_in_English))
print("Your History grade is" + " " + str(User_grade_in_History))
print("Your Geography grade is" + " " + str(User_grade_in_Geography))
print("Your average grade is" + " " + str(User_average_grades // 3))

