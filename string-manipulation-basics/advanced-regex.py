import re
#  CAPTURING GROUPS
sentiment_analysis = ['Just got ur newsletter, those fares really are unbelievable. Write to statravelAU@gmail.com or statravelpo@hotmail.com. They have amazing prices',
 'I should have paid more attention when we covered photoshop in my webpage design class in undergrad. Contact me Hollywoodheat34@msn.net.',
 'hey missed ya at the meeting. Read your email! msdrama098@hotmail.com']

"""

    Complete the regex to match the email capturing only the name part. The name part appears before the @.
    Find all matches of the regex in each element of sentiment_analysis analysis. Assign it to the variable email_matched.
    Complete the .format() method to print the results captured in each element of sentiment_analysis analysis.

    Remember that placing a subpattern inside parenthesis will capture that content and stores it temporarily in memory. This can be later reused.
"""

regex_email = r"(\S+[A-Z0-9a-z]+?\S+)@\w+.\w+\S+"

for tweet in sentiment_analysis:
    # Find all matches of regex in each tweet
    email_matched = re.findall(regex_email, tweet)

    # Complete the format method to print the results
    print("Lists of users found in this tweet: {}".format(email_matched))


# AIRLINE code extraction
"""
Your boss assigned you to a small project. They are performing an analysis of the travels people made to attend business meetings. You are given a dataset with only the email subjects for each of the people traveling.

You learn that the text followed a pattern. Here is an example:

Here you have your boarding pass LA4214 AER-CDB 06NOV.

You need to extract the information about the flight:

    The two letters indicate the airline (e.g LA),
    The 4 numbers are the flight number (e.g. 4214).
    The three letters correspond to the departure (e.g AER),
    The destination (CDB),
    The date (06NOV) of the flight.

All letters are always uppercase.

The variable flight containing one email subject was loaded in your session. You can use print() to view it in the IPython Shell.
"""
flight = 'Subject: You are now ready to fly. Here you have your boarding pass IB3723 AMS-MAD 06OCT'

# Complete the regular expression to match and capture all the flight information required.
regex = r"([A-Z]{2})(\d{4})\s([A-Z]{3})-([A-Z]{3})\s(\d{2}[A-Z]{3})"

# Find all the matches corresponding to each piece of information about the flight. Assign it to flight_matches
flight_matches = re.findall(regex, flight)

# Complete the format method with the elements contained in flight_matches. In the first line print the airline, and the flight number. In the second line, the departure and destination. In the third line, the date.

print("Airline: {} Flight number: {}".format(flight_matches[0][0], flight_matches[0][1]))
print("Departure: {} Destination: {}".format(flight_matches[0][2], flight_matches[0][3]))
print("Date: {}".format(flight_matches[0][4]))


# ALTERNATION AND CAPTURING NON GROUPS

sentiment_analysis = ['I totally love the concert The Book of Souls World Tour. It kinda amazing!',
 'I enjoy the movie Wreck-It Ralph. I watched with my boyfriend.',
 "I still like the movie Wish Upon a Star. Too bad Disney doesn't show it anymore."]

"""

    Complete the regular expression to capture the words love or like or enjoy. Match and capture the words movie or concert. Match and capture anything appearing until the ..
    Find all matches of the regex in each element of sentiment_analysis. Assign them to positive_matches.
    Complete the .format() method to print out the results contained in positive_matches for each element in sentiment_analysis.

"""

# Write a regex that matches sentences with the optional words
regex_positive = r"(love|like|enjoy).+?(movie|concert)\s(.+?)\." #The pipe operator works by comparing everything that is to its left with everything to the right. Grouping optional patterns is the way to get the correct result.

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    positive_matches = re.findall(regex_positive, tweet)
    
    # Complete format to print out the results
    print("Positive comments found {}".format(positive_matches))


"""
Complete the regular expression to capture the words hate or dislike or disapprove. Match but don't capture the words movie or concert. Match and capture anything appearing until the ..
Find all matches of the regex in each element of sentiment_analysis. Assign them to negative_matches.
Complete the .format() method to print out the results contained in negative_matches for each element in sentiment_analysis
"""
sentiment_analysis = ['That was horrible! I really dislike the movie The cabin and the ant. So boring.',
 "I disapprove the movie Honest with you. It's full of cliches.",
 'I dislike very much the concert After twelve Tour. The sound was horrible.']


# Write a regex that matches sentences with the optional words
regex_negative = r"(hate|dislike|disapprove).+?(?:movie|concert)\s(.+?)\." #Non-capturing groups are very often used together with alternation. Sometimes you have optional patterns and you need to group them. However you are not interested in keeping them. It's a nice feature of regex.

for tweet in sentiment_analysis:
	# Find all matches of regex in tweet
    negative_matches = re.findall(regex_negative, tweet)
    
    # Complete format to print out the results
    print("Negative comments found {}".format(negative_matches))


