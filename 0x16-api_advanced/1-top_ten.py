#!/usr/bin/python3
"""
Queries the Reddit API and prints the
titles of the first 10 hot posts listed
for a given subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the
    titles of the first 10 hot posts listed
    for a given subreddit.
    """
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {'limit': 10}

    try:
        response = requests.get(url, headers=headers,
                                params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']
            for post in posts:
                print(post['data']['title'])
        else:
            print("None")

    except Exception:
        print("None")
