s1 ={1 ,2 ,4 ,5,6}
s2 ={3,6,7}
print(s1.union(s2))

print(s1 ,s2)

#it will s2 value in s1
s1.update(s2)

#===========another example===========#

cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}

cities2 ={ "Tokyo", "seoul" , "kabul" , "Madrid"}
cities3 = cities.union(cities2)
print(cities3) 



##intersection = jo same hai dono wahi sirf print hoga baki  isme se extra value hat jyega

cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}

cities2 ={ "Tokyo", "seoul" , "kabul" , "Madrid"}
cities.intersection_update(cities2)
print(cities) 