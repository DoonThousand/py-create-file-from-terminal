import os
import sys
import datetime


def create_file_from_terminal(file_name: str) -> None:
    file_exists_and_not_empty = os.path.exists(file_name) and os.path.getsize(file_name) > 0

    with open(file_name, "a", encoding="utf-8") as f:
        if file_exists_and_not_empty:
            f.write("\n")

        f.write(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "\n")

        number_of_line = 1

        while True:
            string_input = input("Enter content line: ")

            if string_input == "stop":
                break

            f.write(f"{number_of_line} {string_input}\n")
            number_of_line += 1


def file_path_from_terminal() -> None:
    terminal_content = sys.argv
    dir_path = None

    if "-d" in terminal_content:
        d_index = terminal_content.index("-d")

        if "-f" in terminal_content:
            f_index = terminal_content.index("-f")
            dir_path = terminal_content[d_index + 1:f_index]
        else:
            dir_path = terminal_content[d_index + 1:]

        dir_path = os.path.join(*dir_path)
        os.makedirs(dir_path, exist_ok=True)

    if "-f" in terminal_content:
        file_name = terminal_content[terminal_content.index("-f") + 1]

        if "-d" in terminal_content and dir_path:
            file_name = os.path.join(dir_path, file_name)

        create_file_from_terminal(file_name)


if __name__ == "__main__":
    file_path_from_terminal()
