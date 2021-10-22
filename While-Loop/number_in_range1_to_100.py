number = int(input())

while not (1 <= number <= 100):  # simple while (while like if)
    print('Invalid number')
    number = int(input())

print(f'The number is: {number}')  # this is out of the while loop body
