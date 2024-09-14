# letter = "Hey my name is {} and I am from {}"
country= "India"
name=("Harry")
# print(letter.format(name,country))

#F-STRING
print(f"Hey my name is {name} and I am from {country}")
#IF WE NEED TO SHOW {name} then we will place {{ }} this
print(f"Hey my name is {{name}} and I am from {{country}}")
txt="For only {price:.2f}"
print(txt.format(price=49.098))
print(type(f"{2*60}"))