name = input('enter your name:')
print(name)

name_1 =input('enter second number')
name_2 =input('enter the first number:')

result = name_1 + name_2
print(result)
print(type(result))

name_1 =float(name_1)
name_2 = float(name_2)
print(name_1)
print(name_2)

a = 23
b = 24
c = 24

print(a>b and b == c)
username_1 = "admin"
password_2 = 1234

username = input("enter username:")
password = int(input("enter password:"))
if username == username_1 and password == password_2 :
    print(f"welcome {username_1} you are logged in")
else:
    print("invalid information")

temp_1  = 30
condition_2 = "sunny/cloudy"

temp = int(input("enter the temp(in degrees):"))
condition =input("enter the condition_2(sunny/cloudy):")

if temp >= 30 and condition.lower() == "sunny":
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
print(numbers[5])

student ={"name":"anna",
          "age":23
          }
student["age"] = 34
student["name"]= "ammy"
print(student)

