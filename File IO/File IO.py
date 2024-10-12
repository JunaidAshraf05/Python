# 

#writing a file
# f = open('myfile.txt',"a")
# f.write('Hello world')
# f.close()

# with open('myfile.txt', 'a') as f:
#     f.write("Hey i am inside with")
    
    
# read(), readline() , and other methods

# f = open('myfile.txt', 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)
    
    #another example
# f = open('myfile.txt', 'r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     m1 =line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     print(f"Mrks of student{i} in maths is:{m1}")
#     print(f"marks of student {i} is english is :{m2}")
#     print(f"Marks of student{i} is sst in {m3}")
#     if not line:
#         break
#     print(line)
    
# print(f.read())
    
    #writelines()method
f = open('myfile2.txt','w')
lines =['line 1\n' 'line2\n' 'line3\n']
f.writelines(lines)
f.close()