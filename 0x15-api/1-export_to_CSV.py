#!/usr/bin/python3

"""
This module provides a function to export user tasks to a CSV file.
"""

import csv
import sys

lazy_methods = __import__("0-gather_data_from_an_API")


def export_to_csv(user_id: int, username: str, tasks: "list[dict]") -> None:
    """
    Export user tasks to a CSV file.

    Args:
        user_id (int): The ID of the user.
        username (str): The username of the user.
        tasks (list[dict]): A list of dictionaries representing the tasks.
    """
    with open(f"{user_id}.csv", "w", newline="") as csv_file:
        fieldnames = [
            "USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"
        ]
        writer = csv.DictWriter(
            csv_file, fieldnames=fieldnames, quoting=csv.QUOTE_ALL
        )

        for task in tasks:
            writer.writerow(
                {
                    "USER_ID": f"{user_id}",
                    "USERNAME": f"{username}",
                    "TASK_COMPLETED_STATUS": f"{task.get('completed')}",
                    "TASK_TITLE": f"{task.get('title')}",
                }
            )


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <user_id>\n")
        sys.exit(1)

    user_id = sys.argv[1]
    user = lazy_methods.get_username(user_id)
    if user is None:
        sys.stderr.write("Invalid user id.\n")
        sys.exit(1)

    todos = lazy_methods.get_todos(user_id)
    export_to_csv(user_id=user_id, username=user, tasks=todos)
