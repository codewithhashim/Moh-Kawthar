# Collection
# list, tuples, set and dictionaries

# indexed, order, changeable, duplicate

# dictionaries are like  Arrays or objects (in JS) having key value pairs

car = {
    "key" : "value",
    "brand": "Toyota",
    "Model" : "Grande",
    "make_year": 2018,
    "shape": "sedan",
    "max_speed" : "100"
}
# print(type(car))

# wrong
# print(car["make_year"].pop())

# print individual dictionary item
# print(car["make_year"])

# wrong way of popping dictionary item
# print(car.pop(1))

# correct
print(car.pop("shape"))

print(car)













