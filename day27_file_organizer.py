# Day 27 - Simple File Organizer

import os
import shutil

print("=== File Organizer ===")

folder_path = input("Enter folder path: ")

# File type folders
image_folder = os.path.join(folder_path, "Images")
doc_folder = os.path.join(folder_path, "Documents")
other_folder = os.path.join(folder_path, "Others")

# Create folders if not exist
os.makedirs(image_folder, exist_ok=True)
os.makedirs(doc_folder, exist_ok=True)
os.makedirs(other_folder, exist_ok=True)

# File extensions
image_ext = [".jpg", ".png", ".jpeg"]
doc_ext = [".pdf", ".txt", ".docx"]

# Loop through files
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        if any(file.endswith(ext) for ext in image_ext):
            shutil.move(file_path, image_folder)

        elif any(file.endswith(ext) for ext in doc_ext):
            shutil.move(file_path, doc_folder)

        else:
            shutil.move(file_path, other_folder)

print("Files organized successfully 📁")
