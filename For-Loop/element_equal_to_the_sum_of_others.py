import sys
n = int(input())
max_number = -sys.maxsize
total = 0
for num in range(n):
    number = int(input())
    if number > max_number:
        max_number = number
    total += number

if max_number == (total - max_number):

    print(f'Yes')
    print(f'Sum= {total}')
else:
    print('No')
    print(f'Diff = {abs(max_number - (total - max_number))}')