fruit = input()
day = input()
quantity = float(input())
weekday = day =='Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday'
weekend = day == 'Saturday' or day == 'Sunday'
product = fruit == 'banana' or fruit == 'apple' or fruit == 'orange' or fruit == 'grapefruit' or fruit == 'kiwi' or fruit == 'pineapple' or fruit == 'grapes'
sales = 0


if weekday and product:
    if fruit == 'banana':
        sales = 2.50 * quantity
    if fruit == 'apple':
        sales = 1.20 * quantity
    if fruit == 'orange':
        sales = 0.85 * quantity
    if fruit == 'grapefruit':
        sales = 1.45 * quantity
    if fruit == 'kiwi':
        sales = 2.70 * quantity
    if fruit == 'pineapple':
        sales = 5.50 * quantity
    if fruit == 'grapes':
        sales = 3.85 * quantity
    print(f"{sales:.2f}")
elif weekend and product:
    if fruit == 'banana':
        sales = 2.70 * quantity
    if fruit == 'apple':
        sales = 1.25 * quantity
    if fruit == 'orange':
        sales = 0.90 * quantity
    if fruit == 'grapefruit':
        sales = 1.60 * quantity
    if fruit == 'kiwi':
        sales = 3.00 * quantity
    if fruit == 'pineapple':
        sales = 5.60 * quantity
    if fruit == 'grapes':
        sales = 4.20 * quantity
    print(f"{sales:.2f}")
else:
        print('error')