#!/usr/bin/python3
"""Display an employee's TODO list progress using a REST API."""
import json
import sys
import urllib.request


def get_json(url):
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))
if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = get_json("{}/users/{}".format(base_url, employee_id))
    todos = get_json("{}/todos?userId={}".format(base_url, employee_id))

    employee_name = user.get("name")

    done_tasks = []
    for task in todos:
        if task.get("completed") is True:
            done_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), len(todos)))
    for title in done_tasks:
        print("\t {}".format(title))
