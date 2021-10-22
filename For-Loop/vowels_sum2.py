word = input()
result = 0
for index in range(0, len(word)):
    if word[index] == 'a':
        result += 1
    if word[index] == 'e':
        result += 2
    if word[index] == 'i':
        result += 3
    if word[index] == 'o':
        result += 4
    if word[index] == 'u':
        result += 5

print(result)
