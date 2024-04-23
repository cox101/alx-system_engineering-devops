#!/usr/bin/python3
"""
Uses the JSON placeholder API to query data about an employee's tasks.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 employee_tasks.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    main_url = 'https://jsonplaceholder.typicode.com'

    todo_url = f"{main_url}/users/{employee_id}/todos"
    name_url = f"{main_url}/users/{employee_id}"

    try:
        todo_result = requests.get(todo_url).json()
        name_result = requests.get(name_url).json()

        todo_num = len(todo_result)
        todo_complete = sum(1 for todo in todo_result if todo.get("completed"))
        name = name_result.get("name")

        print(f"Employee {name} has completed {todo_complete}/{todo_num} tasks:")
        for todo in todo_result:
            if todo.get("completed"):
                print(f"\t{todo.get('title')}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)
    except (KeyError, TypeError) as e:
        print(f"Error processing data: {e}")
        sys.exit(1)

