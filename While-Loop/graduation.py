name = input()
grade = 1
result = 0
while True:
    score = float(input())

    if score >= 4:
        result += score
        grade += 1

    if grade > 12:
        break

average_score = result / 12
print(f'{name} graduated. Average grade: {average_score:.2f}')
