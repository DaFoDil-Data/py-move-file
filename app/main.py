import os
import shutil


def move_file(command: str) -> None:
    parts = command.split()
    if len(parts) != 3 or parts[0] != "mv":
        return
    _, source_name, destination_name = parts
    if not os.path.isfile(source_name):
        return
    if destination_name.endswith(("/", "\\")):
        destination_name = os.path.join(
            destination_name, os.path.basename(source_name)
        )
    if os.path.abspath(source_name) == os.path.abspath(destination_name):
        return
    if (os.path.exists(destination_name)
            and os.path.samefile(source_name, destination_name)):
        return
    destination_directory = os.path.dirname(destination_name)
    if destination_directory:
        os.makedirs(destination_directory, exist_ok=True)
    shutil.copyfile(source_name, destination_name)
    os.remove(source_name)
