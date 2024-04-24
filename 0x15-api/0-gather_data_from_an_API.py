#!/usr/bin/python3

"""
This script takes an employee ID and returns the information about his/her
TODO list progress. Specifically, the ones they have completed.
"""

import lazy_methods
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write(f"Usage: {sys.argv[0]} <user_id>\n")
        sys.exit(1)

    user = lazy_methods.get_name(sys.argv[1])
    if user is None:
        sys.stderr.write("Invalid user id.\n")
        sys.exit(1)

    todos = lazy_methods.get_todos(sys.argv[1])
    completed_tasks = lazy_methods.get_completed_tasks(todos)
    lazy_methods.print_completed_tasks(user, len(todos), completed_tasks)
