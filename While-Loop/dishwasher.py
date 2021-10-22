bottles = int(input())
ml = bottles * 750
command = input()
loading = 1
used = 0
plates = 0
pots = 0
while command != "End":
    dishes = int(command)
    if loading % 3 == 0:
        used = dishes * 15
        pots += dishes
    else:
        used = dishes * 5
        plates += dishes
    ml -= used
    if ml < 0:
        break
    loading += 1
    command = input()

if ml >= 0:
    print(f"Detergent was enough!")
    print(f"{plates} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {ml} ml.")
else:
    print(f"Not enough detergent, {abs(ml)} ml. more necessary!")