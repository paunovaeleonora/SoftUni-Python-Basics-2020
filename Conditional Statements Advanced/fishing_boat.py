budget = int(input())
season = input()
fishers = int(input())
ship = 0
discount = 0
price_after_discount = 0

if season == 'Spring':
    ship = 3000
elif season == 'Summer' or season == 'Autumn':
    ship = 4200
elif season == 'Winter':
    ship = 2600

if fishers <= 6:
    discount = 0.1
elif 7 <= fishers <= 11:
    discount = 0.15
elif fishers >= 12:
    discount = 0.25

price_after_discount = ship - ship * discount

if fishers % 2 == 0 and season != 'Autumn':
    price_after_discount = price_after_discount * 0.95

if budget >= price_after_discount:
    print(f'Yes! You have {(budget - price_after_discount):.2f} leva left.')
else:
    print(f'Not enough money! You need {(price_after_discount - budget):.2f} leva.')

