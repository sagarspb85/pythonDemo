mystr= "harry is a good boy"

print(mystr[0:5]) # Harry
print(len(mystr)) # 19
print(mystr[::-1]) # yob doog a si yrraH


mystr1= "Harryisagoodboy123"
print(mystr1.isalnum()) #True (only alphabet numbers)

mystr3= "Harryisagoodboy"
print(mystr3.isalpha())  #True (only alphabet )

print(mystr.endswith("boy")) #True

print(mystr.count("o")) # 3

print(mystr.capitalize()) # Harry is a good boy (first letter capital)

print(mystr.find("is")) # 6

print(mystr.lower()) # harry is a good boy

print(mystr.upper()) # HARRY IS A GOOD BOY

print(mystr.replace("is","are")) #harry are a good boy