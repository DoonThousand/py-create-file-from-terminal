import sys
import os
from datetime import datetime


def create_file(file_path: str) -> None:
    os.makedirs(os.path.dirname(file_path) or ".", exist_ok=True)

    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists and os.path.getsize(file_path) > 0:
            file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        line_no = 1

        while True:
            try:
                user_input = input("Enter content line: ")
            except (EOFError, IndexError):
                break

            if user_input.strip().lower() == "stop":
                break

            file.write(f"{line_no} {user_input}\n")
            line_no += 1


def find_path_from_terminal() -> None:
    args = sys.argv[1:]

    dirs = []
    filename = None
    create_file_flag = False

    i = 0
    while i < len(args):
        arg = args[i]

        if arg == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
            continue

        if arg == "-f":
            if i + 1 < len(args) and not args[i + 1].startswith("-"):
                filename = args[i + 1]
                create_file_flag = True
                i += 2
                continue
            i += 1
            continue

        i += 1

    dir_path = os.path.join(*dirs) if dirs else ""

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    if create_file_flag:
        file_path = os.path.join(dir_path, filename) if dir_path else filename
        create_file(file_path)


if __name__ == "__main__":
    find_path_from_terminal()
