#!/usr/bin/python3
"""Module"""

import json
import requests
import sys
import csv

"""Module"""

if __name__ == "__main__":
    """IF SCRIPT IS NOT RUN AS MODULE"""
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')
    # name = int(sys.argv[1])

    def task_title(name):
        """
        Retrieves and displays compeleted tasks
        Args:
            name (int): The employee's index in the user list.

        Returns:
            None
        """
        userId = name
        user = response.json()[(name - 1)]["username"]
        with open('{}.csv'.format(userId), mode='w') as file:
            for task in todo_list.json():
                    if task['userId'] == userId:
                        done = task['completed']
                        # print(userId, user, done, task['title'])
                        file_editor = csv.writer(file, quoting=csv.QUOTE_ALL)
                        file_editor.writerow([userId, user, done, task['title']])
    (task_title(2))
