import os
import time

def remove_old_files(directory: str, exclude_filenames: list, days: int = 30):
    now = time.time()
    cutoff = now - days * 86400  # 30 days in seconds

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Skip directories and excluded files
        if (filename in exclude_filenames or not os.path.isfile(file_path)):
            continue
        file_mtime = os.path.getmtime(file_path)
        if file_mtime < cutoff:
            try:
                os.remove(file_path)
                print(f"Removed: {file_path}")
            except Exception as e:
                print(f"Could not remove {file_path}: {e}")

if __name__ == "__main__":
    script_name = os.path.basename(__file__)
    current_dir = os.path.dirname(os.path.abspath(__file__))
    exclude_files = [script_name, "README.md"]
    remove_old_files(current_dir, exclude_files)
