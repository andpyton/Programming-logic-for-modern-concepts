# Exercise: Machine Learning Data Quality Monitor
# Context

# Before training a Machine Learning model, data must be validated and cleaned.
# You are simulating a data quality monitoring system that inspects incoming samples
# and decides whether training can continue.

# Given data "samples": Each item represents a data sample collected from sensors:

# Rules

# Process samples one by one using a while loop.

# Keep counters for:

# Valid samples

# Invalid samples

# Consecutive invalid samples

# Validation rules:

# value must be between 0 and 1

# value must not be None

# Behavior:

# If sample is valid → print: Sample OK

# If sample is invalid → print: Invalid sample detected

# If 3 invalid samples occur consecutively:

# Print: Data quality too low — stopping training

# Stop processing (break)

# At the end, print:

# Number of valid samples

# Number of invalid samples

# Remaining unprocessed samples

samples = [

    {"id": 1, "value": 0.82, "label": 1},
    {"id": 2, "value": None, "label": 0},
    {"id": 3, "value": None, "label": 1},
    {"id": 4, "value": -0.10, "label": 1},
    {"id": 5, "value": 0.91, "label": 1},
    {"id": 6, "value": None, "label": 0},
    {"id": 7, "value": None, "label": 1},
    {"id": 8, "value": 0.60, "label": 0}
]

# Counting invalid numbers (General)
cont_invalid_sample = 0

# Counting valid numbers
cont_valid_ = 0

# Counting invalid numbers (consecutively)
cont_invalid_consecutively = 0

while samples:

  sample = samples.pop(0)
  value = sample["value"]

  if value is None:
    print("Invalid Sample detected.")
    cont_invalid_sample+=1
    cont_invalid_consecutively+=1

    if cont_invalid_consecutively==3:
      break
    
  elif 0<=value<=1:
    print("Sample Ok.")
    cont_valid_+=1

  else:
    print("Invalid sample detected")
    cont_invalid_sample+=1
    cont_invalid_consecutively+=1

    if cont_invalid_consecutively==3:
      print("Data quality too low - stopping training")
      break

print(f'Number of valid samples is {cont_valid_}')
print(f'Number of invalid samples is {cont_invalid_sample}')
print(f'Remaining unprocessed events: {samples}')




