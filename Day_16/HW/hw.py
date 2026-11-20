# def check_number(num):
#     if num>0:
#         return "Positive"
#     elif num<0:
#         return "Negative"
#     else:
#         return "Zero"


# print(check_number(int(input("Enter ur num: "))))


# def calculate_sum(numbers):
#     sum = 0
#     for i in range(1, numbers+1):
#         sum+=i
#     return(sum)
# print(calculate_sum(int(input("Enter ur num: "))))


# def calculator(num1,num2,math_opr):
#     if math_opr=="+":
#         return num1+num2
#     elif math_opr=="-":
#         return num1-num2
#     elif math_opr=="*":
#         return num1*num2
#     else:
#         return num1/num2

# num1 = int(input("Enter ur number 1: "))
# num2 = int(input("Enter ur number 2: "))
# math_opr = input("Enter operation (+, -, *, /): ")
# print(calculator(num1,num2,math_opr))


def password_checker(password):
    aso = 0
    ricxvi = 0
    simbolo = 0
    len(password)
    for i in password:
        if len(password)>8:
            len(password)==True
        else:
            len(password)==False
    for i in password:
        if i.upper()!=i.lower():
            aso+=1
    for i in password:
        if i.upper()==i.lower():
            ricxvi+=1
    return len(password)>8 and ricxvi>1 and aso>1
    
print(password_checker(input("Enter your password: ")))


# - პაროლის სიგრძე 8 სიმბოლოზე მეტია.
# - პაროლში არის მინიმუმ 1 ასო.
# - პაროლში არის მინიმუმ 1 რიცხვი.