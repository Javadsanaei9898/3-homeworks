main_list = ['mohammad kamali', 'ali nekoonam' , 'farhad alavi' , 'ali alavi', 'mohammad komeili' , 'javad jafari', 
             'javad jamali' , 'majid koohi', 'hamid rezaii', 'fatemeh hamidi', 'fatemeh yahyaii', 'negar lavasani', 
             'asal moghadam', 'kamran razavi']

my_list = list(map(lambda x: x.split(' ')[0], main_list))

stats = {}

for i in my_list:
    if i in stats:
        stats[i] += 1
    else:
        stats[i] = 1


result = ""

for key, value in stats.items():
    result += f"{key} = {value}, "
    if value == 1:
        print(f'{key} has a unique name')

result = result.rstrip(', ')

print(result)
    