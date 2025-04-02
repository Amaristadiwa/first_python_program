print("welcome to tadiwa's receap code")

name = "tadiwa"
print(name)

print(f"Hello to you {name}")


age = 14
print(age)
print(type(age))

number_of_children = 30
print(number_of_children)
print(type(number_of_children))

x = 2
y = 4

print(f"addition{x+y}")
print(f"subtraction{x-y}")
print(f"multiply{x*y}")
print(f"devision{x/y}")
print(f"modulus{x%y}")
print(f"interger devision{x//y}")
print(f"expo or power of{x**y}")

a = True
b = False

print(type(a))
print(type(b))

persona = {'name', 'anna','age', 23,'city','harare'}
print(persona)

colors = ('red','blue', 'yellow')
print(colors)

fruits = ["apple","banana","orange"]
nums = [1,2,3,4,5,6,7,8]
mixed_list = [1,2,3,4,5,6,"kiwi",[1,2,3,4.3]]

print(fruits)
print(nums)
print(mixed_list)

print(fruits[0])
print(nums[3])

numbers = [10,20,30,40,50]

numbers[0]=5
print(numbers)


fruits = ['apple','banana','orange']
fruits[0]='kiwi'
print(fruits)

fruits.append("mango")
print(fruits)
fruits.insert(1,"guava")
print(fruits)

student ={"name": "anna",
          "age" : 20,
          "job" : "physcian"}

print(student)


student["name"] = "amaris"
print(student)

response = input(f"would you like some pizza ? (yes/no)")
if response == "yes":
    print("have some pizza")
else:
    print("no pizza for you")

name = "anna"
register = ""
if register == "present":
    print(f"{name} is {register}")
else:
    print(f"{name} is absent")

x = 2
if x > 5 :
    print(f"{x} is greater than 5")
else:
    print(f"{x} is less than 5")
response = input("do you like pizza !")
Y = "yes"
N =  "no"
if response == Y:
    print("lets have some pizza")
else:
    print("no pizza for you")

username = "admin"
password = 1234

username  = input("Enter username !")
if password == 1234:
    print("welcome admin")
else:
    print("invalid information")

first_name = "anna"
food = "wrap"
email = "tadiwamangate9@gmail.com"

print( f"hello {first_name}")
print(f"my favourate food is {food}")
print(f"my email address is {email}")



# functions

def greet(name):
    print(f"hello {name}")
greet("hello tadiwa")


def add(a,b):
    return a + b
print(add(4,5))

def multiply(x,y):
    return x * Y
print(multiply(5,8))

#files

file = open("index.txt","r")
contect = file.read()
print(contect)
file.close()

name = "tadiwa"
age = 20
gpa = 2.4
student = True


print(type(name))
print(type(age))
print(type(gpa))
print(type(student))



age = float(age)
print(age)

name = input("enter your name !")
print(f"welcome {name}")

age =int(input("enter your age: "))

if age >=18:
    print("you are signed up now!")

elif age <= 0:
    print("you are not bone yet!")
elif age >=100:
    print("you are to old to sign up")
else: 
    print("you must be 18+ to sign up")


for_sale = True

if for_sale:
    print("item is for sale")
else:
    print("item is not for sale")

doubles = []
for x in range (1,11):
    doubles.append(x * 2)

print(doubles)

fruits =["apple","banana","orange","strawberry"]
fruits =[fruits[0] for fruit in fruits]

print(fruits)

numbers = (1,2,3,4,5,6)
print(numbers)

print(numbers[0])

print(numbers[1:3])

num = (1,2,3)
num_2 = (4,5,6)
print(num  + num_2)

print(num * 2)


set = {1,2,3,4,5,6}
print(set)

set.add(7)
print(set)

set.remove(4)
print(set)

set = {"apple","banana","mango"}
set_2 ={"orange","kiwi"}

print(set.union(set_2))

list = ["boy","girls",[1,2,3,4]]
print(list)




name_1 =input('enter second number')
name_2 =input('enter the first number:')

result = name_1 + name_2
print(result)
print(type(result))

name_1 =float(name_1)
name_2 = float(name_2)
print(name_1)
print(name_2)

a = 30
b = 45
c = 30

print(a>b and b == c)
username_1 = "admin"
password_2 = 1234

username = input("enter username:")
password = int(input("enter password:"))
if username == username_1 and password == password_2 :
    print(f"welcome {username_1} you are logged in")
else:
    print("invalid information")

temp_1  = 20
condition_2 = "sunny/cloudy"

temp = int(input("enter the temp(in degrees):"))
condition =input("enter the condition_2(sunny/cloudy):")

if temp >= 20 and condition.lower() == "sunny":
    print("it is sunny")
else:
    print("it is cold")


day = input("enter day:").lower()

if day =="monday":
    print("wear uniform")
elif day == "tuesday":
    print("wear jeans")
elif day == "wensday":
    print("wear casual")
elif day == "thursday":
    print("wear formal")
elif day == "friday":
    print("wear tomboy_style")
else:
    print(f"is not a day")

score = int(input("enter your score:"))
if score >=90 and score <=100:
    print('A')
elif score >=80 and score < 89:
    print('B')
elif score >=70 and score < 79:
    print('C')
elif score >=60 and score < 69:
    print('D')
elif score >=50 and score < 59:
    print('E')
elif score >=40 and score <49 :
    print('F')
else:
    print("invalid score")

numbers = [1,2,3,4,5,6,7,8,9]
print(numbers[6])

student ={"name":"anna",
          "age":23
          }
student["age"] = 34
student["name"]= "ammy"
print(student)

name = input("enter your name:")
print(name)

score = 4
while score < 8 :
    print(score)
    score = score + 1


print("welcome to the race game .")


command = ""
while True :
    command = input("enter a command :").lower()
    
    if command == 'quit':
        print("exiting the game")
        break
    elif command == 'start':
     print("car started")
     
    elif command == 'stop':
       print("car has stopped")
       
    elif command == 'help':
       print("""
start- to start the car
stop - to stop the game
quit - to exit the game
help - to show all commands
       """)
    else:
       print("i don't understand this!")

number_to_guess = 7

print(f"welcome to the guess a number game")

guess = int(input("guess a number:"))
print(guess)

while True:
    if number_to_guess > 7:
        print("your number to guess is grater than the correct number")
        number_to_guess = int(input(f"guess another number less than{number_to_guess} :"))
    elif number_to_guess < 7:
        print("your number is less than the correct number")
        number_to_guess = int(input(f"guess another one greater than {number_to_guess} :"))
    else:
        print("you have guessed the correct number")
        number_to_guess =int(input("guess anumber :"))

    