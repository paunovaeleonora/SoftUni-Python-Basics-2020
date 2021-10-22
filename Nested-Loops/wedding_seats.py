last_sector = input()
rows_first_sector = int(input())
count_seats_odd_row = int(input())
counter = 0

last_sector = ord(last_sector)
for sector in range(65, last_sector + 1):
    for row in range(1, rows_first_sector + 1):
        if row % 2 == 1:
            for seat in range(97, 97 + count_seats_odd_row):
                print(f'{chr(sector)}{row}{chr(seat)}')
                counter += 1
        else:
            for seat in range(97, 97 + count_seats_odd_row + 2):
                print(f'{chr(sector)}{row}{chr(seat)}')
                counter += 1
    rows_first_sector += 1
print(counter)



