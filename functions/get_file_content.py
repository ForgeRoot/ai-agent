import os
from config import MAX_CHARS
from google.genai import types

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the text content of a single file",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read from, relative to the working directory",
            ),
        },
    ),
)

def get_file_content(working_directory, file_path):
    target_file = os.path.abspath(os.path.join(working_directory,file_path))
    working_dir_path = os.path.abspath(working_directory)
    if not target_file.startswith(working_dir_path):
        return f'Error: Cannot read \"{file_path}\" as it is outside the permitted working directory'
    if not os.path.isfile(target_file):
        return f'Error: File not found or is not a regular file: \"{file_path}\"'
    try:
        with open(target_file, "r") as f:
            content = f.read(MAX_CHARS)
            if os.path.getsize(target_file) > MAX_CHARS:
                content += (
                    f"[...File \"{file_path}\" truncated at {MAX_CHARS} characters]"
                )
        return content
    except Exception as e:
        return f'Error: {e}'
