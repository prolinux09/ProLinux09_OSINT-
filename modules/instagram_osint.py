# pro_linux09 - Instagram Public Data Lookup

import requests
from utils.logger import log_action
from utils.validator import valid_username

def instagram_lookup(username: str):
    log_action("Instagram Lookup", username)
    if not valid_username(username):
        return {"error": "Invalid username format"}

    headers = {"User-Agent": "Mozilla/5.0"}
    url = f"https://www.instagram.com/{username}/?__a=1&__d=dis"

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return {"error": "Unable to access data (account may be private or removed)"}

    try:
        profile = response.json().get("graphql", {}).get("user", {})
        return {
            "name": profile.get("full_name"),
            "bio": profile.get("biography"),
            "followers": profile.get("edge_followed_by", {}).get("count"),
            "following": profile.get("edge_follow", {}).get("count"),
            "is_verified": profile.get("is_verified")
        }
    except Exception:
        return {"error": "Unexpected response format"}
