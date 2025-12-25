# SIMULATION OF A ROBOT CONSOLE CONTROL

# The robot waits for commands from user
# Objective is explore the "while" condition
# The robot accepts only three commands
# "move" → prints: Robot is moving
# "scan" → prints: Scanning area
# "exit" → stops the program and prints: System shutting down
# Any other input should print:
# Invalid command
# The program must:
# Use while True
# Use break to exit the loop
# Print "Loop finished" after the loop ends
# Add a counter counts how many valid commands were executed.
# Prints the number after the loops ends.
# Battery , Robot starts with 100% battery ,"move" → battery –10 "scan" → battery –5
# When battery reaches 0, the system shuts down automatically
# To exit you need to type securiy code... it is 4321.

count = 0
battery = 100
attempts=0

while True:

  print("Commands are: move, scan, exit...")
  command = str(input("Type a command: "))

  if command == "move":
    print("Robot is moving...")
    count+=1
    battery-=10
  elif command == "scan":
    print("Robot is scanning area...")
    count+=1
    battery-=5

  elif command == "exit":
     count+=1
     print("Type scurity code to exit, you have 3 attempts...")

     while True:

       try:

          security_code = int(input("Type security code: "))

          if security_code == 4321:
            print("Exit accepted...")
            exit_status = 1
            break
          else:
            attempts+=1
            if attempts == 3:
              print("Forcing shutting down...")
              exit_status = 0
              break
            else:
              print("Incorrect, try again...")

       except ValueError:
          print("Type number not a string...")

     if exit_status == 1:
        break
     elif exit_status == 0:
        break
  else:
    print("Not valid try again")



  if battery <= 0:
    battery = 0
    print("System shutting down...")
    break


print("")
print("Loop finished...")
print(f'Quantity of valid inputs is {count}')
print(f'Battery of robot is: {battery}%')



