#!/usr/bin/python3

"""
This script takes an employee ID and returns the information about his/her
TODO list progress. Specifically, the ones they have completed.
"""

import requests
import sys

URL = "https://jsonplaceholder.typicode.com/users/"


def get_todos(user_id: int) -> "list[dict]":
    """
    Retrieves a list of todos for a given user.

    Args:
        user_id (int): The ID of the user.

    Returns:
        list[dict]: A list of dictionaries representing the todos for the user.
    """
    return requests.get(f"{URL}/{user_id}/todos").json()


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
    return requests.get(f"{URL}/{user_id}").json().get("name", None)


def get_username(user_id):
    """
    Retrieves the name associated with the given user ID from an API.

    Args:
        user_id (int): The ID of the user.

    Returns:
        str | None: The name associated with the user ID, or
        None if the username is not found.
    """
    return requests.get(f"{URL}/{user_id}").json().get("username", None)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <user_id>\n")
        sys.exit(1)

    user = get_name(sys.argv[1])
    if user is None:
        sys.stderr.write("Invalid user id.\n")
        sys.exit(1)

    todos = get_todos(sys.argv[1])
    completed_tasks = get_completed_tasks(todos)
    print_completed_tasks(user, len(todos), completed_tasks)
