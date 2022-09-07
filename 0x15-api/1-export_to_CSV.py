#!/usr/bin/python3
"""extend your Python script to export data in the CSV format"""
import csv
import requests
from sys import argv


if __name__ == '__main__':

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(
            argv[1])
    data = requests.get(url)
    data = data.json()
    name = data.get('username')
    url1 = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(
            argv[1])
    posts = requests.get(url1)
    posts = posts.json()

    with open("{}".format(argv[1]) + ".csv", "w") as f:
        writer = csv.writer(f, dialect='unix')
        for _dic in posts:
            writer.writerow(
                    [argv[1],
                        name,
                        _dic.get('completed'),
                        _dic.get('title')])
