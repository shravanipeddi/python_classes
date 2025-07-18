# Primitive Data Types
# Boolean
true_boolean = True
false_boolean = False

# Integers
integer_number_1 = 10
integer_number_2 = -100

# Float
float_number_1 = 3.14
float_number_2 = -3.1435253
float_number_3 = -33534.1435253


# String
string_1 = "Hey"
string_2 = 'Hey'

string_3 = """Multiline String
which is spanning across multiple lines
just to show you that this is possible"""

string_4 = '''Another form of writing Multiline 
String spanning across 2 lines with single quotes'''

string_5 = "Using single quote - Shravani's code in a double quote line"
string_6 = 'Using double quote - "This code belongs to Shravani" in a double quote line'

string_7 = f"Hello! This is a formatter string. Here is our first integer {integer_number_1} and here is our first float {float_number_1}"

string_8 = "345545645" # We cannot do arithmetic operations on string
# number = 345545645 * 10 / 100 - 15 + 25


# Non Primitive - Collection of Primitive Data Types

# List or Array
fruits = ["apple", "banana", "cherry"]
print(f" {fruits[0]}")
print(f" {fruits[1]} ")

# List
list_or_array_of_numbers = [1,2,3,4,5]

# Tuple
numbers_tuple = (1,2,3,4,5)

# Set
numbers_set = ((1,2,3,4,5,5,5,6,6))
((1,2,3,4,5))

# Dictionary - key and a value - primitive or non primitive
dictionary_of_person_data = {
    "name": "Shravani",
    "hobbies": ["Programming", "Teaching"],
    "interests": "Programming",
    "address": "Hyderabad",
    "Education": "Engineering"
}

# Complex
complex_1 = 3 + 4j
complex_2 = complex(10, 9)

# Print Statements
print("Booleans")
print(true_boolean)
print(false_boolean)
print("\n")
print("Integers")
print(integer_number_1)
print(integer_number_2)
print("\n")
print("Floats")
print(float_number_1)
print(float_number_2)
print(float_number_3)
print("\n")
print("Strings")
print(string_1)
print(string_2)
print(string_3)
print(string_4)
print(string_5)
print(string_6)
print(string_7)
print(string_8)
print("\n")
print("List, Tuple & Set")
print(list_or_array_of_numbers)
print(fruits)
print(numbers_tuple)
print(numbers_set)
print("\n")
print("Dictionary")
print(dictionary_of_person_data)
print("\n")
print("Complex Numbers")
print(complex_1)
print(complex_2)
