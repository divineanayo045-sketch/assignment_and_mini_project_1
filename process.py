# dict#
# name = "divine"
# age = 20
# course = "enterprise_python"
# print("my name is divine")
# print("i am 20 years old")
# print("am studying enterprise python")
# set = {"a,c", "b,d", "e,f", "g,h"}
# print(set)
# tuple = ("toyota", "camry", "benz")
# print(tuple)
# list = ["candies", "pizza", "vannilla"]
# print(list)


# name = "ada"
# age = 22
# if age>18:
#     print("ada is an adult")
# else:
#     print("ada is not an adult")



# my_num = [1,2,3,4,5,6,7,8,9,10]
# print(my_num[0:6:1])

# #modify the list using append
# list = [1,4,5,7,13,50]
# #append
# list.append(80)#adds to the last on the list.
# print(list)
# #insert
# list.insert(5,25)#inserts numbers, according to your direction of position.
# print(list)
# #remove
# list.remove(5)#removes any value you points.
# print(list)
# #pop
# list.pop()#removes the last value, unless you specify
# print(list)
# #sort
# list.sort()#sorts in ascending order.
# print(list)
# #reverse
# list.reverse()#reverses what sort did...
# print(list)

# #dictionary#
# student = {"name": "Divine", "age": 20, "score": 89.7}
# #access items in a dictionary

# student["age"]
# print(student["name"])
# print(student.get("score"))#get functions accepts strings.

# #update#what it does!!!
# student["grade"] = "A"
# student["name"] = "Divine Bethel"
# print(f"This is my profile: {student}")
# student.pop("age")
# print(student)

article = {"title": "Love for meta AI",
        "author": "Divine Bethel",
          "year": 2026,
             "price": 1000}

article.update({"price": 1200})
print("author:", article["author"])
print(article)
in_stock = True
if in_stock:
     print(f"{article['title']} is in stock and costs {article['price']}.")



# #thursday june 4th 2026.
# student = {"name": "Benny", "age": 32, "score": "100.27"}

# student["age"] = 33
# print(student)
# student["score"] = 200
# print(student)
# #del method:
# #del student["name"]
# print(student)

#creating tuples
coordinates = (10,20)
print(coordinates)

single_item = 5
single_item_1 = (5,)#it is adviced to add comma to your tuple..
empty_tuple = ()
print(single_item)
print(single_item_1)
print(empty_tuple)
empty_list = []
print(empty_list)

#tuple examples.
coordinates_3 = (40, 20, 44, 55) 
print(coordinates_3)
coordinates_3[0:3]
print(coordinates_3)

##unpacking__assign each item to a variable in one line.
#x,y = coordinates

car_models = ("mazda", "toyota", "benz", "mazda", "corrolla", "benz", "mecerdes", "mazda")
# car1, car2, car3, car4, car5 = car_models
print(car_models)
print(car_models.count("mazda"))#counts the values you mentioned.
print(car_models.index("mecerdes"))#shows the index position of the value.

#why use tuples over lists...
#1. its faster(python optimizes immutable data)
#2. can be used as dictionary keys(lists cannot)
#3. signals: this data cashould NEVER change
#   e.g. GPS coordinates, RGB colour nodes, database primary keys