# BACK REFERENCING

# Numbered groups
text = 'Python 3.0 was released on 12-03-2008'
information = re.search(r'(\d{1,2})-(\d{2})-(\d{4})', text)
print(information.group(3))
print(information.group(0))
#.group() only be used with .search() and .match()

# Named groups
text = 'Austine, 78701'
cities = re.search(r'(?P<city>[A-Za-z]+).*?(?P<code>\d{4})', text)
print(cities.group('city'))
print(cities.group('code'))

# Using capturing groups for backreferencing

# Using numbered capturing groups to reference back
sentence = 'I wish you a happy happy birthday!'
print(re.findall(r'(\w+)\s\1', sentence))

# Using numbered capturing groups to replace a string
print(re.sub(r'(\w+)\s\1', r'\1', sentence))

# Using named capturing groups to reference back
sentence = 'Your new code number is 23434. Please, enter 23434 to open the door'
print(re.findall(r'(?P<code>\d{5}).*?\s(?P=code)', sentence))


# Using named capturing groups to replace a string
sentence = "This app is not working! It's repeating the last word word"
print(re.sub(r'(?P<txt>\w+)\s(?P=txt)', r'\g<txt>', sentence))


# Parsing PDF Files
"""
You now need to work on another small project you have been delaying. Your company gave you some PDF files of signed contracts. The goal of the project is to create a database with the information you parse from them. Three of these columns should correspond to the day, month, and year when the contract was signed.
The dates appear as Signed on 05/24/2016 (05 indicating the month, 24 the day). You decide to use capturing groups to extract this information. Also, you would like to retrieve that information so you can store it separately in different variables.

You decide to do a proof of concept
"""

contract = 'Provider will invoice Client for Services performed within 30 days of performance.  Client will pay Provider as set forth in each Statement of Work within 30 days of receipt and acceptance of such invoice. It is understood that payments to Provider for services rendered shall be made in full as agreed, without any deductions for taxes of any kind whatsoever, in conformity with Provider’s status as an independent contractor. Signed on 03/25/2001.'

# Write a regex that captures the month, day, and year in which the contract was signed. Scan contract for matches
regex_dates = r"Signed\son\s(\d{2})/(\d{2})/(\d{4})"
dates = re.search(regex_dates, contract)

# Assign each captured group to the corresponding keys in the dictionary.

signature = {
	"day": dates.group(2),  #Remember that each capturing group is assigned a number according to its position in the regex. Only if you use .search() and .match(), you can use .group() to retrieve the groups.
	"month": dates.group(1),
	"year": dates.group(3)
}

# Complete the positional method to print out the captured groups. Use the values corresponding to each key in the dictionary.
print("Our first contract is dated back to {data[year]}. Particularly, the day {data[day]} of the month {data[month]}.".format(data=signature))

# Close the tag, please!
"""
In the meantime, you are working on one of your other projects. The company is going to develop a new product. It will help developers automatically check the code they are writing. You need to write a short script for checking that every HTML tag that is open has its proper closure.

You have an example of a string containing HTML tags:

<title>The Data Science Company</title>

You learn that an opening HTML tag is always at the beginning of the string. It appears inside <>. A closing tag also appears inside <>, but it is preceded by /.

You also remember that capturing groups can be referenced using numbers, e.g \4.
"""

html_tags = ['<body>Welcome to our course! It would be an awesome experience</body>',
 '<article>To be a data scientist, you need to have knowledge in statistics and mathematics</article>',
 '<nav>About me Links Contact me!']

"""
    Complete the regex in order to match closed HTML tags. Find if there is a match in each string of the list html_tags. Assign the result to match_tag.
    If a match is found, print the first group captured and saved in match_tag.
    If no match is found, complete the regex to match only the text inside the HTML tag. Assign it to notmatch_tag.
    Print the first group captured by the regex and save it in notmatch_tag.
"""

for string in html_tags:
    # Complete the regex and find if it matches a closed HTML tags
    match_tag =  re.match(r"<(\w+)>.*?</\1>", string)
 
    if match_tag:
        # If it matches print the first group capture
        print("Your tag {} is closed".format(match_tag.group(1))) 
    else:
        # If it doesn't match capture only the tag 
        notmatch_tag = re.match(r"<(\w+)>", string)
        # Print the first group capture
        print("Close your {} tag!".format(notmatch_tag.group(1)))
# Backreferences are very helpful when you need to reuse part of the regex match inside the regex. Knowing when and how to use them will simplify many of your tasks!


# Reeepeated characters

