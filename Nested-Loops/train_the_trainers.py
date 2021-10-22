n = int(input())
presentation_count = 0
total_grade = 0
while True:
    presentation = input()
    if presentation == 'Finish':
        break
    presentation_count += 1
    grades_sum = 0
    for grades in range(1, n + 1):
        grade = float(input())
        grades_sum += grade
    average_grade = grades_sum / n
    total_grade += average_grade
    print(f'{presentation} - {average_grade:.2f}.')


print(f"Student's final assessment is {(total_grade / presentation_count):.2f}.")


