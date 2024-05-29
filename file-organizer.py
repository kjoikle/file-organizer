import os
import shutil

# Define the directory to be organized
desktop_dir = os.path.join(os.path.join(os.path.expanduser('~')), 'Desktop')
other_folder_name = 'Other'

# Define the mapping of file types to folder names
file_type_mappings = {
    'Documents': ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
    'Scripts': ['.py', '.sh', '.bat'],
    'Executables': ['.exe', '.msi']
}

# creates folders with the names as defined by the keys above, plus an Other folder
def make_folders():
    for name in file_type_mappings.keys():
        folder_path = os.path.join(desktop_dir, name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    other_path = os.path.join(desktop_dir, other_folder_name)
    if not os.path.exists(other_path):
        os.makedirs(other_path)

def organize_files():
    for item in os.listdir(desktop_dir):
        item_path = os.path.join(desktop_dir, item)
        if os.path.isfile(item_path):
            move_file(item_path)

# moves file into appropriate folder
def move_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    for folder_name, extensions in file_type_mappings.items():
        if ext in extensions:
            folder_path = os.path.join(desktop_dir, folder_name)
            shutil.move(file_path, folder_path)
            print("Moved {file_path} to {folder_path}")
            break
    shutil.move(file_path, os.path.join(desktop_dir, other_folder_name))

def main():
    make_folders()
    organize_files()
    print("Done!")

if __name__ == "__main__":
    main()