n = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p1 = 0
p2 = 0
p3 = 0

for number in range(1, n + 1):
    number = int(input())
    if number % 2 == 0:
        p1_count += 1
        p1 = p1_count / n * 100
    if number % 3 == 0:
        p2_count += 1
        p2 = p2_count / n * 100
    if number % 4 == 0:
        p3_count += 1
        p3 = p3_count / n * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')