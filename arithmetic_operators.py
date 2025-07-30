# Arithmetic Operations Mini Projects
# Simple Interest
# SI = PTR / 100
# from nltk.sem.linearlogic import Expression

print("Calculating Simple Interest")
# Input
principal = input("Please enter the Principal Amount: ")
interest_rate = input("Please enter the Interest Rate %: ")
time_duration = input("Please enter the Time duration (yrs): ")

# Float Conversion
float_principal = float(principal)
float_interest_rate = float(interest_rate)
float_time_duration = float(time_duration)
simple_interest = (float_principal * float_interest_rate * float_time_duration) / 100

# simple_interest = (principal * interest_rate * time_duration) / 100


print(f"Our calculated Simple Interest is: {simple_interest}")



# Write 2 different programs to implement these 2 formulae for weight conversion

# Collect Kgs from user and convert to pounds
# Pounds = 0.45 * Kgs
#print("\n")

# Collect pounds from user and convert to kgs
# Kgs = 2.2 * Pounds
#print("\n")






#Fahrenheit Celsius & Kelvin Conversion - Temperature conversions

# Collect Fahrenheit value from User and convert into Celsius
# C = (F - 32) * 5/9
#print("\n")


# Collect Celsius value from User and convert into Fahrenheit
# F = (9/5 * C) + 32
#print("\n")


# Collect Kelvin value from User and convert it into Celsius and Fahrenheit
# C = K - 273.15
# F = (K - 273.15) * 9/5 + 32
#print("\n")





# Survey about a person & their interests and prepare a mini report or a biodata
# Collect Name, Birth year - Calculate age while printing, Interests, Hobbies
# A brief quote about them to be visible in quotes while printing
# Collect marks of 3 subjects in their grade and calculate percentage of marks
# Percentage = (sub_1_marks + sub_2_marks + sub_3_marks)/3*100
# Collect all the information into a variable called biodata - using formatter string f"" and then print it

print("\n")
print("Surveying about Person")
name = input("Please enter your name: ")
birth_year = int(input("Please enter the Birth Year: "))
interests = input("Please enter your interests: ")
hobbies = input("Please enter your hobbies: ")
quote = input("Please enter your quote: ")
subject_1_marks_out_of_100 = float(input("Please enter your subject-1 marks out of 100: "))
subject_2_marks_out_of_100 = float(input("Please enter your subject-2 marks out of 100: "))
subject_3_marks_out_of_100 = float(input("Please enter your subject-3 marks out of 100: "))
total_marks_per_subject = 100
percentage = ((subject_1_marks_out_of_100 + subject_2_marks_out_of_100 + subject_3_marks_out_of_100) / (total_marks_per_subject * 3)) * 100

biodata = f"""
Name: {name},
Age: {2025 - birth_year},
Interests: {interests},
Hobbies: {hobbies},
Quote: "{quote}",
Percentage: {round(percentage,2)} %,
"""

print(biodata)

# Calculating Perimeter and Area of different shapes
print("\n")
# print("Calculating Perimeter and Area of different shapes")

# Area & Perimeter of Square


# Area & Perimeter of Rectangle


# Area & Perimeter of Circle


# Area & Perimeter of Triangle
# Area = 1/2 * base * height - Collect Base and Height of Triangle to calculate Area

# Perimeter - You need to collect all sides measurement of the triangle to calculate perimeter


# Digit Separator
# 3 digit number
print("\n")
print("Digit Separator")
number = input("Please enter a 3 digit number: ")
integer_number = int(number)

first_remainder = integer_number % 10
integer_number = int(integer_number) // 10
second_remainder = integer_number % 10
integer_number = int(integer_number) // 10
third_remainder = int(integer_number) % 10

print(f"{third_remainder} {second_remainder} {first_remainder}")



#Few arithmetic operations
#PE MD AS
expression = 10 * (5 + 30) * 3 ** 2 * 5  / 10 - 20
print("Expression Value: ", expression)

#Division

#Standard division
normal_division = 10 / 3
print("Normal Division: ",normal_division)

floor_division = 10 // 3
print("Floor Division: ",floor_division)

# Modulus - Remainder
print("Remainder: ", 10 % 3)

# Exponent or to the power of
print("Exponent: ", 10 ** 3)

#Import Math Module
import math
print("Floor division using math function: ", math.floor(10 / 3))
print("Ceil division using math function: ", math.ceil(11.9 / 3))

print("Rounding value to nearest number: ", round(2.9))
print("Absolute value to nearest number: ", abs(-2.9))

#Augmented assignment operator -=, +=, *=, /=

x = 10

x = x + 3 # 13
x += 3

x = x * 3
x *= 3

x /= 5
x = x / 5

# Giving the change only - 3, we are also doing the operation mentioned "+"
# we are assigning back the result to x


x = x * 3
x *= 3

print("Augmented x+: ", x)

x -= 3
print("Augmented x+: ", x)

x *= 3
print("Augmented x*: ", x)

print("Augmented x/: ", x)
x /= 3

#
#
# Calculate age from days

days = int(float(input("Please enter the number of days: ")))

years = days // 365
months = (days % 365) // 30
days_left = (days % 365) % 30

print(f" Years: {years}, Months: {months}, Days: {days_left}")


# Digital Clock Converter
# Input seconds

seconds = int(float(input("Please enter the number of seconds: ")))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
seconds_left = (seconds % 3600) % 60


