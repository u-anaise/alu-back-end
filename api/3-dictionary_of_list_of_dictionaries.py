#!/usr/bin/python3
"""Export the tasks of all employees to a JSON file."""
import json
import requests


def export_all_to_json():
    """Fetch the tasks of every employee and write todo_all_employees.json."""
    base_url = "https://jsonplaceholder.typicode.com"
    users = requests.get("{}/users".format(base_url)).json()
    todos = requests.get("{}/todos".format(base_url)).json()

    all_tasks = {}
    for user in users:
        user_id = user.get("id")
        username = user.get("username")
        all_tasks[str(user_id)] = [
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
            for task in todos
            if task.get("userId") == user_id
        ]

    with open("todo_all_employees.json", "w") as json_file:
        json.dump(all_tasks, json_file)


if __name__ == "__main__":
    export_all_to_json()
