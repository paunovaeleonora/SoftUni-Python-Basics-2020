import sys
n = int(input())
fixed_sum = 0
min_sum = sys.maxsize
max_sum = -sys.maxsize
max_diff = -sys.maxsize
for pair in range(1, n + 1):
    sum_numbers = 0
    fixed_sum = sum_numbers
    max_diff = 0
    for numbers in range(1, 2 + 1):
        number = int(input())
        sum_numbers += number
    if sum_numbers >= max_sum:
        max_sum = sum_numbers
    if sum_numbers <= min_sum:
        min_sum = sum_numbers
    else:
        diff = max_sum - min_sum
        if diff >= max_diff:
            max_diff = diff

if min_sum == max_sum:
    print(f"Yes, value={min_sum}")
else:
    print(f"No, maxdiff={max_diff}")
