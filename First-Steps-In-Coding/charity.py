days = int(input())
chefs = int(input())

cakes = int(input())
gofrets = int(input())
pancakes = int(input())

total = days * chefs * (cakes * 45 + gofrets * 5.8 + pancakes * 3.2)
expences = total/ 8
end_money = total - expences
print(end_money)