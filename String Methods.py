a = " !!!!Junaid!!!! !!!!!!  !!!Ashraf" 
print(len(a))  
print(a.upper()) #its uppercase the letters
print(a.lower())#its lowercase the letters

print(a.rstrip("!"))


#replace
# it will replace the junaid letter to ashraf letter
print(a.replace("Junaid" , "Ashraf"))

#split
#it will make string in list depends on how many spaces are there
print(a.split(" "))

#blogHead
b = "introduction to js"
print(b.capitalize())  #it will capitalize the first letter of statement


#centre= this will align the text to the center
str1 = "Welcome to console!!!!"
print(str1.center(50))