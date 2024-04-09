#!/usr/bin/python3
'''Query the Reddit API and returns the number of subscribers'''
from requests import get


def number_of_subscribers(subreddit):
    '''query the number of subuscribers for a given subreddit

    Args:
        subreddit(str): subreddit to query

    Returns:
        number of subscribers
    '''

    url = "https://www.reddit.com/r/{subreddit}/about.json".format(subreddit)
    # Custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    try:
        response = get(url, headers=headers, allow_redirects=False)
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        # Return 0 if there's an error
        return 0
