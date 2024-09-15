dic={'name':"Adityaa",'age':19,'eligible':True}

#update():- to add key and value pairs
dic.update({'Date of birth':2006,'Choice of language':"Python"})

#clear():- It is used to make an empty dictionary
#pop():- It removes the said key and value pair
dic.pop('name')

#popitem():- will remove the last key and value pair
dic.popitem()

#del:- it is a keyword, and it will delete the whole dictionary , like the set
del dic['age']
print(dic.items())
