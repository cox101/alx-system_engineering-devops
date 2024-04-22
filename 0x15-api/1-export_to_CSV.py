#!/usr/bin/python3
"""
Fetches information from JSONPlaceholder API and exports to CSV
"""

import requests
import csv
import sys

def fetch_user_todo_list(user_id):
    main_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{main_url}/user/{user_id}/todos"
    name_url = f"{main_url}/users/{user_id}"

    try:
        todo_result = requests.get(todo_url).json()
        name_result = requests.get(name_url).json()
        return name_result, todo_result

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def export_to_csv(user_id, username, todo_list):
    filename = f"{user_id}.csv"
    with open(filename, 'w', newline='') as csvfile:
        fieldnames = ["user_ID", "username", "completed", "task"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for todo in todo_list:
            writer.writerow({"user_ID": user_id, "username": username, "completed": todo.get("completed"), "task": todo.get("title")})
    print(f"CSV file '{filename}' has been created successfully.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py user_id")
        sys.exit(1)

    user_id = sys.argv[1]

    user_info, todo_list = fetch_user_todo_list(user_id)
    username = user_info.get("username")

    export_to_csv(user_id, username, todo_list)

