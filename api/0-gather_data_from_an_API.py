"""Module"""

import json
import requests
import sys

"""Module"""

if __name__ == "__main__":
    """IF SCRIPT IS NOT RUN AS MODULE"""
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')
    

    def task_title(name):
        """
        Retrieves and displays compeleted tasks
        Args:
            name (int): The employee's index in the user list.

        Returns:
            None
        """
        userId = name + 1
        counter = []
        for i in todo_list.json():
            if i['userId'] == userId:
                if i['completed'] == 1:
                    counter.append('True')
        employee_name = response.json()[name]['name']
        num_of_done_tasks = len(counter)
        print(employee_name, 'has completed', num_of_done_tasks, '/20 tasks')
        for task in todo_list.json():
            if task['completed'] == 1:
                if task['userId'] == userId:
                    print(task['title'])
    (task_title(2))
