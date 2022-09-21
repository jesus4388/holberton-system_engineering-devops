#!/usr/bin/python3
"""how many subs?"""
import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'from': 'jesushernandez1843@gmail.com'
    }


def number_of_subscribers(subreddit):
    """function return users"""
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    try:
        response = requests.get(url, headers=headers)
        response = response.json()
        data = response['data']
        return data['subscribers']
    except Exception:
        return 0
