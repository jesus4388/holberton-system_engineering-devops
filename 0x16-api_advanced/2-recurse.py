#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed"""
import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'from': 'jesushernandez1843@gmail.com'
    }


def recurse(subreddit, hot_list=[]):
    """function return the hot"""
    if type(subreddit) is not list:
        url = "http://www.reddit.com/r/{}/hot.json".format(subreddit)
    else:
        url = "http://www.reddit.com/r/{}/hot.json?after={}".format(
            subreddit[0], subreddit[1])

    try:
        response = requests.get(url, headers=headers)
        response = response.json()
        dat = response['data']['children']
        for dic in dat:
            ti = dic.get('data')
            hot_list.append(ti.get('title'))
        if response['data']['after'] is None:
            return hot_list
        else:
            before = dat[0]['data']['subreddit']
            after = response['data']['after']
            return recurse([before, after], hot_list)
    except Exception:
        return None
