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
    str_userId = str(userId)
    user = response.json()[(name - 1)]["username"]
    for task in todo_list.json():
            the_task = []
            if task['userId'] == userId:
                done = task['complete']
                u_task = task['title']
                the_task.append({"task": u_task, 'completed': done, 'username': user})
    with open(f"{userId}.json", "w") as file:
        data = {str_userId: the_task}
        json_data = json.dumps(data)
        file.write(json_data)
    (task_title(name))
