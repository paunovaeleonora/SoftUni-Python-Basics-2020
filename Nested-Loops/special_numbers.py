n = int(input())
for number in range(1111, 10000):
    count = 0
    for digit in str(number):
        digit = int(digit)
        if digit == 0:
            break
        if n % digit == 0:
            count += 1
    if count == 4:
        print(f"{number}", end=" ")
