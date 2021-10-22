budget = float(input())
season = input()
destination = 0
building = 0
price = 0
if budget <= 100:
    destination = 'Bulgaria'
    if season == 'summer':
        price = budget * 0.3
    elif season == 'winter':
        price = budget * 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        price = budget * 0.4
    elif season == 'winter':
        price = budget * 0.8
else:
    destination = 'Europe'
    price = budget * 0.9

if season == 'summer' and destination != 'Europe':
    building = 'Camp'
elif season == 'winter':
    building = 'Hotel'
if destination == 'Europe':
    building = 'Hotel'
print(f'Somewhere in {destination}')
print(f'{building} - {price:.2f}')

