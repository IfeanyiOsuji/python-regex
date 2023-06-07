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
^ : start of a sting
$ : end of a string
\ : escape character
| : OR operator
[]: Set of characters
[^]: transforms the expression to negative i.e not included
. : The dot . metacharacter is very useful when we want to match all repetitions of any character. However, we need to be very careful how we use it.

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

# Finding files
"""
You are not satisfied with your tweets dataset cleaning. There are still extra strings that do not provide any sentiment. Among them are strings that refer to text file names.

You also find a way to detect them:

    They appear at the start of the string.
    They always start with a sequence of 2 or 3 upper or lowercase vowels (a e i o u).
    They always finish with the txt ending.

You are not sure if you should remove them directly. So you write a script to find and store them in a separate dataset. 


    Write a regex that matches the pattern of the text file names, e.g. aemyfile.txt.
    Find all matches of the regex in the elements of sentiment_analysis. Print out the result.
    Replace all matches of the regex with an empty string "". Print out the result.

"""
sentiment_analysis = ["AIshadowhunters.txt aaaaand back to my literature", "ouMYTAXES.txt I am worried that I won't get my taxes"]

# Write a regex to match text file name
regex = r"[AEIOUaeiou]{2,3}\w+\.txt"

for text in sentiment_analysis:
	# Find all matches of the regex
	print(re.findall(regex, text))
    
	# Replace all matches with empty string
	print(re.sub(regex, '', text))


#  VALID EMAILS
"""
A colleague has asked for your help! When a user signs up on the company website, they must provide a valid email address.
The company puts some rules in place to verify that the given email address is valid:

    The first part can contain:
        Upper A-Z or lowercase letters a-z
        Numbers
        Characters: !, #, %, &, *, $, .
    Must have @
    Domain:
        Can contain any word characters
        But only .com ending is allowed

The project consists of writing a script that checks if the email address follow the correct pattern. Your colleague gave you a list of email addresses as examples to test.



    Write a regular expression to match valid email addresses as described.
    Match the regex to the elements contained in emails.
    To print out the message indicating if it is a valid email or not, complete .format() statement.

"""
emails = ['n.john.smith@gmail.com', '87victory@hotmail.com', '!#mary-=@msca.net']

# Write a regex to match a valid email address
regex = r"[0-9A-Za-z!#%&*$.]+@[a-z]+\.com"

for example in emails:
  	# Match the regex to the string
    if re.match(regex, example):
        # Complete the format method to print out the result
      	print("The email {email_example} is a valid email".format(email_example=example))
    else:
      	print("The email {email_example} is invalid".format(email_example=example)) 



# INVALID PASSWORDS
"""
The second part of the website project is to write a script that validates the password entered by the user. The company also puts some rules in order to verify valid passwords:

    It can contain lowercase a-z and uppercase letters A-Z
    It can contain numbers
    It can contain the symbols: *, #, $, %, !, &, .
    It must be at least 8 characters long but not more than 20

Your colleague also gave you a list of passwords as examples to test.


    Write a regular expression to check if the passwords are valid according to the description.
    Search the elements in the passwords list to find out if they are valid passwords.
    To print out the message indicating if it is a valid password or not, complete .format() statement.

"""
passwords = ['Apple34!rose', 'My87hou#4$', 'abc123']

regex = r"[0-9a-zA-Z*#$%!&.]{8,20}"

for example in passwords:
  	# Scan the strings to find a match
    if re.match(regex, example):
        # Complete the format method to print out the result
      	print("The password {pass_example} is a valid password".format(pass_example=example))
    else:
      	print("The password {pass_example} is invalid".format(pass_example=example)) 


# Greedy and Non Greedy characters
"""
Write a regex expression to replace HTML tags with an empty string.
Print out the result.
""" 
string = 'I want to see that <strong>amazing show</strong> again!'

# Write a regex to eliminate tags
string_notags = re.sub(r"<.+?>", "", string)

# Print out the result
print(string_notags)

sentiment_analysis = 'Was intending to finish editing my 536-page novel manuscript tonight, but that will probably not happen. And only 12 pages are left '

# Use a lazy quantifier to match all numbers that appear in the variable sentiment_analysis.

# Write a lazy regex expression 
numbers_found_lazy = re.findall(r"\d+?", sentiment_analysis)

# Print out the result
print(numbers_found_lazy)

# Now, use a greedy quantifier to match all numbers that appear in the variable sentiment_analysis.
# Write a greedy regex expression 
numbers_found_greedy = re.findall(r"\d+", sentiment_analysis)

# Print out the result
print(numbers_found_greedy)


sentiment_analysis = "Put vacation photos online (They were so cute) a few yrs ago. PC crashed, and now I forget the name of the site (I'm crying). "

# Use a greedy quantifier to match text that appears within parentheses in the variable sentiment_analysis
# Write a greedy regex expression to match 
sentences_found_greedy = re.findall(r"\(.+\)", sentiment_analysis)

# Print out the result
print(sentences_found_greedy)


# Now, use a lazy quantifier to match text that appears within parentheses in the variable sentiment_analysis.
# Write a lazy regex expression
sentences_found_lazy = re.findall(r"\(.*?\)", sentiment_analysis)

# Print out the results
print(sentences_found_lazy)