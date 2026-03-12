import os, subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        abs_file_path = os.path.normpath(os.path.join(working_dir_abs, file_path))
        if os.path.commonpath([abs_file_path, working_dir_abs]) != working_dir_abs:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_file_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        
        if not os.path.splitext(abs_file_path)[1] == ".py":
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", abs_file_path]
        
        if args:
            command.extend(args)
        completed_process = subprocess.run(command, capture_output=True, text=True, timeout=30, cwd=working_dir_abs)
        
        output = []
        if not completed_process.returncode == 0:
            output.append("Process exited with code " + str(completed_process.returncode))
        if not completed_process.stdout and not completed_process.stderr:
           output.append("No output produced")
        if completed_process.stdout:
            output.append("STDOUT: " + completed_process.stdout)
        if completed_process.stderr:
            output.append("STDERR: " + completed_process.stderr)
        
        return "\n".join(output)

    except Exception as e:
        return f"Error: executing Python file: {e}"