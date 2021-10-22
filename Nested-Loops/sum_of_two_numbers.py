start = int(input())
end = int(input())
magic_number = int(input())
counter = 0
valid = 0

for x in range(start, end + 1):
    for y in range(start, end + 1):
        if x + y == magic_number:
            print(f'Combination N:{counter} ({x} + {y} = {magic_number})')
        else:
            valid += 1


if valid == 0:
    print(f'{counter} combinations - neither equals {magic_number}')

