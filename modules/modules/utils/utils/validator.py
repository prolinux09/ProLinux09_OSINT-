# pro_linux09 - Input Validator

def valid_username(username: str) -> bool:
    """Username format validation"""
    return username.replace("_", "").replace(".", "").isalnum() and len(username) >= 3
