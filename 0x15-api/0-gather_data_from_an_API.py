#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

import requests
import sys

def get_employee_data(employee_id):
    base_url = "https://jsonplaceholder.typicode.com/"

    try:
        response_user = requests.get(f"{base_url}users/{employee_id}")
        response_user.raise_for_status()
        user = response_user.json()

        params = {"userId": employee_id}
        response_todos = requests.get(f"{base_url}todos", params=params)
        response_todos.raise_for_status()
        todos = response_todos.json()

        return user, todos
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

def print_todo_list(user, todos):
    completed_tasks = [todo["title"] for todo in todos if todo["completed"]]

    print(f"Employee {user['name']} is done with tasks({len(completed_tasks)}/{len(todos)}):")

    for task in completed_tasks:
        print(f"\t{task}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    user, todos = get_employee_data(employee_id)
    print_todo_list(user, todos)

