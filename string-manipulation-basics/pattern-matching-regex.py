"""
Useful metacharacters in regex
\d: digit
\w: word character
\W: non-word character
\s: whitespace
\S: Non whitespace
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