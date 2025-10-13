# AI Agent - Build Your Own Claude Code

A toy implementation of an agentic AI coding assistant using Google's Gemini API. Learn how tools like Cursor and Claude Code work by building one from scratch.

**Example:**
```sh
uv run main.py "fix my calculator app"
# - Calling function: get_files_info
# - Calling function: get_file_content
# - Calling function: write_file
# Final response: Calculator app fixed and working correctly.
```

## Prerequisites

- Python 3.10+
- [uv](https://github.com/astral-sh/uv) package manager
- Google AI Studio API key

## Quick Start

```bash
# Create project
uv init your-project-name
cd your-project-name
uv venv
source .venv/bin/activate

# Install dependencies
uv add google-genai==1.12.1
uv add python-dotenv==1.1.0

# Set up API key
echo 'GEMINI_API_KEY="your_key_here"' > .env

# Run agent
uv run main.py "your task here" --verbose
```

## How It Works

The agent operates in a feedback loop:

1. Receives a coding task
2. LLM chooses which function to call
3. Function executes and returns results
4. Results feed back to LLM
5. Steps 2-4 repeat until complete (max 20 iterations)

### Available Functions

All functions are scoped to `working_directory` for security:

- **get_files_info**: List directory contents with metadata
- **get_file_content**: Read files (truncated at 10k chars)
- **write_file**: Create or overwrite files
- **run_python_file**: Execute Python scripts (30s timeout)

## Usage Examples

```bash
# List files
uv run main.py "what files are in the root?"

# Read a file
uv run main.py "read the contents of main.py"

# Fix a bug
uv run main.py "fix the bug: 3 + 7 * 2 shouldn't be 20"

# Verbose mode (shows function calls and tokens)
uv run main.py "run tests.py" --verbose
```

## Project Structure

```
project_root/
├── calculator/         # Test project
│   ├── main.py
│   ├── tests.py
│   ├── lorem.txt
│   └── pkg/
│       ├── calculator.py
│       └── render.py
├── functions/          # Agent tools
│   ├── call_function.py
│   ├── get_files_info.py
│   ├── get_file_content.py
│   ├── write_file.py
│   └── run_python_file.py
├── main.py
├── config.py
├── prompts.py
├── tests.py
├── .env               # API key (don't commit!)
├── pyproject.toml
└── README.md
```

## Testing

```bash
# Manual testing
uv run tests.py

# Run calculator tests
uv run calculator/tests.py
```

## Security Notes

- All functions validate paths stay within `working_directory`
- Python execution limited to 30 seconds
- File reads truncated at 10,000 characters
- **For learning only** - not production-ready

## Tips

- Use `--verbose` for debugging
- Adjust system prompt if LLM misbehaves
- Monitor token usage (free tier has limits)
- Always activate virtual environment first
