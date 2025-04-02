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

