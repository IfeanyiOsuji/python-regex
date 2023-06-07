# Using placeholders
wikipedia_article = 'In computer science, artificial intelligence (AI), sometimes called machine intelligence, is intelligence demonstrated by machines, in contrast to the natural intelligence displayed by humans and animals.'
"""
Assign the substrings going from the 4th to the 19th character inclusive, and from the 22nd to the 44th character inclusive of wikipedia_article to the variables first_pos and second_pos, respectively. 
Adjust the strings to be lowercase.
"""
# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()

"""
Define a string with the text "The tool is used in" adding placeholders after the word tool and the word in for future positional formatting. Append it to the list my_list.
"""
my_list = []
# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()

# Define string with placeholders 
my_list.append('The tool {} is used in {}')

"""
Define a string with the text "The tool is used in" adding placeholders after the word tool and in but reorder them so the second argument passed to the method will replace the first placeholder. Append to the list my_list.
"""
# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()

# Define string with placeholders 
my_list.append("The tool {} is used in {}")

# Define string with rearranged placeholders
my_list.append("The tool {1} is used in {0}")

"""
Complete the for-loop so that it uses the .format() method and the variables first_pos and second_pos to print out every string in my_list.
"""
# Assign the substrings to the variables
first_pos = wikipedia_article[3:19].lower()
second_pos = wikipedia_article[21:44].lower()

# Define string with placeholders 
my_list.append("The tool {} is used in {}")

# Define string with rearranged placeholders
my_list.append("The tool {1} is used in {0}")

# Use format to print strings
for my_string in my_list:
  	print(my_string.format(first_pos, second_pos))
	
#  Using named PLACEHOLDERS
courses = ['artificial intelligence', 'neural networks']
"""
Create a dictionary assigning the first and second element appearing in the list courses to the keys "field" and "tool" respectively.
"""
# Create a dictionary
plan = {
  		'field': courses[0],
        'tool': courses[1]
        }

"""
    Complete the placeholders accessing inside to the elements linked with the keys field and tool in the dictionary data.
    Print out the resulting message using the .format() method, passing the plan dictionary to replace the data placeholders.
"""
# Complete the placeholders accessing elements of field and tool keys in the data dictionary
my_message = "If you are interested in {data[field]}, you can take the course related to {data[tool]}" #values in a list or dictionary are accessed without quatation marks

# Use the plan dictionary to replace placeholders
print(my_message.format(data=plan))


# Using named placeholders and format specifiers
"""
    Import the function datetime from the module datetime .
    Obtain the date of today and assign it to the variable get_date.
    Complete the string message by adding to the placeholders named today and the format specifiers to format the date as month_name day, year and time as hour:minutes.
    Print the message using the .format() method and the variable get_date to replace the named placeholder.
"""
# Import datetime 
from datetime import datetime

# Assign date to get_date
get_date = datetime.now()

# Add named placeholders with format specifiers
message = "Good morning. Today is {today:%B %d, %Y}. It's {today:%H:%M} ... time to work!"

# Use the format method replacing the placeholder with get_date
print(message.format(today=get_date))


# Using String literals
field1 = 'sexiest job'
field2 = 'data is produced daily'
field3 = 'Individuals'
fact1 = 21
fact2 = 2500000000000000000
fact3 = 72.41415415151
fact4 = 1.09

# Complete the f-string to include the variable field1 with quotes and the variable fact1 as a digit.
# Complete the f-string
print(f"Data science is considered {field1!r} in the {fact1}st century")

# Complete the f-string to include the variable fact2 using exponential notation, and the variable field2
# Complete the f-string
print(f"About {fact2:e} of {field2} in the world")

# Complete the f-string to include field3, fact3 rounded to 2 decimals, and fact4 rounded to one decimal.
# Complete the f-string
print(f"{field3} create around {fact3:.2f}% of the data but only {fact4:.1f}% is analyzed")

# making functions
import datetime as dt
number1 = 120
number2 = 7
string1 = 'httpswww.datacamp.com'
list_links = ['www.news.com',
 'www.google.com',
 'www.yahoo.com',
 'www.bbc.com',
 'www.msn.com',
 'www.facebook.com',
 'www.news.google.com']
# Inside the f-string, include number1,number2 and the result of dividing number1 by number2 rounded to one decimal.

# Include both variables and the result of dividing them 
print(f"{number1} tweets were downloaded in {number2} minutes indicating a speed of {number1/number2:.1f} tweets per min")

# Inside the f-string, use .replace() to replace the substring https with an empty substring in string1.

# Replace the substring https by an empty string
print(f"{string1.replace('https', '')}")

# Inside the f-string, get list_links length, multiply it by 100 and divide it by 120. Round the result to two decimals.

# Divide the length of list by 120 rounded to two decimals
print(f"Only {((len(list_links)*100)/120):.2f}% of the posts contain links")

# accessing values with quatation in f strings unlike .format()
east = {'date': dt.datetime(2007, 4, 20, 0, 0), 'price': 1232443}
west = {'date': dt.datetime(2006, 5, 26, 0, 0), 'price': 1432673}

# Inside the f-string, access the values of the keys price and date in east dictionary. Format the date to month-day-year.
# Access values of date and price in east dictionary
print(f"The price for a house in the east neighborhood was ${east['price']} in {east['date']:%m-%d-%Y}")

# Inside the f-string, access the values of the keys price and date in west dictionary. Format the date to month-day-year.

# Access values of date and price in west dictionary
print(f"The price for a house in the west neighborhood was ${west['price']} in {west['date']:%m-%d-%Y}.")