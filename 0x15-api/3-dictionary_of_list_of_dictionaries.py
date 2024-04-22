#!/usr/bin/python3
"""fetches information from JSONplaceholder API and exports to JSON"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    # Fetch user data
    user_response = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    user_data = user_response.json()
    username = user_data['username']

    # Fetch tasks data
    tasks_response = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")
    tasks_data = tasks_response.json()

    # Construct dictionary of tasks
    tasks_dict = {employee_id: []}
    for task in tasks_data:
        task_dict = {
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        }
        tasks_dict[employee_id].append(task_dict)

    # Write to JSON file
    with open(f"{employee_id}.json", "w") as file:
        json.dump(tasks_dict, file, indent=4)

    print(f"Data exported to {employee_id}.json")
