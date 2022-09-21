#!/usr/bin/python3
"""prints the titles of the first 10 hot posts listed"""

import requests

headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)\
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        'from': 'jesushernandez1843@gmail.com'
    }


def top_ten(subreddit):
    """function return the first 10"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    try:
        response = requests.get(url, headers=headers)
        response = response.json()
        data = response['data']['children']

        count = 0
        for dic in data:
            ti = dic.get('data')
            print(ti.get('title'))
            count += 1
            if count == 9:
                break

    except Exception:
        print('None')
            
    

