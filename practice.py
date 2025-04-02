# strings

first_name = "tadiwa"
food = "nadoos"
email = "tadiwamangate@gmail.com"



print(f"hello {first_name}") 
print(f"you like {food}")
print(f"your email_address is {email}")

# intergers

age = 17

print(f"you are {17} years old")

# boolean

is_student = True

print(f"are you a student?:{is_student}")

# if

age =int(input("enter your age: "))

if age >=18:
    print("you are signed up now!")

elif age <= 0:
    print("you are not bone yet!")
elif age >=100:
    print("you are to old to sign up")
else: 
    print("you must be 18+ to sign up")

response = input("would you like food?(Y/N):")
if response == "Y":
    print("have some food!")
else:
    print("no food for you")

name = input("enter you name:")

if name =="":
    print("you did not type in your name!")
else:
    print(f"hello{name}")

for_sale = True

if for_sale:
    print("item is for sale")
else:
    print("item is not for sale")

# typecasting

name = "tadiwa"
age  = 15
gpa = 2.9
student = True
print(type (name))
print(type (age))
print(type (gpa))
print(type (student))

age = float(age)
print(age)

name = input("enter your name:")
age
print(f"wlcome {name}")

