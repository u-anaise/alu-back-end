#!/usr/bin/python3
"""Export all tasks owned by an employee to a CSV file, using a REST API."""
import csv
import requests
import sys


def export_to_csv(user_id):
    """Fetch the tasks of user_id and write them to USER_ID.csv."""
    base_url = "https://jsonplaceholder.typicode.com"
    user = requests.get("{}/users/{}".format(base_url, user_id)).json()
    todos = requests.get(
        "{}/todos".format(base_url), params={"userId": user_id}
    ).json()

    username = user.get("username")

    with open("{}.csv".format(user_id), "w", newline="") as csv_file:
        writer = csv.writer(
            csv_file, quoting=csv.QUOTE_ALL, lineterminator="\n"
        )
        for task in todos:
            writer.writerow([
                user_id,
                username,
                task.get("completed"),
                task.get("title"),
            ])


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        export_to_csv(int(sys.argv[1]))
