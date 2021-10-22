goal = 10000

sum_steps = 0
not_going_home = True

while sum_steps < goal and not_going_home:
    steps = input()

    if steps == 'Going home':
        not_going_home = False
        break
    sum_steps += int(steps)

if not_going_home:
    if sum_steps >= goal:
        print(f'Goal reached! Good job!')
        print(f'{sum_steps - goal} steps over the goal!')
    else:
        print(f'{goal - sum_steps} more steps to reach goal.')


if not not_going_home:
    steps = input()
    sum_steps += int(steps)
    if sum_steps >= goal:
        print(f'Goal reached! Good job!')
        print(f'{sum_steps - goal} steps over the goal!')
    else:
        print(f'{goal - sum_steps} more steps to reach goal.')
