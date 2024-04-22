#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee's TODO list progress
"""
from requests import get
from sys import argv

def get_employee_todo_progress(employee_id):
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = f"{main_url}/user/{employee_id}/todos"
    name_url = f"{main_url}/users/{employee_id}"

    try:
        todo_result = requests.get(todo_url).json()
        name_result = requests.get(name_url).json()

        todo_num = len(todo_result)
        todo_complete = sum(1 for todo in todo_result if todo.get("completed"))
        name = name_result.get("name")
        return name, todo_complete, todo_num, todo_result

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py employee_id")
        sys.exit(1)

    employee_id = sys.argv[1]

    name, todo_complete, todo_num, todo_result = get_employee_todo_progress(employee_id)

    print(f"Employee {name} is done with tasks({todo_complete}/{todo_num}):")
    for todo in todo_result:
        if todo.get("completed"):
            print(f"\t{todo.get('title')}")

