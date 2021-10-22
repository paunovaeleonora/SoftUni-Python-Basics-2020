budget = float(input())
statists = int(input())
clothes_price = float(input())

decor = budget * 0.1
total_expences_clothes = statists * clothes_price
if statists > 150:
    total_expences_clothes *= 0.9

total_expences = decor + total_expences_clothes
diff = budget - total_expences

if diff < 0:
    print(f"Not enough money!\nWingard need {abs(diff):.2f} leva more.")

else:
    print(f'Action!\nWingard starts filming with {diff:.2f} leva left.')
