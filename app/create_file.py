import sys
import os
from datetime import datetime


def create_file(file_path: str) -> None:
    file_exists = os.path.exists(file_path)

    with open(file_path, "a", encoding="utf-8") as file:
        if file_exists and os.path.getsize(file_path) > 0:
            file.write("\n")

        file.write(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        number_of_line = 1

        while True:
            input_line = input("Enter content line: ")

            if input_line.lower() == "stop":
                break

            file.write(f"{number_of_line} {input_line}\n")
            number_of_line += 1


def find_path_from_terminal() -> None:
    args = sys.argv[1:]
    dirs = []
    filename = "file.txt"

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                dirs.append(args[i])
                i += 1
            continue

        if args[i] == "-f":
            if i + 1 < len(args):
                filename = args[i + 1]
            i += 2
            continue

        i += 1

    dir_path = os.path.join(*dirs) if dirs else ""

    if dir_path:
        os.makedirs(dir_path, exist_ok=True)

    file_path = os.path.join(dir_path, filename) if dir_path else filename

    create_file(file_path)


if __name__ == "__main__":
    find_path_from_terminal()
