#!/usr/bin/python3
"""Export an employee's TODO list data to a CSV file using a REST API."""
import csv
import json
import sys
import urllib.request


def get_json(url):
    """Download a URL and return its JSON content as Python data."""
    with urllib.request.urlopen(url) as response:
        return json.loads(response.read().decode("utf-8"))


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = get_json("{}/users/{}".format(base_url, employee_id))
    todos = get_json("{}/todos?userId={}".format(base_url, employee_id))

    username = user.get("username")

    with open("{}.csv".format(employee_id), "w", newline="") as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL,
                            lineterminator="\n")
        for task in todos:
            writer.writerow([employee_id, username,
                             str(task.get("completed")), task.get("title")])
