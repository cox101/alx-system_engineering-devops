#!/usr/bin/python3
"""
Exports to-do list information for a given employee ID to a JSON file.
Usage: python3 export_todo.py <employee_id>
"""

from json import dump
from requests import get
from sys import argv

def export_todo_list(employee_id):
    base_url = "https://jsonplaceholder.typicode.com"

    try:
        user_response = requests.get(f"{base_url}/users/{employee_id}")
        user_response.raise_for_status()
        user_data = user_response.json()
        username = user_data["username"]

        todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
        todos_response.raise_for_status()
        todos_data = todos_response.json()

        todo_list = []
        for todo in todos_data:
            todo_item = {
                "username": username,
                "task": todo["title"],
                "completed": todo["completed"]
            }
            todo_list.append(todo_item)

            output_file = "todo_all_employees.json"

        with open(output_file, "w") as json_file:
            json.dump({employee_id: todo_list}, json_file, indent=4)

        print(f"Todo list for employee ID {employee_id} has been exported to {output_file}")

    except requests.exceptions.RequestException as e:
        print(f"Error occurred while fetching data: {e}")
        sys.exit(1)
    except (KeyError, TypeError) as e:
        print(f"Error processing data: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_todo.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    export_todo_list(employee_id)

