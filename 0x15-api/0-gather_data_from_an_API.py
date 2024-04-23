#!/usr/bin/python3
"""
Script to fetch employee TODO list progress from a REST API.
"""

import requests
import sys

def fetch_employee_todo_progress(employee_id):
    """
    Fetches employee TODO list progress from the given API.
    """
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    response = requests.get(url)
    todos = response.json()

    if not todos:
        print("No data found for employee ID:", employee_id)
        return

    completed_tasks = [todo for todo in todos if todo['completed']]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)
    employee_name = todos[0]['username']

    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_count, total_tasks))
    for task in completed_tasks:
        print("\t", task['title'])

if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_todo_progress(employee_id)

