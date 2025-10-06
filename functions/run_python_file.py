import os
import sys
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    target_file = os.path.abspath(os.path.join(working_directory, file_path))
    working_dir_path = os.path.abspath(working_directory)

    if not target_file.startswith(working_dir_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    if not os.path.exists(target_file):
        return f'Error: File "{file_path}" not found.'

    if not target_file.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    try:
        result = subprocess.run([sys.executable, target_file] + args, cwd=working_directory, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)

        return_list = []
        if result.stdout:
            return_list.append(f"STDOUT: {result.stdout.decode("utf-8")}")
        if result.stderr:
            return_list.append(f"STDERR: {result.stderr.decode("utf-8")}")
        if result.returncode != 0:
            return_list.append(f"Process exited with code {result.returncode}")
        if not return_list:
            return "No output produced."
        else:
            return "\n".join(return_list)
    except Exception as e:
        return f"Error: executing Python file: {e}"
    