#!/usr/bin/python3
""" a Python script that, using this REST API """
import json
import requests
from sys import argv


if __name__ == "__main__":
    user = 'https://jsonplaceholder.typicode.com/users/{}'.format(
            argv[1])
    data = requests.get(user)
    data = data.json()
    _id = data.get("id")
    name = data.get("name")

    todo = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            argv[1])
    todos = requests.get(todo)
    todos = todos.json()
    task = len(todos)
    completed = 0
    for _dict in todos:
        if _dict.get('completed') is True:
            completed += 1
    print("Employee {} is done with tasks({}/{}):".format(
        name, completed, task))
    for _dict in todos:
        if _dict.get('completed') is True:
            print("\t", _dict.get('title'))
