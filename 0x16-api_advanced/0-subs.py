#!/usr/bin/python3
'''Query the Reddit API and returns the number of subscribers

Attrs:
    BASE_URL(str): url for reddit
'''
from requests import get

BASE_URL = 'https://www.reddit.com'


def number_of_subscribers(subreddit):
    '''query the number of subuscribers for a given subreddit

    Args:
        subreddit(str): subreddit to query

    Returns:
        number of subscribers
    '''

    url = "{}/r/{}/about.json".format(BASE_URL, subreddit)
    # Custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'Chrome/120.0.0.0'}

    try:
        resp = get(url, headers=headers, allow_redirects=False)
        if not (200 <= resp.status_code <= 299):
            # status is not success
            return 0
        data = resp.json()
        if 'data' in data and 'subscribers' in data.get('data'):
            return data.get('data').get('subscribers')
    except Exception:
        return 0
