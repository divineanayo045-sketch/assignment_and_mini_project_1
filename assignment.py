# #EXERCISE 6.1

# name = "Ada"
# age = 22
# if age>=16:
#     print("Adult")

# #EXERCISE 6.2

# commodity = ("rice")
# price = 2000
# qty_in_stock = 4 
# available_for_sale = True
# print(f"commodity:", commodity)
# print(f"price:", price)
# print(f"qty_in_stock:", qty_in_stock)
# print(f"rice is in quantum for sale")

# #EXERCISE 6.3a


# movies = ["krishna", "strike", "aura", "the sea", "deep"]#list operations.
# print("aura")
# movies[0] = "smile"
# movies.append("scream")
# print(movies)

# #EXERCISE 6.3b

# masterpiece = {"title": "lane",#dict operations.
#                 "author": "benny",
#                 "year": "2026",
#                 "price": "$15"}
# print("author:", masterpiece ["author"])
# price = "$19"
# in_stock = False
# print(f"Welcome to Divah Books!! please review...")
# print("title:", masterpiece ["title"]) 
# print("author:", masterpiece["author"])
# print("year:", masterpiece["year"])
# print("price:", masterpiece["price"])
# if in_stock:
#      print("Lane is all Yours!!!")
# else:
#      print("oops! Lane is out of stock")

#      #EXERCISE 6.3c

#      state = ("Aba", "Edo", "Lagos")#tuple operations
#      print("Edo")
#      city_1, city_2, city_3 = state
#      city_1 = "ondo"
#      print(state)#TUPLE CANNOT BE MODIFIED..

     #EXERCISE 6.3d:
figures = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
unique = set(figures)#conversion to set thereby removing duplicates
sorted_list = sorted(unique)#here sorts the list
print("sorted list without duplicates:", sorted_list)
# Intersection
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print("intersection:", a & b)

#EXERCISE:6.3e
#EXERCISE:6.f

#EXERCISE:6.3g

print(10 + 2 * 3 ** 2 // 4)
print((10 + 2) * 3 ** 2 // 4)

#EXERCISE:6.3h

total = 100
print(100 - 30)
print(70 * 2)
print(140 / 5)
print(28.0 // 3)

#EXERCISE:6.3I
full_name = str(input("Enter your full name:"))
print("Full Name:", full_name)

name ="Divine    Bethel"

print(name.strip())
print(name.upper())
print("first name:\tDivine\nlast name:\tBethel")


#EXERCISE:6.4:

product_name = input("Enter the product name:")
product_price = input("Enter the product price:")
product_QTY = input("input quantity:")
total = product_price * product_QTY
print(f"total: ${total}. THANKS FOR BUYING! WE LOOK FORWARD TO NEXT TIME")