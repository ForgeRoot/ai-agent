import os

def write_file(working_directory, file_path, content):
    target_file = os.path.abspath(os.path.join(working_directory,file_path))
    working_dir_path = os.path.abspath(working_directory)
    if not target_file.startswith(working_dir_path):
        return f'Error: Cannot read \"{file_path}\" as it is outside the permitted working directory'
    try:
        with open(target_file, "w") as f:
            f.write(content)
        return(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    except Exception as e:
        return f'Error: {e}'
    