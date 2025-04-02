# loops are used to repeat a block of code mutiple times.
#there are to types of loops = [1] while loops and for loops

# for loops is used to iterate over a sequence(list,dictionary,strings,tuples/range)

#syntax:
#for variablie in sequence:
  #staments

fruits = ["a","b","c"]
for fruit in fruits:
    print(fruit)

text = "python"
for char in text:
    print(char)

name ="anna"

def happy_birthday():
    print("happy birthday to you")
happy_birthday()



# why do we need function?
#[1] reduce code duplication
#[2] organization of code
#[3] easy to deburg

#def function_name():
#  function body
 #return a value

#def greet():
   #print("Hello, welcome to python!")
#greet()

def greet(name):
    print(f"Hello,{name}!")
greet("annie")
greet("amaris")

def add(a,b):
    return a + b
result = add(12,4)
print(result)


def sub(x,y):
    return x - y
result = sub(20,15)
print(result)

def happy_easter_holidays(name):
    print(f"happy easter holiday to you {name} !")
happy_easter_holidays("annie")

def devide(c,d):
    return c / d
result =  devide(10,2)
print (result)

def mutiply(a,b):
    return a * b
result = mutiply(10,6)
print(result)

numbers = [1,2,3,4,5,6,7,8,9,10,11]
for nums in numbers:
    print(nums)

for even in range(2,21,2):
    print(even)


for even in range(1,51):
    if even % 5 == 0:
        continue
    print(even)