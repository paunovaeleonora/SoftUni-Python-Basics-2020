failed_treshold = int(input())

solved_problems = 0
counter_bad_grades = 0
sum_score = 0
last_problem = ' '
failed_times = 0
has_failed = True

while failed_times < failed_treshold:
    problem_name = input()
    if problem_name == 'Enough':
        has_failed = False
        break
    grade = int(input())
    if grade <= 4:
        failed_times += 1
    sum_score += grade
    solved_problems += 1
    last_problem = problem_name
if has_failed:
    print(f'You need a break, {failed_treshold} poor grades.')
else:
    print(f'Average score: {sum_score / solved_problems:.2f}')
    print(f'Number of problems: {solved_problems}')
    print(f'Last problem: {last_problem}')