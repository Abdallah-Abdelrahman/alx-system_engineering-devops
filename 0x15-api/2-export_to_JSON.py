#!/usr/bin/python3
'''script returns information for a given employee ID
about his/her TODO list progress

Attrs:
    URL: endpoint to retrive the iformation from
'''
from requests.exceptions import HTTPError
from json import dumps
from requests import get
import sys

URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    EMPLOYEE_ID = sys.argv[1]
    try:
        user = get(f'{URL}/users/{EMPLOYEE_ID}').json()
        todos = get(f'{URL}/todos?userId={EMPLOYEE_ID}').json()
        data = {user.get('id'):
                [
                {'task': t.get('title'), 'completed': t.get('completed'),
                 'username': user.get('username')} for t in todos
                ]
                }

        with open(f'{user.get("id")}.json', 'w') as f:
            f.write(dumps(data))

    except HTTPError as http_err:
        print(http_err)
    except Exception as e:
        print(e)
