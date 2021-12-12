import praw
import time
import operator

reddit = praw.Reddit(
    client_id="xrG77qJmbHnfCidPdzlqyg",
    client_secret="eW8q71to5VC364c94SxxvLqu3AYsVA",
    user_agent="<console:ARGUMENT:1.0>",
    username='kia-argument-bot',
    password='hujzod-1dazqa-foKsis'
)

subreddit = reddit.subreddit('MemePiece')

number_of_comments_checked = 0
number_of_comments_found = 0

def isInReverseAlphabeticalOrder(stringToParse):
    X = stringToParse.split(' ')
    words = [word.lower() for word in X]
    return words ==''.join(sorted(words, reverse=True))


for submission in subreddit.hot():
    for comment in submission.comments:
        if hasattr(comment, "body"): #some comments do not have bodies, only print if there is a body
            comment_lower = comment.body.lower()
            if isInReverseAlphabeticalOrder(comment_lower):
                number_of_comments_found += 1
                comment.reply('Wow, your comment is in reverse alphabetical order, only '+ str(number_of_comments_found) + ' comments out of ' + str(number_of_comments_checked) + ' has this attribute!')
                time.sleep(660) #sleep for 11 minutes, reddit does not let you spam, 10 minute limit
                print('posted!\n')
            number_of_comments_checked += 1
    #print('**************************')



