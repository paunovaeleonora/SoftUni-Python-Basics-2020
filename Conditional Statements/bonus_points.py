bonus_points = 0
number = int(input())

if number > 1000:
    bonus_points += number * 0.1
elif number > 100:
    bonus_points += number * 0.2
else:
    bonus_points += 5

if number % 2 == 0:
    bonus_points += 1
elif number % 5 == 0:
    bonus_points += 2

print(bonus_points)
print(number + bonus_points)