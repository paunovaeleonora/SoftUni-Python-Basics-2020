students = int(input())
sum_grade = 0
average_grade = 0
students_1 = 0
students_2 = 0
students_3 = 0
students_4 = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
for students in range(1, students + 1):
    grade = float(input())
    sum_grade += grade
    average_grade = sum_grade / students

    if 5.00 <= grade <= 6.00:
        students_1 += 1
    elif 4.00 <= grade <= 4.99:
        students_2 += 1
    elif 3.00 <= grade <= 3.99:
        students_3 += 1
    elif grade < 3.00:
        students_4 += 1
p1 = students_1 / students * 100
p2 = students_2 / students * 100
p3 = students_3 / students * 100
p4 = students_4 / students * 100

print(f'Top students: {p1:.2f}%')
print(f'Between 4.00 and 4.99: {p2:.2f}%')
print(f'Between 3.00 and 3.99: {p3:.2f}%')
print(f'Fail: {p4:.2f}%')
print(f'Average: {average_grade:.2f}')