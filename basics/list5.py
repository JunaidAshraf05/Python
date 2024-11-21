tea_varieties = ["black" , "green" , "oolong" , "white"]
print(tea_varieties)

print(tea_varieties[-1])
# white
print(tea_varieties[1:3])
# ['green', 'oolong']

print(tea_varieties[:2])
['black', 'green']

print(tea_varieties[2:])
['oolong', 'white']

print(tea_varieties[3])
white

tea_varieties[3]="herbal"
print(tea_varieties)
['black', 'green', 'oolong', 'herbal']

tea_varieties[1:2]
['green']
tea_varieties[1:2]="lemon"
tea_varieties
['black', 'l', 'e', 'm', 'o', 'n', 'oolong', 'herbal']

tea_varieties[1:2] = ["lemon"]
tea_varieties
['black', 'lemon', 'oolong', 'white']