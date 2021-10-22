days = int(input())
food = float(input())
sum_dog = 0
sum_cat = 0

biscuits = 0
sum_biscuits = 0
total_eaten = 0
total_eaten_food_percent = 0
dog_percent = 0
cat_percent = 0
for days in range(1, days + 1):
    dog = int(input())
    cat = int(input())
    if days % 3 == 0:
        biscuits = (cat + dog) * 0.1
    sum_dog += dog
    sum_cat += cat
    sum_biscuits += biscuits
total_eaten = sum_cat + sum_dog

total_eaten_food_percent = total_eaten / food * 100
dog_percent = sum_dog / total_eaten * 100
cat_percent = sum_cat / total_eaten * 100

print(f'Total eaten biscuits: {round(sum_biscuits)}gr.')
print(f'{total_eaten_food_percent:.2f}% of the food has been eaten.')
print(f'{dog_percent:.2f}% eaten from the dog.')
print(f'{cat_percent:.2f}% eaten from the cat.')
