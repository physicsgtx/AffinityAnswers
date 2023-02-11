import re

def profanity_score(tweet, slurs):
    score = 0
    words = re.findall(r'\b\w+\b', tweet)
    for word in words:
        if word.lower() in slurs:
            score += 1
    return score

def calculate_profanity(filename, slurs):
    with open(filename, 'r') as file:
        tweets = file.readlines()
        
    scores = {}
    for tweet in tweets:
        scores[tweet.strip()] = profanity_score(tweet, slurs)
    
    return scores

slurs = ['racism', 'bigotry', 'prejudice', 'xenophobia']
filename = 'tweets.txt'
profanity_scores = calculate_profanity(filename, slurs)

for tweet, score in profanity_scores.items():
    print(f'{tweet}: {score}')

#Assumptions:

#The input file tweets.txt contains one tweet per line.
#The list of slurs provided are all lowercase.
#The profanity score for a tweet is simply the number of times a word from the slurs list appears in the tweet.
#The tweet strings in the file are stripped of any leading/trailing white spaces.
#The words in the tweets are separated by spaces.
#The re module is used to extract the words from the tweets. The regular expression \b\w+\b is used to match words.
