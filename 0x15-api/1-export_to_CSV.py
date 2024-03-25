#!/usr/bin/python3
'''script returns information for a given employee ID
about his/her TODO list progress

Attrs:
    URL: endpoint to retrive the iformation from
'''
from requests.exceptions import HTTPError
from sys import argv
from csv import writer, QUOTE_ALL
from requests import get

URL = 'https://jsonplaceholder.typicode.com'

if __name__ == '__main__':
    EMPLOYEE_ID = argv[1]
    try:
        completed = 0
        user = get(f'{URL}/users/{EMPLOYEE_ID}').json()
        todos = get(f'{URL}/todos?userId={EMPLOYEE_ID}').json()
        data = []
        for t in todos:
            data.append([user.get('id'), t.get('completed'), t.get('title')])

        with open(f'{user.get("id")}.csv', 'w') as f:
            w = writer(f, quoting=QUOTE_ALL).writerows(data)

    except HTTPError as http_err:
        print(http_err)
    except Exception as e:
        print(e)
