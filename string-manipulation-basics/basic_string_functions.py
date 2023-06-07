
movie = 'fox and kelley soon become bitter rivals because the new fox books store is opening up right across the block from the small business .'

#find the length
print(len(movie))

# Select the first 32 characters of the variable movie1 and assign it to the variable first_part
first_part = movie[:32]
print(first_part)

movie1 = 'the most significant tension of _election_ is the potential relationship between a teacher and his student .'
# Select the substring going from the 43rd character to the end of movie1. Assign it to the variable last_part.
last_part = movie1[42:]
print(last_part)
movie2 = 'the most significant tension of _rushmore_ is the potential relationship between a teacher and his student .'
# Select the substring going from the 33rd to the 42nd character of movie2. Assign it to the variable middle_part.
middle_part = movie2[31:42]
print(middle_part)

# Print the concatenation of the variables first_part, middle_part and last_part in that order. Print the variable movie2 and compare them
print(first_part+middle_part+last_part) 
print(movie2)

# PALLINDROME
movie = 'oh my God! desserts I stressed was an ugly movie'
"""
    Extract the substring from the 12th to the 30th character from the variable movie which corresponds to the movie title. Store it in the variable movie_title.
    Get the palindrome by reversing the string contained in movie_title.
    Complete the code to print out the movie_title if it is a palindrome.
"""
movie_title = movie[11:30]
pallindrome = movie_title[::-1]
print(movie_title == pallindrome)

# String OPERATIONS
movie = '$I supposed that coming from MTV Films I should expect no less$'
# Convert the string in the variable movie to lowercase. Print the result.
print(movie.lower())
"""Remove the $ that occur at the start and at the end of the string contained in movie_lower. Print the results.
"""
movie_lower = movie.lower()
movie_no_sign = movie_lower.strip('$') # using .strip()
print(movie_no_sign)

# Split the string contained in movie_no_sign into as many substrings as possible. Print the results.
print(movie_no_sign.split())
# To get the root of the second word contained in movie_split, select all the characters except the last one.
movie_split = movie_no_sign.split();
print(movie_split[1][:-1])

#  JOINING Strings
movie = 'the film,however,is all good<\\i>'
# Remove tag <\i> from the end of the string. Print the results.
movie_tag = movie.strip('<\i>')
print(movie_tag)

# Split the string contained in movie_tag using the commas as a separating element. Print the results.
movie_no_comma = movie_tag.split(',')
print(movie_no_comma)

# Join back together the list of substring contained in movie_no_comma using a space as a join element. Print the results.
movie_join = ' '.join(movie_no_comma)
print(movie_join)

# Using .linesplit() for splitting strings based on new line
file = 'mtv films election, a high school comedy, is a current example\nfrom there, director steven spielberg wastes no time, taking us into the water on a midnight swim'
"""
    Split the string file into many substrings at line boundaries.
    Print out the resulting variable file_split.
    Complete the for-loop to split the strings into many substrings using commas as a separator element.
"""
# Split string at line boundaries
file_split = file.splitlines()

# Print file_split
print(file_split)

# Complete for-loop to split by commas
for substring in file_split:
    substring_split = substring.split(',')
    print(substring_split)


#  FINDING AND REPLACING
movies = ["it's clear that he's passionate about his believe","I believe you I always said that the actor actor", "it's astonishing how frightening the actor actor"]
"""
    Find if the substring actor occurs between the characters with index 37 and 41 inclusive. If it is not detected, print the statement Word not found.
    Replace actor actor with the substring actor if actor occurs only two repeated times.
    Replace actor actor actor with the substring actor if actor appears three repeated times.
"""
for movie in movies:
  	# If actor is not found between character 37 and 41 inclusive
    # Print word not found
    if movie.find("actor", 37, 42) == -1:
        print("Word not found")
    # Count occurrences and replace two with one
    elif movie.count("actor") == 2:  
        print(movie.replace("actor actor", "actor"))
    else:
        # Replace three occurrences with one
        print(movie.replace("actor actor actor", "actor"))

movies = ["heck , jackie doesn't even have enough money for me", "in condor , chan plays the same character he's in others"]
# Find the index where money occurs between characters with index 12 and 50. If not found, the method should return -1.
for movie in movies:
  # Find the first occurrence of word
  print(movie.find('money', 12, 51))

# Find the index where money occurs between characters with index 12 and 50. If not found, it should raise an error.
for movie in movies:
  try:
    # Find the first occurrence of word
  	print(movie.index('money', 12, 51))
        
  except ValueError:
    print("substring not found")
