groups = int(input())

people_1 = 0
people_2 = 0
people_3 = 0
people_4 = 0
people_5 = 0

sum_people = 0
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for people in range(1, groups + 1):
    number_of_people = int(input())
    if 1 <= number_of_people <= 5:
        people_1 += number_of_people
    elif 6 <= number_of_people <= 12:
        people_2 += number_of_people

    elif 13 <= number_of_people <= 25:
        people_3 += number_of_people

    elif 26 <= number_of_people <= 40:
        people_4 += number_of_people

    if number_of_people >= 41:

        people_5 += number_of_people
    sum_people += number_of_people
p1 = people_1 / sum_people * 100
p2 = people_2 / sum_people * 100
p3 = people_3 / sum_people * 100
p4 = people_4 / sum_people * 100
p5 = people_5 / sum_people * 100

print(f'{p1:.2f}%')
print(f'{p2:.2f}%')
print(f'{p3:.2f}%')
print(f'{p4:.2f}%')
print(f'{p5:.2f}%')