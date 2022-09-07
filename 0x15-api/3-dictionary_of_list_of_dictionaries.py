#!/usr/bin/python3
"""extend your Python script to export data in the CSV format"""
import csv
import json
import requests
from sys import argv


if __name__ == '__main__':

    response_users_all = requests.get(
            'https://jsonplaceholder.typicode.com/users')

    users_all = response_users_all.json()
    ids = []
    for user in users_all:
        ids.append(user.get('id'))

    from_json = {}
    for user_id in ids:

        response_user = requests.get(
                'https://jsonplaceholder.typicode.com/users/{}'.format(
                    user_id))
        user = response_user.json()
        name = user.get('username')
        response_posts = requests.get(
                'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                    user_id))
        posts = response_posts.json()

        new_list = []
        for dict_post in posts:
            new_dict = {}
            new_dict['task'] = dict_post.get('title')
            new_dict['completed'] = dict_post.get('completed')
            new_dict['username'] = name
            new_list.append(new_dict)
        from_json['{}'.format(user_id)] = new_list

    with open("todo_all_employees.json", "w") as file:
        json.dump(from_json, file)
