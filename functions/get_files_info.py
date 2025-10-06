import os

def get_files_info(working_directory, directory="."):
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    working_dir_path = os.path.abspath(working_directory)

    if not target_dir.startswith(working_dir_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        entries = sorted(os.listdir(target_dir))
        mapped = "\n".join(generate_line(name, target_dir) for name in entries)
        return mapped

    except Exception as e:
        return f'Error: {e}'

def generate_line(name, full_path):
    full_path_of_file = os.path.join(full_path, name)
    size = os.path.getsize(full_path_of_file)
    is_dir = os.path.isdir(full_path_of_file)

    return f"- {name}: file_size={size} bytes, is_dir={is_dir}"
    