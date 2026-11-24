person = {
    "name": "Avto",
    "age": 17,
    "profession": "IT Specialist",
    "city": "Abasha",
    "hobby": "Football"
}

print("Entire Object:")
print(person)

print("\nOnly Keys:")
for key in person.keys():
    print(key)

print("\nOnly Values:")
for value in person.values():
    print(value)


print("\nKeys and Values (.items()):")
for key, value in person.items():
    print(f"{key}: {value}")



book = {
    "title": "",
    "author": "Shota Rustaveli",
    "year": 1200,
    "genre": "poema",
    "pages": 99999999999
}


book["year"] = 1250
book["pages"] = 320


book["language"] = "Georgian"
book["price"] = 25.99

del book["genre"]

print("Final Book Object:")
for key, value in book.items():
    print(f"{key}: {value}")