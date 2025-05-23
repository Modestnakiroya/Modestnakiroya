Shoes = {
	"brand" : "Nick”",
	"color" : "black",
	"size" : 40
	}
print(Shoes["size"])
Shoes["brand"] = "Adidas"
Shoes["type"] = "sneakers"

keys= list(Shoes.keys())
print(keys)

values= list(Shoes.values())
print(values)

if "size" in Shoes:
    print("the key size exists in dictionary")
else:
    print("the key size doesnot exist in dictionary")

for key, value in Shoes.items():
    print(f"{key}: {value}")

Shoes.pop("color")
print(Shoes)
Shoes.clear()
print(Shoes)

keys=['modest', 'junior','lynn','nancy']
value=['java','python', 'JS','CSS']
dictionary= dict(zip(keys, value))
print(dictionary)
dictionary2= dictionary.copy()
print (dictionary2)

student= {
    "name": "alex",
    "age": 22,
    "school" : {
        "schoolName": "makerere university",
        "city": "kamapala"
    },
    "course": "BSSE",
    "sex": "male"

}
print(student["school"]["schoolName"])