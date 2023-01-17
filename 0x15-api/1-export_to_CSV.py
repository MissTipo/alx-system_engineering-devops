#!/usr/bin/python3
from requests import get
from sys import argv
import csv


user = get('https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])).json()
todos = get(f'https://jsonplaceholder.typicode.com/todos', params = {"userId" : argv[1]}).json()
with open(f'{argv[1]}.csv', 'w', encoding='utf8') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for todo in todos:
        writer.writerow([f"{argv[1]}", f'{user["name"]}' f'{str(todo["completed"])}', f'{todo["title"]}'])
