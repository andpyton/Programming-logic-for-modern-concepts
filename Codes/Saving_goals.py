# 🏦 The Problem: "The Savings Goal"
# Scenario: You want to buy a new gaming console (or any item you like) that costs a specific amount of money.
# You currently have $0 saved, but you can save a fixed amount of money every month from your allowance or salary.
# Your Task: Write a program that calculates how many months it will take to reach your goal.
# Requirements:
# Define a variable for the goal amount (e.g., 500).
# Define a variable for how much you save per month (e.g., 80).
# Use a while loop to simulate the months passing. The loop should continue running while your current savings are less than the goal.
# Inside the loop:
# Add the monthly saving amount to your total savings.
# Increase a "month counter" by 1.
# Print the total number of months it took to reach (or pass) the goal.

while True:

  try:

    goal = int(input("Type goal of money to save: "))
    if goal<=0:
      print("Try again, 0 an negative numbers aren´t allowed: ")
    saves = int(input("Type how much do you want to save per month: "));
    if saves<=0:
      print("0 and negative numbers are not valid, try again...")
    elif goal>=0 and saves>=0:
      break

  except ValueError:
    print("Type a valid input...")

def numbers_of_months(savings, goal):

  var =  0
  months = 0
  saved = savings

  while saved<goal:

    months += 1
    saved += var

    print(f'Month {months} = {saved} saved.')

    var = savings

  return  months, saved

months, saved = numbers_of_months(saves, goal)


