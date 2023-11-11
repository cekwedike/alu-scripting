#!/usr/bin/python3
"""get hot post function"""


import json
import requests
import sys


def top_ten(subreddit):
    """get top ten hot post"""
    if len(sys.argv) < 2:
        return print(None)
    else:
        url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
        headers = {"User-Agent": "Mozilla/5.0"}
        result = requests.get(url, headers=headers, allow_redirects=False)
        listing = []
        if result.status_code != 200:
            return print(None)
        body = json.loads(result.text)
        for i in body["data"]["children"]:
            print(i["data"]["title"])
