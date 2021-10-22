sum_not_prime = 0
sum_prime = 0
while True:
    number = input()
    if number == 'stop':
        break
    else:
        number = int(number)
        if number > 1:
            count = 0
            for i in range(2, number):
                if number % i == 0:
                    count += 1
            if not count == 0:
                sum_not_prime += number
            else:
                sum_prime += number
        elif number == 0:
            pass
        elif number < 0:
            print(f'Number is negative.')
print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_not_prime}')
