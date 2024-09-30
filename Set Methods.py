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

##disjoint =jisme kuch bhi common nahi hota

cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}

cities2 ={ "Tokyo", "seoul" , "kabul" , "Madrid"}
print(cities.isdisjoint(cities2))


##superset= kya function 2 ka element fun1 me hai ? check krne ke liye use hota hai

cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities2 = {"seoul" , " kabul"}
print(cities.issuperset(cities2))
cities3 ={ "Tokyo", "seoul" , "kabul" , "Madrid"}
print(cities.issuperset(cities3))
print(cities.issubset(cities2))


#to add anoter item
cities.add("helsinki")
print(cities)

#remove()/discard()
cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities.remove("Tokyo")
print(cities)


#pop= this method will remove last element of the set but catch is that which item will get popped as sets are undefined

cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
item=cities.pop()
print(cities)
print(item)

#del = by the hellp of del we can delete the entire set
cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
del cities

#clear()= by the help of clear we can clear all items and print an empty sets
cities = {"Tokyo" , "Madrid" , "Berlin" , "Delhi"}
cities.clear()
print(cities)
