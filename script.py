import os
import shutil

# Define file categories
file_categories = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.doc', '.docx', '.txt'],
    'Videos': ['.mp4', '.avi', '.mkv', '.mov'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Others': []  # Add other file extensions here
}

# Path to the directory containing downloaded files
download_directory = r'path_to_your_downloads_folder'

# Iterate over downloaded files
for filename in os.listdir(download_directory):
    if os.path.isfile(os.path.join(download_directory, filename)):
        file_extension = os.path.splitext(filename)[1]
        category = 'Others'  # Default category if not found
        for cat, extensions in file_categories.items():
            if file_extension.lower() in extensions:
                category = cat
                break
        
        # Create category folder if not exists
        category_folder = os.path.join(download_directory, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        
        # Move the file to the category folder
        shutil.move(os.path.join(download_directory, filename), os.path.join(category_folder, filename))
