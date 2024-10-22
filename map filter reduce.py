def cube(x):
    return x**3
print(cube(2))

# map
l = [1,2,3,4,5,6]
newl = list(map(cube, l))
print(newl)

# filter
def filter_function(a):
 return a>4

newnewl = list(filter(filter_function, l))
print(newnewl)

    