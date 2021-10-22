days = int(input())
type = input()
feedback = input()

nights = days - 1
price = 0

if type == 'room for one person':
    price = 18 * nights
elif type == 'apartment':
    if days < 10:
        price = 25 * nights * 0.70
    elif 10 <= days <= 15:
        price = 25 * nights * 0.65
    elif days > 15:
        price = 25 * nights * 0.5
elif type == 'president apartment':
    if days < 10:
        price = 35 * nights * 0.90
    elif 10 <= days <= 15:
        price = 35 * nights * 0.85
    elif days > 15:
        price = 35 * nights * 0.80

if feedback == 'positive':
    price = price + price * 0.25
elif feedback == 'negative':
    price = price - price * 0.10

print(f'{price:.2f}')

