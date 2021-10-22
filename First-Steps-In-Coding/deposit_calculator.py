deposit = float(input())
period = int(input())
annual_percent = float(input())

fees = deposit * annual_percent / 100
fees_for_a_month = fees / 12
total_expences = deposit + period * fees_for_a_month

print(f"{total_expences:.2f}")
