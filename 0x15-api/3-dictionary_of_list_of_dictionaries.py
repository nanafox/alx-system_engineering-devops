#!/usr/bin/python3

"""
This module provides a function to export all tasks to a JSON file.
"""

import json
import requests

lazy_methods = __import__("0-gather_data_from_an_API")


def export_all_to_json(users: "list[dict]", tasks: "list[dict]") -> None:
    """
    Export user tasks to a JSON file.

    Args:
        tasks (list[dict]): A list of dictionaries representing the tasks.
    """
    tasks_by_user = {}
    # I am inserting a dummy element here so it's easier to reference user ids
    # later on in the code
    users.insert(0, {})

    for task in tasks:
        user_id = str(task.get("userId"))

        if user_id not in tasks_by_user:
            username = users[int(user_id)].get("username")
            tasks_by_user[user_id] = []

        tasks_by_user[user_id].append(
            {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed"),
            }
        )

    with open("todo_all_employees.json", "w", encoding="utf-8") as json_file:
        json.dump(tasks_by_user, json_file, indent=4)


if __name__ == "__main__":
    # get user info and todos once so we can minimize the number of requests.
    # this helps to achieve more speed since everything will be done locally
    # after the data has been retrieved.
    users = requests.get(lazy_methods.URL).json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    export_all_to_json(users=users, tasks=todos)
