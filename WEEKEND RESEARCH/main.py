# list comperihesion


doubles = []
for x in range (1,11):
    doubles.append(x * 2)

print(doubles)

fruits =["apple","banana","orange","strawberry"]
fruits =[fruits[0] for fruit in fruits]

print(fruits)