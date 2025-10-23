
# pro_linux09 - Ethical OSINT Tool CLI for Instagram & Snapchat

from modules.instagram_osint import instagram_lookup
from modules.snapchat_osint import snapchat_lookup
from rich.console import Console

console = Console()

def menu():
    console.print("ProLinux09 Ethical OSINT Tool", style="bold green")
    console.print("1. Instagram Lookup")
    console.print("2. Snapchat Lookup")
    console.print("3. Exit")

    choice = input("Select option (1/2/3): ").strip()

    if choice == "3":
        console.print("Exiting... Goodbye!", style="yellow")
        return

    username = input("Enter username: ").strip()
    if choice == "1":
        result = instagram_lookup(username)
    elif choice == "2":
        result = snapchat_lookup(username)
    else:
        result = {"error": "Invalid choice"}

    console.print(result, style="cyan")
    print("
")
    menu()

if __name__ == "__main__":
    menu()
