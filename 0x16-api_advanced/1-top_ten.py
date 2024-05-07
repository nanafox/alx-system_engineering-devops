#!/usr/bin/python3

"""This script queries the Reddit API and prints the titles of the first 10 top
posts for a give subreddit."""

import requests


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts from a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        None
    """
    # Send a GET request to the Reddit API to retrieve the top 10 hot posts
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit),
        headers={"User-Agent": "nabuntu_bot-01"},
        allow_redirects=False,
    )

    # Check if the request was successful
    if response.status_code != 200:
        print(None)
        return

    # Print the titles of the top 10 hot posts
    for post in response.json()["data"]["children"]:
        print(post["data"]["title"])
