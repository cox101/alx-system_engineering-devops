#!/usr/bin/python3
"""
Fetches information from JSONPlaceholder API and exports to CSV
"""

import csv
import requests
import sys

def fetch_user_todo_list(user_id):
    main_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{main_url}/users/{user_id}/todos"

    try:
        todo_result = requests.get(todo_url).json()
        return todo_result

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def export_to_csv(user_id, todo_list):
    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for todo in todo_list:
            writer.writerow({"USER_ID": user_id,
                             "USERNAME": todo.get("username"),
                             "TASK_COMPLETED_STATUS": todo.get("completed"),
                             "TASK_TITLE": todo.get("title")})

    print(f"CSV file '{filename}' has been created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py user_id")
        sys.exit(1)

    user_id = sys.argv[1]

    todo_list = fetch_user_todo_list(user_id)

    export_to_csv(user_id, todo_list)

