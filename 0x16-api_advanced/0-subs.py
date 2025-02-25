#!/usr/bin/python3
"""
Queries the Reddit API and returns the number of
subscribers (not active users, total subscribers)
for a given subreddit. If an invalid subreddit is
given, the function should return 0.
"""
import requests


def number_of_subscribers(subreddit):
  url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
  headers = {
      'User-Agent': 'My User Agent 1.0'
  }
  response = requests.get(url, headers=headers)
  subscribers = response.json().get('data').get('subscribers')
  if response.status_code != 200 or subscribers is None:
      return 0
  return subscribers
