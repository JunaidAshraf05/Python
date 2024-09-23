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

#count = it count the strings in statement
print(a.count("Junaid "))


str1 = "Welcome to console!!!!"
print(str1.endswith("!!!")) #it will tell if the strings is ending with same letter which we defined in code or not if yes it will print "true" if no it will prnt "false"

#find = it will find letter in strings if our defined letter is not there it will returnin negative value
str2 = "i am Batman "
print(str2.find("am"))

#islanum= it will return true only if the entire  string only consistA-Z a-z 0-9
str1 = "Welcome to console!!!!"
print(str1.isalnum())



str1 = "Welcome to console!!!!"
print(str1.isalpha())


#string.swapcase convert uppercase to lowercase and vice versa in a string
str1 = "I am IRONMAN"
print(str1.swapcase())
