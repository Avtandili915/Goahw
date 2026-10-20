
for i in range(1, 21):
    print(i)

for l in range(1, 50, 2):
    print(l)

start = 0

for j in range(1, 101):
    start += j
    print(start)

user_whole_num = int(input("Enter whole number: "))

for k in range(1, 11):
    result = user_whole_num * k
    print(user_whole_num, "x", k, "=", result)

car_for_sell = 5

while car_for_sell > 0:
    print("Car For Sale")
    car_for_sell = car_for_sell - 1