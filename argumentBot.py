import praw

reddit = praw.Reddit(
    client_id="xrG77qJmbHnfCidPdzlqyg",
    client_secret="eW8q71to5VC364c94SxxvLqu3AYsVA",
    user_agent="<console:ARGUMENT:1.0>",
)

subreddit = reddit.subreddit('rarepuppers')
