area_in_meters = int(input())

price_per_sq_meter = 7.61
discount = 0.18 * area_in_meters * price_per_sq_meter

total = (area_in_meters * price_per_sq_meter) - discount
print(f"The final price is: {total} lv.\nThe discount is: {discount} lv.")