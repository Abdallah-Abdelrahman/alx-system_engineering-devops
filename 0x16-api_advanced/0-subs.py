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

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    # Custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64)'}
    try:
        response = get(url, headers=headers)
        data = response.json()
        if 'data' in data and 'subscribers' in data['data']:
            return data['data']['subscribers']
        return 0
    except Exception as e:
        print(f"An error occurred: {e}")
        # Return 0 if there's an error during the
        return 0


if __name__ == '__main__':
    import sys
    print(number_of_subscribers(sys.argv[1]))
