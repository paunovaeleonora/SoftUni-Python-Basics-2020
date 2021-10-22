import sys
import math
cake = int(input())
max_sugar = -sys.maxsize
max_flour = -sys.maxsize
total_sugar = 0
total_flour = 0
packs_sugar = 0
packs_flour = 0
for cake in range(1, cake + 1):
    sugar = int(input())
    flour = int(input())
    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour
    total_sugar += sugar
    total_flour += flour
packs_sugar = math.ceil(total_sugar / 950)
packs_flour = math.ceil(total_flour / 750)

print(f'Sugar: {packs_sugar}')
print(f'Flour: {packs_flour}')
print(f'Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.')