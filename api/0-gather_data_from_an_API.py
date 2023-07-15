#!/usr/bin/python3
"""Module"""

import json
import requests
import sys

"""Module"""

if __name__ == "__main__":
    """IF SCRIPT IS NOT RUN AS MODULE"""
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')

    name = int(sys.argv[1])

    def task_title(name):
        """
        Retrieves and displays compeleted tasks
        Args:
            name (int): The employee's index in the user list.

        Returns:
            None
        """
        userId = name
        counter = []
        for i in todo_list.json():
            if i['userId'] == userId:
                if i['completed'] == 1:
                    counter.append('True')
        e_name = response.json()[(name - 1)]['name']
        tasks = len(counter)
        print("Employee {} is done with tasks({}/20):".format(e_name, tasks))
        for task in todo_list.json():
            if task['completed'] == 1:
                if task['userId'] == userId:
                    print(task['title'])
    (task_title(name))
