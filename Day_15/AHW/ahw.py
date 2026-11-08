# def ricxvi(num1):
#     sum=0
#     for i in range(0, num1):
#         for x in str(i):
#             sum+=int(x)**2
#     return sum
# print(ricxvi(21))

# print("A"*10)
# def high_and_low(numbers):
#     for i in numbers:
#         ka=numbers.sort()
#     return numbers[0][-1]
# print(nu mbers)

# scores = [88, 94, 72, 99, 53]
# srt_scores = sorted(scores, reverse = True)
# print(srt_scores)
# მოსალმების ფუნქცია

# დავალება: შექმენი ფუნქცია სახელად say_hello, რომელიც არგუმენტად მიიღებს სახელს (name) და დაბრუნებს ტექსტს: "გამარჯობა, [სახელი]!".

# მაგალითი გამოძახებისთვის: say_hello("ლუკა") უნდა აბრუნებდეს "გამარჯობა, ლუკა!".

# def say_hello(name):
#     return "Hello " + name
# print(say_hello("Avto"))
#   
# ორი რიცხვის ჯამი

# დავალება: შექმენი ფუნქცია სახელად add_numbers, რომელიც მიიღებს ორ რიცხვს (a და b) და დააბრუნებს მათ ჯამს.

# def add_numbers(a, b):
#     return a+b
# print(add_numbers(int(input("Enter 1 num: ")), int(input("Enter 2 num: "))))

# ლუწია თუ კენტი?

# დავალება: შექმენი ფუნქცია სახელად is_even, რომელიც მიიღებს ერთ მთელ რიცხვს. ფუნქციამ უნდა დააბრუნოს True, თუ რიცხვი ლუწია, და False, თუ კენტია.

# def is_even(num):
#     if num%2==0:
#         return True
#     else:
#         return False
# print(is_even(3))

# უდიდესი ორ რიცხვს შორის

# დავალება: შექმენი ფუნქცია სახელად find_max, რომელიც მიიღებს ორ რიცხვს და დააბრუნებს მათგან უფრო დიდს. (თუ ტოლია, შეგიძლია ნებისმიერი დააბრუნო).

# def finდ_max(num1,num2):
#     if num1>num2:
#         return num1
#     elif num1<num2:
#         return num2
#     else:
#         return num1

# კვადრატის პოვნა

# დავალება: შექმენი ფუნქცია square_number, რომელიც მიიღებს ერთ რიცხვს და დააბრუნებს მის კვადრატს (ანუ რიცხვი გამრავლებული თავის თავსავე).

# def square_number(num):
#     return num**2

# სიტგის შებრუნება (Reverse String)

# დავალება: შექმენი ფუნქცია სახელად reverse_string, რომელიც მიიღებს ტექსტს (სტრიქონს) და დააბრუნებს მის შებრუნებულ ვერსიას.

# მაგალითი: reverse_string("გამარჯობა") უნდა აბრუნებდეს "აბოჯრამაგ".

# def reverse_string(text):
#     return text[::-1]
# print(reverse_string("Avto"))

# სიაში უდიდესი რიცხვის პოვნა

# დავალება: შექმენი ფუნქცია სახელად find_max_in_list, 
# რომელიც არგუმენტად მიიღებს რიცხვების სიას (list) და დააბრუნებს ამ სიიდან უდიდეს რიცხვს 
# (სცადე, რომ არ გამოიყენო ჩაშენებული max() ფუნქცია და ციკლის (for) ან სხვა ლოგიკის გამოყენებით იპოვო).

# def find_max_in_list(list):
#     list.sort()
#     return list[-1]

# ხმოვანთა თვლა ტექსტში

# დავალება: შექმენი ფუნქცია სახელად count_vowels, რომელიც მიიღებს ტექსტს და
# დააბრუნებს, თუ რამდენი ხმოვანი ასო (a, e, i, o, u ან ქართული ა, ე, ი, ო, უ) არის ამ ტექსტში.

# def count_vowels(teqsti):
#     xmovnebi ="aeiou"
#     count=0
#     for i in teqsti:
#         if i in xmovnebi:
#             count+=1
#     return count

# კონკრეტული ასოს დათვლა (Count Character)

# დავალება: შექმენი ფუნქცია სახელად count_char, რომელიც მიიღებს ორ არგუმენტს:
# ტექსტს (text) და საძიებო ასოს (char). ფუნქციამ უნდა დააბრუნოს, თუ რამდენჯერ გვხვდება 
# ეს კონკრეტული ასო მოცემულ ტექსტში.

# მაგალითი გამოძახებისთვის: count_char("banana", "a") უნდა აბრუნებდეს 3-ს.

# def count_char(teqx, char):
#     count_char =0
#     for i in teqx:
#         if i == char:
#             count_char+=1
#     return count_char

# უმცირესი რიცხვის პოვნა სიაში (Find Minimum)

# დავალება: შექმენი ფუნქცია სახელად find_min_in_list, რომელიც მიიღებს რიცხვების სიას 
# (numbers) და დააბრუნებს ამ სიიდან ყველაზე პატარა რიცხვს (შეგიძლია გამოიყენო ისეთივე 
#ლოგიკა, როგორიც მაქსიმუმის პოვნისას გამოიყენე!).

# def find_min_in_list(numbers):
#     numbers.sort()
#     return numbers[0]


# მხოლოდ ლუწი რიცხვების ამოფილტრვა (Filter Evens)

# დავალება: შექმენი ფუნქცია სახელად get_evens, რომელიც მიიღებს რიცხვების სიას და დააბრუნებს ახალ სიას, რომელშიც მხოლოდ ლუწი რიცხვები დარჩება.

# მინიშნება: შეგიძლია შექმნა ცარიელი სია (new_list = []), ციკლით ჩაუყვე შემოსულ სიას, შეამოწმო if i % 2 == 0: და new_list.append(i) მეთოდით დაამატო ლუწი რიცხვები.

# def get_evens(ricli):
#     newli=[]
#     for i in ricli:
#         if i%2==0:
#             newli.append(i)
#     return newli

# პალინდრომის შემოწმება (Is Palindrome)

# დავალება: შექმენი ფუნქცია სახელად is_palindrome, რომელიც მიიღებს ერთ სიტყვას (word) 
# და დააბრუნებს True-ს, თუ ეს სიტყვა წინწმაც და უკუღმაც ერთნაირად იკითხება (მაგალითად: "radar", "level"), 
# და False-ს, თუ ასე არ არის.

# def is_palindrome(word):
#     if word==word[::-1]:
#         return True
#     else:
#         return False
                                                                                                                                            

# ყველაზე გრძელი სიტყვის პოვნა (Find Longest Word)

# დავალება: შექმენი ფუნქცია სახელად find_longest_word, რომელიც მიიღებს სიტყვების სიას (words) და დააბრუნებს ყველაზე გრძელ სიტყვას ამ სიიდან.

# მაგალითი გამოძახებისთვის: find_longest_word(["cat", "elephant", "dog"]) უნდა აბრუნებდეს "elephant"-ს.


# ეს ვერ გავიგე key არვიცოდი რა იყო და ვერც გამოყენებაში მივხვდი როგორ უნდა გამოვიყენო.
# def largest_word(words):
#     for i in words:
#         return max(words, key=len)