#!/usr/bin/python3
'''Query the Reddit API.

Attrs:
    BASE_URL(str): reddit url
'''
from re import findall
from requests import get

BASE_URL = 'https://www.reddit.com'


def count_words(subreddit, word_list, count={}, after=None):

    '''queries the Reddit API.
    and prints the count of all keywords found in the titles of hot articles

    Args:
        subreddit(str): subreddit to query
        word_list(List(str)): key words to search for
        hot_list(List(dict)): optoinal list hot posts
        count(dict): dictionary contains all the key words count
        after(None|str): optoinal argument to paginate to next page
    '''

    endpoint = "{}/r/{}/hot.json".format(BASE_URL, subreddit)
    if after:
        endpoint += '?after={}'.format(after)
    # Custom User-Agent header to avoid Too Many Requests error
    headers = {'User-Agent': 'Chrome/120.0.0.0'}
    try:
        resp = get(endpoint, headers=headers, allow_redirects=False)

        if not (200 <= resp.status_code <= 299):
            # status is not success
            return None

        data = resp.json()
        if 'data' in data and 'children' in data.get('data'):
            children = data.get('data').get('children')
            after = data.get('data').get('after')
            hot_list = [post.get('data').get('title') for post in children]
            for w in [w.lower() for w in word_list]:
                for h in hot_list:
                    m = findall(r'\b{}(?![\w+]|[\.!])\b'.format(w), h.lower())
                    if m:
                        count[w] = count.get(w) + len(m)\
                                if count.get(w) else len(m)
                        # print(count)

            if after:
                hot_list = count_words(subreddit, word_list,
                                       count=count, after=after)

            if (after is None):
                for k, v in sorted(count.items(), key=lambda x: x[1],
                                   reverse=True):
                    print('{}: {}'.format(k, v))
    except Exception:
        return None
