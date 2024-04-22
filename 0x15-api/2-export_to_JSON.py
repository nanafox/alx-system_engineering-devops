#!/usr/bin/python3

"""
This module provides a function to export user tasks to a JSON file.
"""

import json
import sys

lazy_methods = __import__("0-gather_data_from_an_API")


def export_to_json(user_id: int, username: str, tasks: "list[dict]") -> None:
    """
    Export user tasks to a JSON file.

    Args:
        user_id (int): The ID of the user.
        username (str): The username of the user.
        tasks (list[dict]): A list of dictionaries representing the tasks.
    """
    data = {f"{user_id}": []}

    for task in tasks:
        task_data = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username,
        }

        data[user_id].append(task_data)

    with open(f"{user_id}.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)


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
    export_to_json(user_id=user_id, username=user, tasks=todos)
