import sys
n = int(input())
odd_sum = 0
even_sum = 0
odd_min = True
odd_max = True
even_min = True
even_max = True
max_num = -sys.maxsize
min_num = sys.maxsize
for position in range(1, n + 1):
    number = float(input())

    if not position % 2 == 0:
        odd_sum += number
        print(f'OddSum={odd_sum:.2f},')
        if not odd_min:
            if number < min_num:
                min_num = odd_min
                odd_min = number
                print(f'OddMin={odd_min:.2f},')
        else:
            print('No,')
        if not odd_max:
            if number > max_num:
                max_num = odd_max
                odd_max = number
                print(f'OddMax={odd_max:.2f},')

        else:
            print('No,')

    else:
        even_sum += number
        print(f'EvenSum={even_sum:.2f},')

        if not even_min:

            if number < min_num:
                min_num = even_min
                even_min = number
                print(f'EvenMin={even_min:.2f},')
            else:
                print('No')
        if not odd_max:
            if number > max_num:
                max_num = even_max
                even_max = number
                print(f'EvenMax={even_max:.2f}')
            else:
                print('NO')
if odd_min == float:
    odd_min = round(odd_min, 2)
if odd_max == float:
    odd_max = round(odd_max, 2)
if even_min == float:
    even_min = round(even_min, 2)
if even_max == float:
    even_max = round(even_max, 2)

print(f'OddSum={odd_sum:.2f},')
print(f'OddMin={odd_min},')
print(f'OddMax={odd_max},')
print(f'EvenSum={even_sum:.2f},')
print(f'EvenMin={even_min},')
print(f'EvenMax={even_max}')






