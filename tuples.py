x= ("samsung", "iphone", "techno", "redmi")
print("Favorite phone brand is :", x[1])
print (x[-2])
update = list(x)
update[1]= "itel"
x= tuple(update)
x= x + ("Huawei",)
print(x)

for phone in x:
    print(phone)
x= x[1:]
print(x)

UgandaCities = tuple(["kampala", "jinja", "mbarara", "gulu"])
print(UgandaCities)
city1, city2, city3, city4 = UgandaCities
print(f"City 1: {city1}")
print(f"City 2: {city2}")
print(f"City 3: {city3}")
print(f"City 4: {city4}")

print(UgandaCities[1:4])

surnames = ("nakiroya",  "mugisha", "asasira", "mundu")
firstNames = ("modest", "joseph", "arthur", "nancy")
fullNames = surnames + firstNames
print(fullNames)

colors = ("pink", "orange", "green")
multiple = colors*3
print(multiple)

thistuple = (1,3,7,8,7,5,4,6,8,5)
y = thistuple.count(8)
print(y)