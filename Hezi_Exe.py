import hashlib
from datetime import datetime
import os

folder_path = os.getenv("HASH_FOLDER", "C:/Users/taljo/Downloads/hezi_exe")

file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, file))]

for file in file_paths:
    # Skip files that already have a timestamp in their name
    if any(part.isdigit() for part in os.path.basename(file).split("_")):
        continue

    with open(file, 'r+') as f:
        string = f.read()
        hash_object = hashlib.sha256(string.encode())
        hex_dig = hash_object.hexdigest()
        f.write("\n***\n" + hex_dig + "\n***")

    current_datetime = datetime.now()
    name, extension = os.path.splitext(file)
    new_name_file = f"{name}_{current_datetime.strftime('%Y%m%d_%H%M%S')}{extension}"
    os.rename(file, new_name_file)

    print(f"Processing file: {file}")
    print(f"Generated hash: {hex_dig}")
    print(f"Renaming file to: {new_name_file}")
