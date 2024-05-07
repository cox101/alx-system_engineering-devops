
#!/usr/bin/python3
"""recursive function that queries the Reddit API and returns
 a list containing the titles of all hot articles for a given subreddit. """

import requests

def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    params = {'limit': 100}
    if after:
        params['after'] = after

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json()
    posts = data['data']['children']
    
    if not posts:
        return hot_list if hot_list else None
    
    for post in posts:
        hot_list.append(post['data']['title'])

    after = data['data']['after']
    if after:
        return recurse(subreddit, hot_list, after)
    else:
        return hot_list
