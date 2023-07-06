#!/usr/bin/python3
import requests
import json

response = requests.get('https://jsonplaceholder.typicode.com/users')
todo_list = requests.get('https://jsonplaceholder.typicode.com/todos')

def task_title(name):
    userId = name + 1
    counter = []
    for i in todo_list.json():
        if i['userId'] == userId:
            if i['completed'] == True:
                counter.append('True')
            
    employee_name = response.json()[name]['name']
    number_of_done_tasks = len(counter)
    print (employee_name, 'has completed',number_of_done_tasks , '/20 tasks')
    for task in 


name = 0
while name < 10:
    print (task_title(name))
    name += 1
    