x = 10 #global variable

def my_function():
    global x
    
    y = 5#local variable
    
my_function()
print(x)
    
#print(y)#this will cause an error because y is a local varialble and is not accesible outside of the function