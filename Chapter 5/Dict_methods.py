marks = {
    "Ram" : 88,
    "Shyam" : 92,
    "Raj" : 85,
    0 : "Hariom"
}
# print(marks.items())
# print(marks.keys())
# print(marks.values())

# marks.update({"Ram" : 89})
# print(marks)

# both output are same than whats the difference between them
print(marks.get("Ram"))
print(marks["Om"])

# the difference is .get returns None and [] gives error if the key is not found. 
print(marks.get("Om"))
print(marks["Om"])