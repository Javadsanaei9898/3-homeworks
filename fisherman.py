import random

pond = random.randint(1,10)
kg = pond / 2.2046
price = kg * 2
reward = ['fishing rod', 'tackle box' , 'hooks' , 'fishing reel', 'bait fish']
i = random.randint(0,4)

print('fisherman got' ,pond ,'pond fish')

if pond >= 5:
    price = kg * 3

if pond >= 6:
    print(f'you got {reward[i]} for reward')


print('your bill is', price, '$')