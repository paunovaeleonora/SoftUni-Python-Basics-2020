number1 = int(input())
number2 = int(input())

for number in range(number1, number2 + 1):
    number_to_str = str(number)
    sum_even_position = 0
    sum_odd_position = 0
    for index, digit in enumerate(number_to_str):
        if index % 2 == 0:
            sum_even_position += int(digit)
        else:
            sum_odd_position += int(digit)
    if sum_even_position == sum_odd_position:
        print(f'{number}', end=' ')