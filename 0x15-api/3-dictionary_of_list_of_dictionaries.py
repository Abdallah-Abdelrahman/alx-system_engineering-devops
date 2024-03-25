#!/usr/bin/python3
'''script returns information for a given employee ID
about his/her TODO list progress

Attrs:
    URL: endpoint to retrive the iformation from
'''
from requests.exceptions import HTTPError
from json import dumps
from requests import get

URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    try:
        users = get(f'{URL}/users').json()
        todos = get(f'{URL}/todos').json()
        data = {}

        for u in users:
            data.update({u.get('id'): []})
            for t in todos:
                if u.get('id') == t.get('userId'):
                    data[u.get('id')].append(
                            {'username': u.get('username'),
                             'task': t.get('title'),
                             'completed': t.get('completed')
                             }
                            )

        with open('todo_all_employees.json', 'w') as f:
            f.write(dumps(data))

    except HTTPError as http_err:
        print(http_err)
    except Exception as e:
        print(e)
