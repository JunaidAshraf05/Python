marks = [ 3 ,35 ,6]
print(marks)
print(type(marks))

 
marks = [ 3 ,35 ,6,"Junaid","True" , 8 , 9 , 5, 7 ,9 ,2 ,1 ,4 ]
print(marks)
print(type(marks))
#list can contains another datatype too
print(marks[0])
print(marks[1])
print(marks[2])
print(marks[3])
print(marks[4])
print(marks[5])
 
 
print(marks[-3]) #negative index 
# print(marks(len(marks)-3)) # positive index
 
print(marks[5-3])#positive index
print(marks[2])#positive inex

if "junaid" in marks:
  print("yes")
else:
    print("no")
    

if "unaid" in "junaid":
    print("yes")
    

print(marks)
print(marks[1:-1])
print(marks[1:4:2])