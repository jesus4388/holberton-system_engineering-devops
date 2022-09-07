#!/usr/bin/python3
"""extend your Python script to export data in the CSV format"""
import csv
import json
import requests
from sys import argv


if __name__ == '__main__':

    response_user = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}'.format(
                argv[1]))
    user = response_user.json()
    name = user.get('username')
    response_posts = requests.get(
            'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
                argv[1]))
    posts = response_posts.json()

    new_list = []
    for dict_post in posts:
        new_dict = {}
        new_dict['task'] = dict_post.get('title')
        new_dict['completed'] = dict_post.get('completed')
        new_dict['username'] = name
        new_list.append(new_dict)
    from_json = {}
    from_json['{}'.format(argv[1])] = new_list

    with open("{}".format(argv[1]) + ".json", "w") as file:
        json.dump(from_json, file)
