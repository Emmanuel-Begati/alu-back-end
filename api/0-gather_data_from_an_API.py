#!/usr/bin/python3
"""Module"""

import requests
import json
import sys

"""Module"""

if __name__ == "__main__":
    """IF SCRIPT IS NOT RUN AS MODULE"""
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')
    name = sys.argv[0]
    def task_title(name):
        """
        Retrieves and displays the completed tasks of a specific employee from a mock API.
        Args:
            name (int): The employee's index in the user list.

        Returns:
            None
        """
        userId = name + 1
        counter = []
        for i in todo_list.json():
            if i['userId'] == userId:
                if i['completed'] == True:
                    counter.append('True')
                
        employee_name = response.json()[name]['name']
        number_of_done_tasks = len(counter)
        print (employee_name, 'has completed',number_of_done_tasks , '/20 tasks')
        for task in todo_list.json():
            if task['completed'] == True:
                if task['userId'] == userId:
                    print (task['title'])
        

    
    (task_title(name))

    

