#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

import requests
import sys

def get_employee_todo_progress(employee_id):
    api_url = f"https://api.example.com/employees/{employee_id}/todos"

    try:
        response = requests.get(api_url)
        response_data = response.json()

        if "error" in response_data:
            print(f"Error: {response_data['error']}")
            return

        employee_name = response_data.get("employee_name", "Unknown Employee")
        done_tasks = response_data.get("done_tasks", 0)
        total_tasks = response_data.get("total_tasks", 0)

        print(f"Employee {employee_name} is done with tasks ({done_tasks}/{total_tasks}):")
        for task_title in response_data.get("completed_task_titles", []):
            print(f"\t{task_title}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)

