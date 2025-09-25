import random

pond = random.randint(1,10)
kg = pond / 2.2046
price = kg * 2
print('fisherman got' ,pond ,'pond fish')

if pond >= 5:
    price = kg * 3

print('your bill is', price, '$')