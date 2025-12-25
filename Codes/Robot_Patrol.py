# Robot Patrol Simulation (Intermediate)
# Context

# You are programming a security robot that patrols an area divided into sectors.
# Each sector may contain an event that the robot must handle. The robot processes events one by one, in order,
# until: there are no more events, or the robot’s battery runs out

# Rules

# The robot starts at sector 0

# Each event consumes battery

# Battery costs:  "move" → 1 battery , "scan" → 2 battery, "repair" → 3 battery

# If the robot does not have enough battery to perform the next event, it must stop
# Every successfully executed event must be stored in a list called log
# Your Tasks
# Use a while loop to process the events list
# Remove events as they are executed
# Stop the loop if:
# the list becomes empty OR
# the battery is insufficient
# At the end, print:
# Remaining battery
# Events left unprocessed
# Execution log

events = ["scan", "move", "move", "repair", "scan", "move"]
log = []
battery = 5

while events and battery>0:

  item = events.pop(0)
  if item == "scan" and battery>=2:
    battery-=2
    print(f'Executing {item}...')
    log.append(item)
  elif item =='move' and battery>=1:
    battery-=1
    print(f'Executing {item}...')
    log.append(item)
  elif item =='repair' and battery>=3:
    battery-=3
    print(f'Executing {item}...')
    log.append(item)
  else:
    break

print(f'processed events: {log}')
print("Events left unprocessed...")
print(f'{events}')
print(f'Remaining battery is: {battery}')
