a="!!!!Adityaa Mehra!!!! !!!!!Adityaa Mehra!!!!!!!!!!!!!!!!!!"
a2="introduction tO python"
a3="welcome to the console !!!"
print(len(a))#length of the string a


#Strings are immutable


print(a.upper())# makes the string a into uppercase
print(a.lower())# makes the string a into lowercase

print(a.rstrip("!"))# removes the TRAILING characters

print(a.replace("Adityaa Mehra","Adi"))# replaces ALL THE OCCURANCES OF THE WORD adityaa mehra with Adi

print(a.split(" "))# makes a LIST

print(a2.capitalize())# it turns all the other characters to LOWERCASE and the first character to UPPERCASE

print(a3.center(50))

print(a.count("Adityaa Mehra"))# counts the occurances of the characters in the string

print(a3.endswith("!!!",4,8))

print(a.find("Adityaa Mehra"))# returns the index of the FIRST OCCURANCE of the string
print(a.find("Meht"))# as the string is not in the string thus , it return -1

print(a.isalnum())# it tells if the string is ALPHANUMERIC or not

print(a.isspace())