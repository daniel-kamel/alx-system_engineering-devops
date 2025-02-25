#!/usr/bin/python3
"""Module for querying the Reddit API"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Returns a list of titles of all hot articles for a given subreddit"""
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    params = {'after': after} if after else {}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    try:
        response = requests.get(
            url, headers=headers, params=params, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            posts = data['data']['children']

            for post in posts:
                hot_list.append(post['data']['title'])

            after = data['data']['after']

            if after:
                return recurse(subreddit, hot_list, after)
            return hot_list
        else:
            return None

    except Exception:
        return None
