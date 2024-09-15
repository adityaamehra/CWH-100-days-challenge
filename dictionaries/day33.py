#Dictionary is a key value pair , it is an ordered collection of data items
dic = {"Adityaa":"Human being",
       "Spoon":"Object",
       344:"Adityaa",
       365:"Shubham"}
print(dic)

print(dic[365])

print(dic["Adityaa"]) #This will throw an error in case of the unavailability of the key
print(dic.get("Adityaa")) #This will NOT throw an error in case of the unavailability of the key


for x in dic:
    print(x, dic[x],end=' ')
print()
for c in dic.keys():
    print(dic[c],end=' ')

print(dic.keys()) #.keys() will give the list of all the keys
print(dic.values()) #.values() will give the list of all the values

print(dic.items()) #.items() will give me the key value pairs

for key,value in dic.items():
    print(f"The value corresponding to the key {key} is {value}")