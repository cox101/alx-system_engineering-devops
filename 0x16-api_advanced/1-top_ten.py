#!/usr/bin/python3
"""function that queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""

import requests

def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print(None)
        return

    data = response.json()
    posts = data['data']['children']

    if not posts:
        print(None)
        return

    print("Top 10 hot posts in r/" + subreddit + ":\n")
    for post in posts:
        print(post['data']['title'])