"""
Back to your sentiment analysis! Your next task is to replace elongated words that appear in the tweets. We define an elongated word as a word that contains a repeating character twice or more times. e.g. "Awesoooome".

Replacing those words is very important since a classifier will treat them as a different term from the source words lowering their frequency.

To find them, you will use capturing groups and reference them back using numbers. E.g \4.

If you want to find a match for Awesoooome. You first need to capture Awes. Then, match o and reference the same character back, and then, me.


Complete the regular expression to match an elongated word as described.
Search the elements in sentiment_analysis list to find out if they contain elongated words. Assign the result to match_elongated.
Assign the captured group number zero to the variable elongated_word.
Print the result contained in the variable elongated_word
"""

sentiment_analysis = ['@marykatherine_q i know! I heard it this morning and wondered the same thing. Moscooooooow is so behind the times',
 'Staying at a friends house...neighborrrrrrrs are so loud-having a party',
 'Just woke up an already have read some e-mail']

regex_elongated = r'\w*(\w)\1\w*'

for tweet in sentiment_analysis:
	# Find if there is a match in each tweet 
	match_elongated = re.search(regex_elongated, tweet)
	
	if match_elongated:
		# Assign the captured group zero 
		elongated_word = match_elongated.group(0)
        
		# Complete the format method to print the word
		print("Elongated word found: {word}".format(word=elongated_word))
	else:
		print("No elongated word found") 


# LOOKAROUND

# Look around allow us to confirm that sub-pattern is behind or ahead main pattern

# Look ahead
    #  it is a non capturing group
    # checks that the first part of the expression is followed or not by the lookahead expression
    # as a consequence, it will return only the first part of the expression
    # the lookahead expression can either be positive or negative
    # for positive we use (?=txt)
    # for negative we use (?!txt)

# Positive lookahead
my_text = 'tweets.txt transferred, mypass.txt transferred, keywords.txt error'
# extracts the words followed by transferred
print(re.findall(r'\w+\.*?\w+?(?=\stransferred)', my_text))

# Negative lookahead

# extracts the matches that are not followed by transferred
print(re.findall(r'\w+\.txt(?!\stransferred)', my_text))

# LOOKBEHIND
        #  non capturing group
        #  get all the matches that are preceded or not by a specific pattern
        # as a consequnce, returns pattern after looking behind expression
        # it can also be positive or negative
        #  positive = (?<=txt)
        # negative = (?<!txt)

my_text = 'Member: Angus Young, Member: Chris Slade, Past: Malcom Young, Past: Cliff Williams.'

# Positive lookbehind
# Find all matches of the name that are preceded by the word Member:
print(re.findall(r'(?<=Member:\s)\w+\s\w+', my_text))

# Negative lookbehind
# Find all matches of the name that are not preceded by the word brown
my_text = 'My white cat sat at the table. However, my brown dog was lying on the couch.'
print(re.findall(r'(?<!brown\s)(cat|dog)', my_text))

# Surrounding word

"""
Now, you want to perform some visualizations with your sentiment_analysis dataset. You are interested in the words surrounding python. You want to count how many times a specific word appears right before and after it.

Positive lookahead (?=) makes sure that first part of the expression is followed by the lookahead expression. Positive lookbehind (?<=) returns all matches that are preceded by the specified pattern.
"""
sentiment_analysis = 'You need excellent python skills to be a data scientist. Must be! Excellent python'

# Get all the words that are followed by the word python in sentiment_analysis. Print out the word found.

look_ahead = re.findall(r"\w+(?=\spython)", sentiment_analysis)

# Print out
print(look_ahead)

# Get all the words that are preceded by the word python or Python in sentiment_analysis. Print out the words found.
look_behind = re.findall(r"(?<=[Pp]ython\s)\w+", sentiment_analysis)

# Print out
print(look_behind)


# Filtering phone numbers
"""
Now, you need to write a script for a cell-phone searcher. It should scan a list of phone numbers and return those that meet certain characteristics.

The phone numbers in the list have the structure:

    Optional area code: 3 numbers
    Prefix: 4 numbers
    Line number: 6 numbers
    Optional extension: 2 numbers

E.g. 654-8764-439434-01.

You decide to use .findall() and the non-capturing group's negative lookahead (?!) and negative lookbehind (?<!)
"""

cellphones = ['4564-646464-01', '345-5785-544245', '6476-579052-01']

# Get all cell phones numbers that are not preceded by the optional area code.
for phone in cellphones:
	# Get all phone numbers not preceded by area code
	number = re.findall(r"(?<!\d{3}-)\d{4}-\d{6}-\d{2}", phone)
	print(number)
        
# Get all the cell phones numbers that are not followed by the optional extension.
for phone in cellphones:
	# Get all phone numbers not followed by optional extension
	number = re.findall(r"\d{3}-\d{4}-\d{6}(?!-\d{2})", phone)
	print(number)

# Negative lookarounds work in a similar way to positive lookarounds. They are very helpful when we are looking to exclude certain patterns from our analysis


