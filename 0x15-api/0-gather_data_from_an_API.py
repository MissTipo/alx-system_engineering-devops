#!/usr/bin/python3
"""
A script that returns information about an employee's ODO list progress
using REST api
"""
from requests import get
from sys import argv


if __name__ == '__main__':
    """ensures code isn't executed when imported"""
    req = get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    u = req.json()
    user_name = u.get('name')
    req = get(f'https://jsonplaceholder.typicode.com/todos',
              params={"userId": argv[1]})
    t = req.json()
    # total number of tasks
    total_tasks = len(t)
    # completed tasks
    completed = 0
    completed_task = []
    for task in t:
        if task['completed']:
            completed += 1
            completed_task.append(task['title'])
    response = f'Employee {user_name} is done with'
    'tasks ({completed}/{total_tasks}):'
    print(response)
    for task in completed_task:
        print(f'\t {task}')
