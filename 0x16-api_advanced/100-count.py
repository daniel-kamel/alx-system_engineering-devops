#!/usr/bin/python3
"""Module for querying the Reddit API"""
import requests


def count_words(subreddit, word_list, after=None, word_count=None):
    """
    Recursively queries the Reddit API, parses the titles of hot articles,
    and prints a sorted count of given keywords
    """
    if word_count is None:
        word_count = {}
        for word in word_list:
            word = word.lower()
            if word not in word_count:
                word_count[word] = 0

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
                title = post['data']['title'].lower().split()
                for word in word_count:
                    word_count[word] += title.count(word)

            after = data['data']['after']

            if after:
                return count_words(subreddit, word_list, after, word_count)

            sorted_counts = sorted(
                word_count.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
            return
        else:
            return

    except Exception:
        return
