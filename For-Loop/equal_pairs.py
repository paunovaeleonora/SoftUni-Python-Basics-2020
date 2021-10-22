
n = int(input())
previous_sum = 0
max_diff = 0


for couple in range(1, n + 1):
    current_sum = 0
    number1 = int(input())
    number2 = int(input())
    current_sum = number1 + number2
    diff = abs(previous_sum - current_sum)
    if couple == 1:
        previous_sum = current_sum
        max_diff = 0
        continue
    if diff == 0:
        max_diff = 0
    if diff > max_diff:
        max_diff = diff

    previous_sum = current_sum

if max_diff == 0:
    print(f'Yes, value={previous_sum}')
else:
    print(f'No, maxdiff={max_diff}')


