#!/usr/bin/python3
'''Query the Reddit API and prints the titles of the first 10 hot posts

Attrs:
    BASE_URL(str): reddit url
'''
from requests import get

BASE_URL = 'https://www.reddit.com'


def top_ten(subreddit):

    '''queries the Reddit API and prints the titles of the first 10 hot posts

    Args:
        subreddit(str): subreddit to query
    '''

    # Limit to the first 10 hot posts
    endpoint = "{}/r/{}/hot.json?limit=10".format(BASE_URL, subreddit)
    # Custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'MyBot/0.1'}
    try:
        resp = get(endpoint, headers=headers, allow_redirects=False)
        data = resp.json()
        if not (200 <= resp.status_code <= 299):
            # status is not success
            print(None)
            return
        if 'data' in data and 'children' in data.get('data'):
            children = data.get('data').get('children')
            for post in children:
                print(post.get('data').get('title'))
        else:
            print(None)
    except Exception:
        print(None)
