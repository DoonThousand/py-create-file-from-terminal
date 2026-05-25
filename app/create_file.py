import os
import sys
from datetime import datetime


def get_content() -> list[str]:
    content_lines = []

    while True:
        line = input("Enter content line: ")

        if line == "stop":
            break

        content_lines.append(line)

    return content_lines


def write_to_file(file_path: str, content_lines: list[str]) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    numbered_lines = []

    for index, line in enumerate(content_lines, start=1):
        numbered_lines.append(f"{index} {line}")

    content = f"{timestamp}\n" + "\n".join(numbered_lines) + "\n"

    with open(file_path, "a", encoding="utf-8") as source_file:
        if source_file.tell() > 0:
            source_file.write("\n")

        source_file.write(content)


def main() -> None:
    cli_args = sys.argv[1:]

    path = ""
    file_name = ""

    if "-d" in cli_args:
        d_index = cli_args.index("-d")

        if "-f" in cli_args:
            f_index = cli_args.index("-f")

            if d_index < f_index:
                dirs = cli_args[d_index + 1 : f_index]
            else:
                dirs = cli_args[d_index + 1 :]
        else:
            dirs = cli_args[d_index + 1 :]

        path = os.path.join(*dirs)

        os.makedirs(path, exist_ok=True)

    if "-f" in cli_args:
        f_index = cli_args.index("-f")
        file_name = cli_args[f_index + 1]

        content_lines = get_content()

        if path:
            file_path = os.path.join(path, file_name)
        else:
            file_path = file_name

        write_to_file(file_path, content_lines)


if __name__ in ("__main__", "<run_path>"):
    main()
