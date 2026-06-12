# #SETS..

# phone_models = {"iphone", "techno", "nokia", "iphone", "infinix", "nokia", "itel", "nokia"}
# print(phone_models)
# numbers = [1, 2, 2, 3, 3, 3]
# print(numbers)
# #how to remove duplicates in a list.... you cast..
# unique = set(numbers)
# numbers = unique

# #conversion functions
# a = 42
# b = "42"
# c = 3.14
# #converting from int to str
# print(type(a))#type shows the data type of the value.
# a = str(a)#this is the syntax.
# print(type(a))

# #converting to string.
# print(type(b))
# b = int(b)
# print(type(b))


# print(str(42))
# print(int("42"))
# print(int(3.74))
# print(float("3.74"))
# print(bool(0))

# num = (1, 2, 3)
# print(type(num))
# num = list(num)#convert tuple to a list.
# print(type(num)) #after conversion

# append = num.append(4)
# print(num)

# num = tuple(num)#convert back to tuple
# print(num)
# #NB:you cant covert a string with characters to an integer...
# #collection convertions:
# print(list(1, 2, 3))
# print(tuple([1, 2, 3]))
# print(set([1, 2, 2, 3]))

# #class exercise#
# mobile_number = input("enter your mobile number:")
# print(mobile_number)
# mobile_number = str("081")
# print(str("081"))
# print(type(mobile_number))

# #convert to interger#
# mobile_number = int(mobile_number)
# print(type(mobile_number))

# #convert to float#
# mobile_number = float(mobile_number)
# print(type(mobile_number))

# #convert to string#
# mobile_number = str("mobile_number")
# print(type(mobile_number))


# #convert to bool
# mobile_number = bool(mobile_number)
# print(type(mobile_number))

#correction#

# #DAY 44444444444444444444
# #string methods and string operations:
# message = "   hello python world  "
# print(message.upper())#CAPITALIZE EACH WORD
# print(message.title())#CAPITALIZE EACH FIRST WORD
# print(message.lower())#CHANGES TO LOWER CASE
# print(message.rstrip())#strips spaces from the right
# print(message.lstrip())#strips spaces from the left
# print(message.split())#splits them with space, quotes'
# print(message.find('python'))

# #ESCAPE SEQUENCES:
# print("name: precious \n age: 14") #that symbol changes to a new line

# x = 10
# if x > 5 :
#     print("x is greater than 5")

# print(5 == 5)
# print(5 == 6)
# print(5 != 3)

# print(8 >= 8)

# print(5 <= 8)

# #grade checker

# score =int(input("enter your score (0-100): "))
# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score  >= 70:
#     grade = "C"
# elif score >= 50:
#     grade = "D"
# else:
#     grade = "f"

# print("Your grade is", grade)

# #SHOPPING CART DISCOUNT:
# total = float(input("cart total:"))


# if total >= 50000:
#     discount = 0.2
# elif total >= 20000:
#     discount = 0.1
# elif total >= 10000:
#     discount = 0.05
# else:   discount = 0.0

# savings = total = discount

# final_total = total * (1 - discount)
# print(f"final total after discount: ${final_total:,.2f}")
# print(f"wow! you saved: {savings:,.2f}")


# #  CLASS EXERCISE:
# errand = str(input("shoe colour:"))

# if errand == "black":
#     print("buy slippers:")
# else:
#     print("welldone!! you got the right pair")

# #correction..
# #choosing what product to buy based on colour type:
# colourofbox = input("Enter the colour of box seen in the market:")

# if colourofbox == "black":
#     print("oga leave that one and buy shoe")
# else:
#     print("oya bring am come! make i manage")

    #EXERCISE 222;
print("WELCOME TO GRAND WEIRDO CRAVINGS HAVEN")

portions = int(input("How many portions of Jellof Rice:"))
if portions >= 10:
    price_per = 800
    label = "Thanks! you'll get a huge discount"
    total_price = portions * price_per

elif portions >= 5:
    price_per = 1000
    label = "Premuim price! you get a discount"
    total_price = portions * price_per
elif portions >=4:
    price_per = 1200
    label = "Little Discount"
elif portions >=1:
    price_per = 1500
    label = "No Discount"
else:
    label = "Enter a valid Number"
    total_price = 0
if total_price >= 0:#find out the error here
    print(f"total: ${total_price} - {label}")
else:
    print(label)



