import os
from google.genai import types


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
        return f'Error: writing to file: {e}'


schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description=f"Writes content to a file specified by the file path.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file that will be written to, relative to the working directory",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content that will be written to the file"
            )
        },
        required=["file_path", "content"]
    ),
)