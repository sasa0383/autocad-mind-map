import os

def parse_abt_file(file_path):
    """
    Parse the .abt file and extract directories and files.
    """
    directories = []
    files = []
    current_section = None

    print(f"Attempting to read .abt file from: {file_path}")  # Debugging

    if not os.path.exists(file_path):
        print("Error: .abt file not found!")
        return directories, files

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            print(f"Processing line: '{line}'")  # Debugging: Show each line being read
            if not line or line.startswith("#"):
                continue
            if line.startswith("[") and line.endswith("]"):
                current_section = line[1:-1].lower()
                print(f"Switching to section: {current_section}")  # Debugging
                continue
            if current_section == "directories":
                directories.append(line)
            elif current_section == "files":
                files.append(line)

    print(f"Parsed Directories: {directories}")  # Debugging
    print(f"Parsed Files: {files}")  # Debugging
    return directories, files

def create_directories(base_dir, directories):
    """
    Create directories listed in the .abt file.
    """
    for directory in directories:
        try:
            full_path = os.path.join(base_dir, directory)
            os.makedirs(full_path, exist_ok=True)
            print(f"Directory created: {full_path}")
        except Exception as e:
            print(f"Error creating directory {directory}: {e}")

def create_files(base_dir, files):
    """
    Create files listed in the .abt file.
    """
    for file in files:
        try:
            full_path = os.path.join(base_dir, file)
            directory = os.path.dirname(full_path)
            if directory:
                os.makedirs(directory, exist_ok=True)
            with open(full_path, 'a'):
                os.utime(full_path, None)  # Update timestamp or create file
            print(f"File created: {full_path}")
        except Exception as e:
            print(f"Error creating file {file}: {e}")

if __name__ == "__main__":
    # Dynamically resolve base directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    abt_file_path = os.path.join(script_dir, "project2_setup.abt")

    print("Starting environment setup...")
    print(f"Resolved .abt file path: {abt_file_path}")
    if not os.path.exists(abt_file_path):
        print("Error: Specified .abt file path does not exist!")
        exit(1)

    directories, files = parse_abt_file(abt_file_path)

    if not directories and not files:
        print("No directories or files found in .abt file. Exiting.")
    else:
        create_directories(script_dir, directories)
        create_files(script_dir, files)

    print("Environment setup complete.")
