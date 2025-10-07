import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.run_python_file import schema_run_python_file
from functions.write_file import schema_write_file
from functions.call_function import call_function

def main():
    load_dotenv()

    args = sys.argv[1:]

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "How do I build a calculator app?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    if args[-1] == "--verbose":
        user_prompt = " ".join(args[:-1])
    else:
        user_prompt = " ".join(args)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]
    system_prompt = """
You are a code assistant that can perform these operations:
- List files and directories
- Read file contents  
- Execute Python files (with or without arguments)
- Write or overwrite files

When a user asks you to run a Python file without specifying arguments, call the function with just the file_path and omit the args parameter.
"""
    response = generate_response(client, messages, system_prompt, available_functions)

    if args[-1] == "--verbose":
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print("Response:")
    if getattr(response, "function_calls", None):
        for fc in response.function_calls:
            print(f"Calling function: {fc.name}({fc.args})")
            function_call_result = call_function(fc)
            if not function_call_result.parts[0].function_response.response:
                raise Exception("Response is not valid")
            if args[-1] == "--verbose":
                print(f"-> {function_call_result.parts[0].function_response.response}")
            
    else:
        print(response.text)

def generate_response(client, messages, system_prompt, available_functions):
    return client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt)
    )

if __name__ == "__main__":
    main()
