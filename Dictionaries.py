dic = {
    344:"junaid",
    3444:"sdadad",
    321211:"wasdsad",
}
print(dic[321211])


#accesing sngle value
info = {'name':'karan' , 'age':19 , 'eligible':True}
print(info)
print(info['name'])
print(info.get('eligible'))
print(info.get('eligible2'))

#it wil print all keys
print(info.keys())

for key in info.keys():
    print(info[key])

print(info.values())

#pairs will give items in pair
print(info.items())

