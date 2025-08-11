from datetime import datetime  # Import module to get current year automatically

# Ask user to enter their name and store it
name = input("Enter your name: ")

# Ask user to enter their birth year and convert it to an integer
year = int(input("Enter your birth year: "))

# Get the current year dynamically
current_year = datetime.now().year

# Calculate the user's current age
age = current_year - year

# Calculate how many years left to reach 100
years_left = 100 - age

# Calculate the year when the user will turn 100
year_100 = current_year + years_left

# Print the result
print(f"Hello {name}! You will turn 100 years old in the year {year_100}.")
