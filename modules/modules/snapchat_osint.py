# pro_linux09 - Snapchat Public Data Lookup

import requests
from utils.logger import log_action
from utils.validator import valid_username

def snapchat_lookup(username: str):
    log_action("Snapchat Lookup", username)
    if not valid_username(username):
        return {"error": "Invalid username format"}

    base_url = f"https://www.snapchat.com/add/{username}"
    response = requests.get(base_url)
    if response.status_code == 200:
        return {
            "username": username,
            "profile_url": base_url,
            "status": "Public link reachable"
        }
    else:
        return {"username": username, "status": "Profile link not reachable"}
