beverages= set(["coffee", "beer", "water"])
beverages.add("juice")
beverages.add("tea")
print(beverages)

mySet = {"oven", "kettle", "microwave", "refrigerator"}
check = "microwave" in mySet
print(check)
mySet.remove("kettle")
print(mySet)
for item in mySet:
    print(item)

m = {"books", "pens", "pencils", "rubber"}
n= ['ruler', 'set']
for requirement in n :
    m.add(requirement)
    print(m)

ages= {22, 13, 27, 17 }
firstNames = {"modest", "amani", "lynn", "charles"}
joined = ages | firstNames
print(joined)