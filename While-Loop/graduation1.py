name = input()
grade = 1
result = 0
score_counter = 0
while grade <= 12:
    score = float(input())
    if score >= 4:
        result += score
        grade += 1
    elif score < 4:
        score_counter += 1
        if score_counter >= 2:
            print(f'{name} has been excluded at {grade} grade')
            break

average_score = result / 12
if score_counter < 2:
    print(f'{name} graduated. Average grade: {average_score:.2f}')
