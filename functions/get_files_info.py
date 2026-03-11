import os


def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        
        if os.path.commonpath([target_dir, working_dir_abs]) != working_dir_abs:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        
        if not os.path.isdir(target_dir):
            return f'Error: "{directory}" is not a directory'

        output_list = []
        items = os.listdir(target_dir)
        for i in items:
            full_path = os.path.join(target_dir, i)
            is_dir = "True" if os.path.isdir(full_path) else "False"
            size = os.path.getsize(full_path)
            output_list.append(f"  - {i}: file_size={size} bytes, is_dir={is_dir}")
        return "\n".join(output_list)
    
    except Exception as e:
        return f"Error: {e}"





