speed = 0
fuel_level = 100

print(f"welcome to a racing car game")
print(f"your goal is to drive to finsh line without running out of fuel")

while fuel_level > 0 :
    print(f"\nspeed:{speed} km/h")
    print(f"\nfuel_level : {fuel_level} %")
    break

action =input("what do you what to do ? (A)ccelarate (B)rake (R)efuel :")
print(action)
if action.upper() == "A":
    speed += 10
    fuel_level -= 5
    print("you have accelarated")
     

elif action.upper() == "B" :
    speed += 10
    if speed <0:
        speed = 0
        print("you have braked")
        

elif action.upper() == "R" :
    fuel_level += 20
    if fuel_level < 100 :
        fuel_level = 100
        print("you have refueled")
        
if speed >= 100 :
    print("\ncongragulations! you have reached the finishing the line!")
     
if fuel_level<= 0 :
    print("\nGame over! you ran out of fuel.")
    
speed -= 5
if speed < 0 :
    speed = 0 


