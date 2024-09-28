letter = "Hey my name is{} and I am from {}"
country="India"
name="Junaid"

print(letter.format(country,name))#it will put the name in the letter statement

#to make this easy we use f-string concept
print(f"Hey my name is {name} and I am from {country}")