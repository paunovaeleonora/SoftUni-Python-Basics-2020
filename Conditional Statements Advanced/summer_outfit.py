degrees = int(input())
time = input()

shoe = 0
outfit = 0

outfits = outfit == 'Sweatshirt' or outfit == 'Swim Suit' or outfit == 'Shirt' or outfit == 'T-Shirt'
shoes = shoe == 'Sneakers' or shoe == 'Moccasins' or shoe == 'Sandals' or shoe == 'Barefoot'

if 10 <= degrees <= 18:
    if time == 'Morning':
        outfits = 'Sweatshirt'
        shoes = 'Sneakers'
    elif time == 'Afternoon':
        outfits = 'Shirt'
        shoes = 'Moccasins'
    elif time == 'Evening':
        outfits = 'Shirt'
        shoes = 'Moccasins'
if 18 < degrees <= 24:
    if time == 'Morning':
        outfits = 'Shirt'
        shoes = 'Moccasins'
    elif time == 'Afternoon':
        outfits = 'T-Shirt'
        shoes = 'Sandals'
    elif time == 'Evening':
        outfits = 'Shirt'
        shoes = 'Moccasins'
if degrees >= 25:
    if time == 'Morning':
        outfits = 'T-Shirt'
        shoes = 'Sandals'
    elif time == 'Afternoon':
        outfits = 'Swim Suit'
        shoes = 'Barefoot'
    elif time == 'Evening':
        outfits = 'Shirt'
        shoes = 'Moccasins'
print(f"It's {degrees} degrees, get your {outfits} and {shoes}.")