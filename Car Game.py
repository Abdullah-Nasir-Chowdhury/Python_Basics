# Car Game:
command = ""
started = False
while True:
    command = input("> ").lower()
    if command == 'start':
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started!...")
    elif command == 'stop':
        if started:
            print("Car stopped!")
        else:
            print("car already stopped")
    elif command == 'help':
        print("""
        start - to start the car
        stop - to stop the car
        quit - to quit
        """)
    elif command == 'quit':
        break
    else:
        print("Sorry, I don't understand that")
