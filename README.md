# Agentic AI Software Engineer

An autonomous AI agent built with Python and the Gemini API that can diagnose and repair bugs in a codebase. Unlike a standard chatbot, this agent uses a **tool-use loop** to interact directly with the local filesystem and terminal to verify its own fixes.

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Gemini](https://img.shields.io/badge/Google_Gemini-API-4285F4?logo=googlegemini&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![uv](https://img.shields.io/badge/uv-Package_Manager-FFD43B?logo=python&logoColor=black)](https://docs.astral.sh/uv/)

## ⚠️ Warning

This tool can modify files and execute commands on your local system. Always review the agent's permissions and use it within a version-controlled environment to allow for rollbacks.

## Features

- Analyzes stack traces and source code to identify logic errors
- Uses function calling to read files, write code, and execute shell commands
- Runs test suites after changes and iterates if tests fail
- Includes a calculator tool for validating numeric operations (added March 2026)
- Human-in-the-loop or sandboxed approach for system commands


## How It Works

The agent operates in a loop:

1. **Analyze** – Receives a task or bug report
2. **Execute** – Calls Python functions to inspect directory structure and file contents
3. **Modify** – Generates and applies code patches
4. **Validate** – Executes shell commands (like `pytest` or `python main.py`) to verify the fix


## Tech Stack

- Python 3.x
- Google Gemini API (`google-generativeai`)
- uv for package management
- Pytest for testing

## Project Structure

```text
llm_agent/
├── calculator/
├── functions/
├── main.py
├── call_function.py
├── constants.py
├── prompts.py
├── pyproject.toml
├── uv.lock
└── test_*.py
```

## Installation & Usage

### Prerequisites
- Python 3.8 or later
- uv or pip
- Google Gemini API key

### Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Polynomial-B/llm_agent.git
   cd llm_agent
   ```

2. Install dependencies with uv:
   ```bash
   uv sync
   ```

   Or with pip:
   ```bash
   pip install -r requirements.txt
   ```

3. Set your API key:
   ```bash
   export GEMINI_API_KEY='your_key_here'
   ```

4. Run the agent
   ```bash
   python main.py
   ```
