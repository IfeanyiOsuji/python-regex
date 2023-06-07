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
my_message = "If you are interested in {data[field]}, you can take the course related to {data[tool]}"

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