import sys
import os
from datetime import datetime


def create_file(file_path: str) -> None:
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists and os.path.getsize(file_path) > 0:
            file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_no = 1

        while True:
            user_input = input("Enter content line: ")

            if user_input.strip().lower() == "stop":
                break

            file.write(f"{line_no} {user_input}\n")
            line_no += 1


def find_path_from_terminal() -> None:
    args = sys.argv[1:]

    dirs = []
    filename = "file.txt"

    i = 0
    while i < len(args):
        arg = args[i]

        if arg == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
            continue

        elif arg == "-f":
            i += 1
            if i < len(args) and not args[i].startswith("-"):
                filename = args[i]
                i += 1
            continue

        else:
            i += 1

    # Build directory path safely
    dir_path = os.path.join(*dirs) if dirs else ""

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, filename) if dir_path else filename

    # Always reach execution step
    create_file(file_path)


if __name__ == "__main__":
    find_path_from_terminal()
