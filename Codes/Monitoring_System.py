# EXERCISE: NETWORK INTRUSION MONITORING SYSTEM (INTERMEDIATE)

# You are simulating a network security monitor that processes firewall events.

# Given list 'events'

# Rules:
# - Process events one by one using a while loop
# - Use a counter for failed login attempts

# Event behavior:
# "NORMAL"            -> print: Traffic normal
# "FAILED_LOGIN"      -> print: Warning: failed login attempt
# "MALWARE_DETECTED"  -> print: CRITICAL THREAT DETECTED
#                        stop monitoring immediately (break)

# Security logic:
# - If 3 FAILED_LOGIN events occur consecutively:
#   print: Possible brute force attack detected
#   reset the failed login counter

# After monitoring ends, print:
# - Total number of processed events
# - Remaining unprocessed events

# Constraints:
# - Use while
# - Use if / elif / else
# - Use break
# - Do NOT use functions
# - Do NOT use for in the main loop
# - for is allowed only to print remaining events

events = [
    "NORMAL",
    "NORMAL",
    "FAILED_LOGIN",
    "NORMAL",
    "FAILED_LOGIN",
    "FAILED_LOGIN",
    "FAILED_LOGIN",
    "MALWARE_DETECTED",
    "NORMAL"
]

failed_login = 0
processed_events = 0

while events:

  processed_events +=1
  item = events.pop(0)

  if item == "NORMAL":
    failed_login=0
    print("Traffic normal...")
  elif item =="FAILED_LOGIN":
    print("Warning: failed login attempt..")
    failed_login+=1
    if failed_login==3:
      print("Possible brute force attack detected.")
      failed_login = 0
  elif item == 'MALWARE_DETECTED':
      print("CRITICAL THREAT DETECTED")
      break

print(f'Quantity of processed events is {processed_events}')
print(f'list of unprocessed event is {events}')
