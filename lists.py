fruits = ['apple', 'banana', 'cherry', 'date', 'elderberry']
print(fruits[1])
fruits[0] = 'mango'
fruits.append('orange')
fruits.insert(2, 'Bathel')
print(fruits)
fruits.remove('date')
print(fruits[-1])
 

names = ['modest', 'karen', 'lynn', 'junior', 'nancy', 'mary', 'arthur']
print(names[2:5])


countries = ['Uganda', 'Kenya', 'Tanzania', 'Rwanda', 'Burundi', 'South Sudan']
Duplicate = countries.copy()
print(Duplicate)
for country in countries:
    print(country)


animals = ['cat', 'dog', 'buffalo', 'elephant', 'lion', 'tiger']
animals.sort()
print(animals)
animals.reverse()
print(animals)
for animal in animals:
    if 'a' in animal:
        print(animal)



surnames = ['nakiroya',  'mugisha', 'asasira', 'mundu']
firstNames = ['modest', 'joseph', 'arthur', 'nancy']
surnames.extend(firstNames)
print(surnames)

cars = ['toyota', 'honda', 'mercedes', 'bmw']
for car in cars:
    print(car)