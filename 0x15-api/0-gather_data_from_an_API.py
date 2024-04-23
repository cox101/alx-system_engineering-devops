#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""
import sys
import requests

def get_todo_list_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(f'{base_url}/{employee_id}/todos')
    if response.status_code != 200:
        print(f"Failed to fetch data for employee ID {employee_id}")
        return

    todos = response.json()
    completed_tasks = [todo for todo in todos if todo['completed']]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)
    employee_name = requests.get(f'{base_url}/{employee_id}').json()['name']

    print(f"Employee {employee_name} is done with tasks({completed_count}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_todo_list_progress(employee_id)

