##Multiplication of any number code

# a = input("Enter the number:")
# print(f"Multiplication table of {a} is:")

# try:
    
#   for i in range(1,11):
#     print(f"{int(a)} X {i} = {int(a)*i}")
    
# except Exception as e:
#    print("invalid input")
   
   
## Value error example

try:
    num = int(input("Enter an integer"))
except ValueError:
    print("Number enterd is not an integer.")