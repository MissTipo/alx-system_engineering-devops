#!/usr/bin/python3
"""Exports data in the JSON format"""
import json
from requests import get
from sys import argv


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = get(url + "users/{}".format(argv[1])).json()
    user_name = user.get("user_name")
    todos = get(url + "todos", params={"userId": argv[1]}).json()
    with open("{}.json".format(argv[1]), "w", encoding="UTF8") as f:
        json.dump({argv[1]: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "user_name": user_name
        } for t in todos]}, f)
