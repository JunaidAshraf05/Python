# Normal function code 

def average (a ,b):
    print("The average is ", (a + b) / 2)

average(4,6)

#example
#in this it will take second arguement 
def average (a=9 ,b=1):
    print("The average is ", (a + b) / 2)

average(4,6) # second argument

#example
def average (a ,b=4):
    print("The average is ", (a + b) / 2)

average(4)
# in this it will  second a and first b argument 

#example

def average (a=5 , b=1 ):
    print("The average is ", (a + b) / 2)

average(b=6)
#in this it will second b argument