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
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    try:
        response = get(endpoint, headers=headers, allow_redirects=False)
        data = response.json()
        if 'data' in data and 'children' in data.get('data'):
            children = data.get('data').get('children')
            for post in children:
                print(post.get('data').get('title'))
    except Exception:
        print("None")
        # Return 0 if there's an error
        return 0
