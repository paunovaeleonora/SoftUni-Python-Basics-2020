month = input()
nights = int(input())

price_studio = 0
price_apart = 0
studio = 0
apartment = 0


if month == 'May' or month == 'October':
    price_studio = 50
    price_apart = 65
    if nights > 14:
        studio = price_studio * nights * 0.7
        apartment = price_apart * nights * 0.9
    elif nights <= 7:
        studio = price_studio * nights
        apartment = price_apart * nights
    elif nights > 7:
        studio = price_studio * nights * 0.95
        apartment = price_apart * nights

elif month == 'June' or month == 'September':
    price_studio = 75.20
    price_apart = 68.70
    studio = price_studio * nights
    apartment = price_apart * nights
    if nights > 14:
        studio = price_studio * nights * 0.8
        apartment= price_apart * nights * 0.9
elif month == 'July' or month == 'August':
    price_studio = 76
    price_apart = 77
    studio = price_studio * nights
    apartment = price_apart * nights
    if nights > 14:
        studio = price_studio * nights
        apartment = price_apart * nights * 0.9

print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')