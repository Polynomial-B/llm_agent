# Agentic AI Software Engineer

An autonomous AI agent built with Python and the Gemini API that can diagnose and repair bugs in a codebase. Unlike a standard chatbot, this agent uses a **tool-use loop** to interact directly with the local filesystem and terminal to verify its own fixes.


## Warning

This tool has the capability to modify files and execute commands on your local system. Always review the agent's permissions and use it within a version-controlled environment to allow for easy rollbacks.

## Features

- **Autonomous Debugging**: Analyzes stack traces and source code to identify logic errors.
- **Tool-Use Architecture**: Equipped with custom functions to read files, write code, and execute shell commands.
- **Self-Correction**: Runs test suites after applying changes and iterates on the solution if tests fail.
- **Safety First**: Implements a human-in-the-loop or sandboxed approach to executing system commands.

## How It Works

The agent operates in a continuous loop:
1. **Analyze**: The LLM receives a task or a bug report.
2. **Execute**: The agent calls Python functions to inspect the directory structure and file contents.
3. **Modify**: It generates and applies code patches to resolve the identified issues.
4. **Validate**: It executes shell commands (like `pytest` or `python main.py`) to ensure the codebase is functional.

## Tech Stack

- **Language**: Python
- **LLM**: Google Gemini (via `google-generativeai`)
- **Interface**: Function calling and system operations

## Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repo-name.git
   ```
2.  Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
3. Set your API Key:
  ```bash
  export GEMINI_API_KEY='your_key_here'
  ```
4. Run the agent:
  ```bash
  python main.py
  ```
