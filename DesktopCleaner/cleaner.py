import os
import shutil
from pathlib import Path

# Define file categories based on extensions
FILE_CATEGORIES = {
    "Images": ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    "Documents": ['.pdf', '.docx', '.txt', '.xlsx', '.pptx'],
    "Audio": ['.mp3', '.wav', '.aac'],
    "Videos": ['.mp4', '.avi', '.mkv', '.mov'],
    "Archives": ['.zip', '.tar', '.rar', '.gz']
}

# Function to create a folder if it doesn't exist
def create_folder(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to organize files in the Downloads folder based on file type
def organize_files(download_folder):
    for filename in os.listdir(download_folder):
        file_path = os.path.join(download_folder, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Get the file extension
        file_extension = Path(filename).suffix.lower()

        # Loop through categories to find the matching file type
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category_folder = os.path.join(download_folder, category)
                create_folder(category_folder)
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved {filename} to {category}")
                break

# Main function to run the script
def main():
    download_folder = str(Path.home() / "Downloads")  # Path to Downloads folder
    organize_files(download_folder)
    print("Cleaning completed!")

if __name__ == "__main__":
    main()
