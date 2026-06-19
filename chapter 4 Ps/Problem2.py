students = []

s1 = int(input("Enter marks of student 1: "))
students.append(s1)
s2 = int(input("Enter marks of student 2: "))
students.append(s2)
s3 = int(input("Enter marks of student 3: "))
students.append(s3)
s4 = int(input("Enter marks of student 4: "))
students.append(s4)
s5 = int(input("Enter marks of student 5: "))
students.append(s5)
s6 =int(input("Enter marks of student 6: "))
students.append(s6)

sorted_students = sorted(students)
print("Marks of students are: ", sorted_students)