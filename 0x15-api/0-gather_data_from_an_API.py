#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

import requests
import sys

def fetch_todo_progress(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"
    employee_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        # Fetch employee data
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()

        # Fetch todos data
        todos_response = requests.get(todos_url)
        todos_data = todos_response.json()

        # Extract employee name
        employee_name = employee_data['name']

        # Calculate progress
        total_tasks = len(todos_data)
        done_tasks = sum(1 for todo in todos_data if todo['completed'])

        # Display progress
        print(f"Employee {employee_name} is done with tasks({done_tasks}/{total_tasks}):")
        for todo in todos_data:
            if todo['completed']:
                print(f"\t{todo['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_todo_progress(employee_id)

