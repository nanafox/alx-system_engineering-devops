#!/usr/bin/python3

"""Defines useful functions for lazy developers (me)."""

import csv
import requests
import json

USERS_URL = "https://jsonplaceholder.typicode.com/users/"
TODOS_URL = "https://jsonplaceholder.typicode.com/todos/"


def get_todos(user_id=None) -> "list[dict]":
    """
    Retrieves a list of todos for a given user if the user ID is provided.
    Else, it retrieves all todos.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list[dict]: A list of dictionaries representing the todos for the
        user or all users.
    """
    if user_id is None:
        return requests.get(TODOS_URL).json()

    return requests.get(f"{USERS_URL}/{user_id}/todos").json()


def get_completed_tasks(tasks: "list[dict]") -> "list[dict]":
    """Returns all the TODO tasks that the user has completed.

    Args:
        tasks (list[dict]): The list of dictionaries containing all of the
        TODOs

    Returns:
        list[dict]: A list of dictionaries of all completed TODOs.
    """
    return [task for task in tasks if task.get("completed") is True]


def print_completed_tasks(
    user: str, num_of_tasks: int, completed_tasks: "list[dict]"
) -> None:
    """
    Prints the completed tasks for a given user.

    Args:
        user (str): The name of the user.
        num_of_tasks (int): The total number of tasks.
        completed_tasks (list[dict]): A list of dictionaries
        representing completed tasks.
    """
    print(
        f"Employee {user} is done with "
        f"tasks({len(completed_tasks)}/{num_of_tasks}):"
    )

    for task in completed_tasks:
        print(f"\t {task.get('title')}")


def get_name(user_id: int) -> "str | None":
    """
    Retrieves the name associated with the given user ID from an API.

    Args:
        user_id (int): The ID of the user.

    Returns:
        str | None: The name associated with the user ID, or
        None if the username is not found.
    """

    return requests.get(f"{USERS_URL}/{user_id}").json().get("name", None)


def get_username(user_id):
    """
    Retrieves the name associated with the given user ID from an API.

    Args:
        user_id (int): The ID of the user.

    Returns:
        str | None: The name associated with the user ID, or
        None if the username is not found.
    """
    return requests.get(f"{USERS_URL}/{user_id}").json().get("username", None)


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
        data[user_id].append(
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username,
            }
        )

    with open(f"{user_id}.json", "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)


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


def get_users() -> "list[dict]":
    """
    Retrieves a list of all users from an API.

    Returns:
        list[dict]: A list of dictionaries representing all users.
    """
    return requests.get(USERS_URL).json()
