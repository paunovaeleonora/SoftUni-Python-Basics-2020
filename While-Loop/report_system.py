money = int(input())
price = input()
transaction_counter = 0
total_cash = 0
total_card = 0
cash_counter = 0
card_counter = 0
total = 0
while price != "End":
    price = int(price)
    transaction_counter += 1
    if transaction_counter % 2 == 1:
        if price > 100:
            print(f"Error in transaction!")
        else:
            total_cash += price
            total += price
            cash_counter += 1
            print("Product sold!")
    else:
        if price < 10:
            print("Error in transaction!")
        else:
            total_card += price
            total += price
            card_counter += 1
            print(f"Product sold!")

    if total >= money:
        print(f"Average CS: {total_cash / cash_counter:.2f}")
        print(f"Average CC: {total_card / card_counter:.2f}")
        break

    price = input()
else:
    print(f"Failed to collect required money for charity.")