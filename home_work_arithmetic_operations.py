# Arithmetic Operations Mini Projects
# Simple Interest
# SI = PTR / 100

print("Calculating Simple Interest")
# Input
principal = input("Please enter the Principal Amount: ")
interest_rate = input("Please enter the Interest Rate: ")
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
# Collect Name, Birth year - Calculate age
# Collect Interests, Hobbies
# Collect - A brief quote about them to be visible in "quotes" while printing
# Collect marks of 3 subjects in their grade and calculate percentage of marks
# Calculate Percentage = ((sub_1_marks + sub_2_marks + sub_3_marks)/ (total marks per subject * 3 )) *100
# Collect all the information into a variable called biodata - using formatter string f"" and then print it

print("\n")
print("Surveying about Person")

biodata = ""

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
