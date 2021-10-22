n = int(input())
sum_odd = 0
sum_even = 0
number = 0
for position in range(1, n + 1):
    current_number = int(input())

    if position % 2 == 0:
        sum_even += current_number
    else:
        sum_odd += current_number

if sum_odd == sum_even:
    print(f'Yes')
    print(f'Sum = {sum_odd}')
else:
    print('No')
    print(f'Diff = {abs(sum_even - sum_odd)}')
