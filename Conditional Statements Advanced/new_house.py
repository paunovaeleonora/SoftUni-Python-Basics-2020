flower_type = input()
flower_count = int(input())
budget = int(input())

total_price = 0

if flower_type == 'Roses':

    if flower_count > 80:
        total_price = flower_count * 5 * 0.9
    else:
        total_price = flower_count * 5
elif flower_type == 'Dahlias':

    if flower_count > 90:
        total_price = flower_count * 3.8 * 0.85
    else:
        total_price = flower_count * 3.8
elif flower_type == 'Tulips':

    if flower_count > 80:
        total_price = flower_count * 2.8 * 0.85
    else:
        total_price = flower_count * 2.8
elif flower_type == 'Narcissus':

    if flower_count < 120:
        total_price = flower_count * 3 * 1.15
    else:
        total_price = flower_count * 3
elif flower_type == 'Gladiolus':

    if flower_count < 80:
        total_price = flower_count * 2.5 * 1.2
    else:
        total_price = flower_count * 2.5

if budget >= total_price:
    print(f'Hey, you have a great garden with {flower_count} {flower_type} and {(budget - total_price):.2f} leva left.')
else:
    print(f'Not enough money, you need {(total_price - budget):.2f} leva more.')





