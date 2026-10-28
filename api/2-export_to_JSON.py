#!/usr/bin/python3
"""Export all tasks owned by an employee to a JSON file, using a REST API."""
import json
import requests
import sys


def export_to_json(user_id):
    """Fetch the tasks of user_id and write them to USER_ID.json."""
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": user_id}
    ).json()

    username = user.get("username")

    tasks = []
    for task in todos:
        tasks.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        })

    with open("{}.json".format(user_id), "w") as json_file:
        json.dump({str(user_id): tasks}, json_file)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        export_to_json(int(sys.argv[1]))
