import os
import shutil

def sort_files(source_dir, destination_dir):
    for filename in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, filename)):
            file_extension = filename.split(".")[-1]
            destination_folder = os.path.join(destination_dir, file_extension)
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)
            shutil.move(os.path.join(source_dir, filename), os.path.join(destination_folder, filename))

source_directory = "/path/to/source/directory"
destination_directory = "/path/to/destination/directory"

sort_files(source_directory, destination_directory)
