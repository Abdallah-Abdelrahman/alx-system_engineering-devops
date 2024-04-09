#!/usr/bin/python3
'''Query the Reddit API and returns a list,
containing the titles of all hot articles for a given subreddit

Attrs:
    BASE_URL(str): reddit url
'''
from requests import get

BASE_URL = 'https://www.reddit.com'


def recurse(subreddit, hot_list=[], idx=0, after=None):

    '''queries the Reddit API and prints the titles of all hot articles

    Args:
        subreddit(str): subreddit to query
        hot_list(List(dict)): optoinal list hot posts
        idx(int): index of the current article
        after(None|str): optoinal argument to paginate to next page
    '''

    # Limit to the first 10 hot posts
    endpoint = "{}/r/{}/hot.json".format(BASE_URL, subreddit)
    if after:
        endpoint += '?after={}'.format(after)
    # Custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'MyBot/0.1'}
    try:
        resp = get(endpoint, headers=headers, allow_redirects=False)

        if not (200 <= resp.status_code <= 299):
            # status is not success
            print(None)
            return
        data = resp.json()
        if 'data' in data and 'children' in data.get('data'):
            children = data.get('data').get('children')
            after = data.get('data').get('after')
            print_titles(hot_list=children)
            '''
            for post in children:
                print(post.get('data').get('title'))
            '''
            if after:
                recurse(subreddit, hot_list=hot_list, idx=idx, after=after)
    except Exception:
        print(None)


def print_titles(hot_list=[], idx=0):
    '''print title of article '''
    if len(hot_list) and len(hot_list) - 1 != idx:
        print(hot_list[idx].get('data').get('title'))
        print_titles(hot_list=hot_list, idx=idx+1)
