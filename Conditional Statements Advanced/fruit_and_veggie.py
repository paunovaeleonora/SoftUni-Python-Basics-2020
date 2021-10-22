item = input()


is_fruit = item == 'banana' or item == 'apple' or item == 'kiwi' or item == 'cherry' or item == 'lemon' or item == 'grapes'
is_vegetable = item == 'tomato' or item == 'cucumber' or item == 'pepper' or item == 'carrot'
if is_fruit:
    print('fruit')
elif is_vegetable:
    print('vegetable')
else:
    print('unknown')