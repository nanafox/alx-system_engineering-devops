#!/usr/bin/python3

"""This script returns a list containing the titles of all hot articles for a
given subreddit. If the subreddit is invalid, the function returns None. It
uses a recursive approach."""

import requests


def recurse(subreddit, hot_list=[], depth=0, max_depth=50, count=0):
    """
    Retrieves a list of titles of all hot articles for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot articles.
        depth (int): The current depth of the recursion.
        max_depth (int): The maximum depth of the recursion.
        count (int): The count of posts retrieved so far.

    Returns:
        list: A list containing the titles of all hot articles for a given
        subreddit. If the subreddit is invalid, the function returns None.
    """
    # Send a GET request to the Reddit API to retrieve the hot posts
    response = requests.get(
        "https://www.reddit.com/r/{}/hot.json".format(subreddit),
        headers={"User-Agent": "nabuntu_bot-01"},
        allow_redirects=False,
        params={"count": count, "after": "", "limit": 100},
        timeout=30,
    )

    # Check if the request was successful
    if response.status_code != 200:
        return None

    print("Working on count: ", count)
    print("Working on depth: ", depth)
    print("Current list length: ", len(hot_list))
    # Get the data from the response
    data = response.json().get("data")

    # Get the list of posts from the data
    posts = data.get("children")

    # Get the after value from the data
    after = data.get("after")

    count += data.get("dist")

    # Add the titles of the posts to the hot_list
    for post in posts:
        hot_list.append(post.get("data").get("title"))

    # Check if the recursion has reached the maximum depth
    if depth == max_depth:
        return hot_list

    # Check if there are more posts to retrieve
    if after is not None:
        return recurse(subreddit, hot_list, depth + 1, max_depth, count)

    return hot_list
