import sys
min_number = sys.maxsize


while True:

    number = input()
    if number != 'Stop':
        number = int(number)
        if number < min_number:
            min_number = number
    else:
        break

print(min_number)