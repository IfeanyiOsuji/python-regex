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


