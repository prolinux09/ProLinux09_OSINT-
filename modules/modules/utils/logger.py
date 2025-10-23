# pro_linux09 - Ethical OSINT Logger

from datetime import datetime

def log_action(action, target):
    """Logs user actions for transparency"""
    with open("activity_log.txt", "a") as log:
        log.write(f"{datetime.now()} | {action} | Target: {target}
")
