"""
Useful metacharacters in regex
\d: digit
\w: word character
\W: non-word character
\s: whitespace
\S: Non whitespace   It is very useful to use when you know a pattern doesn't contain spaces and you have reached the end when you do find one.
"""

# Import the re module
import re

sentiment_analysis = '@robot9! @robot4& I have a good feeling that the show isgoing to be amazing! @robot9$ @robot7%'

# Write a regex that matches the user mentions that starts with @ and follows the pattern, e.g. @robot3!
regex = r'@robot\d\W'

# Find all the matches of the pattern in the sentiment_analysis variable.
print(re.findall(regex, sentiment_analysis))

sentiment_analysis = "Unfortunately one of those moments wasn't a giant squid monster. User_mentions:2, likes: 9, number of retweets: 7"

# Write a regex that matches the number of user mentions given as, for example, User_mentions:9 in sentiment_analysis
print(re.findall(r"User_mentions:\d", sentiment_analysis))

# Write a regex that matches the number of likes given as, for example, likes: 5 in sentiment_analysis.
print(re.findall(r"likes:\s\d", sentiment_analysis))

# Write a regex that matches the number of retweets given as, for example, number of retweets: 4 in sentiment_analysis
print(re.findall(r"retweets:\s\d", sentiment_analysis))

# Match and split
sentiment_analysis = 'He#newHis%newTin love with$newPscrappy. #8break%He is&newYmissing him@newLalready'

# Write a regex that matches the pattern separating the sentences in sentiment_analysis, e.g. &4break!
regex_sentence = r'\W\dbreak\W'

# Replace regex_sentence with a space " " in the variable sentiment_analysis. Assign it to sentiment_sub.
sentiment_sub = re.sub(regex_sentence, ' ', sentiment_analysis)

# Write a regex that matches the pattern separating the words in sentiment_analysis, e.g. #newH.
regex_words = r'\Wnew\w'

# Replace regex_words with a space in the variable sentiment_sub. Assign it to sentiment_final and print out the result.
sentiment_final = re.sub(regex_words, ' ', sentiment_sub)
print(sentiment_final)  


# REPITITIONS

"""
? : 0 or 1 (lazy)
+ : 1 or more (greedy)
* : 0 or more (greedy)

Write a regex to find all the matches of http links appearing in each tweet in sentiment_analysis. Print out the result.
Write a regex to find all the matches of user mentions appearing in each tweet in sentiment_analysis. Print out the result
"""
sentiment_analysis = ["Boredd. Colddd @blueKnight39 Internet keeps internet at https://www.tellyourstory.com", "I had a horrible nightmare last night @anitaLopez98, @MyredHat31",
		      "im lonely  keep me company @YourBestCompany! @foxRadio"] 


for tweet in sentiment_analysis:
	# Write regex to match http links and print out result
	print(re.findall(r"https?://\w{3}.\w+.com", tweet))

	# Write regex to match user mentions and print out result
	print(re.findall(r"@\w+", tweet))
	

# extracting dates

# Complete the for-loop with a regex that finds all dates in a format similar to 27 minutes ago or 4 hours ago
sentiment_analysis = [] # content not currently availabel 
for date in sentiment_analysis:
	print(re.findall(r'\d{1,2}\s\w+\s\w+', date))
	
# Complete the for-loop with a regex that finds all dates in a format similar to 23rd june 2018

for date in sentiment_analysis:
	print(re.findall(r'\d{1,2}rd\s\w+\s\d{4}', date))
	
# Complete the for-loop with a regex that finds all dates in a format similar to 1st september 2019 17:25
for date in sentiment_analysis:
	print(re.findall(r'\d{1,2}st\s\w+\s\d{4}\s\d{1,2}:\d{2}', date))
	
# Getting Tokens

sentiment_analysis = 'ITS NOT ENOUGH TO SAY THAT IMISS U #MissYou #SoMuch #Friendship #Forever'
# Write a regex that matches the described hashtag pattern. Assign it to the regex variable.

# Write a regex matching the hashtag pattern
regex = r"#\w+"

# Replace all the matches of the regex with an empty string "". Assign it to no_hashtag variable.

# Replace the regex by an empty string
no_hashtag = re.sub(regex, '', sentiment_analysis)

# Split the text in the no_hashtag variable at every match of one or more consecutive whitespace.
# Get tokens by splitting text
print(re.split(r"\s+", no_hashtag))