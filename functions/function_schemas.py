from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in a specified directory relative to the working directory, providing file size and directory status",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="Directory path to list files from, relative to the working directory (default is the working directory itself)",
            ),
        },
    ),
)

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads a file in a specified directory. Includes character limit.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="File to be read.",
            ),
        },
    required=["file_path"]
    ),
)
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes or updates to file in a specified directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to file.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="File to be written or updated.",
            ),
        },
    required=["file_path", "content"]
    ),
)
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs python file in a specified directory. Accepts args with default of None. Outputs STDOUT, STDERR, other error or 'No output produced'",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Python file to be executed.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,items=types.Schema(type=types.Type.STRING),
                description="Python file to be executed.",
            ),
        },
    required=["file_path"]
    ),
)