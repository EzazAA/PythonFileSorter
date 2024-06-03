**Automate Your Life Script**

This Python script, `automate_life.py`, is designed to help you organize your files by sorting them based on their file extensions. Below are instructions on how to get and use this script to automate your file management tasks.

### Getting Started
1. **Download the Script**: Download the `automate_life.py` script and save it to your desired location on your computer.

2. **Install Python**: Ensure you have Python installed on your system. You can download and install Python from [python.org](https://www.python.org/downloads/) if you haven't already.

### Usage
1. **Customize Source and Destination Directories**:
   - Open the `automate_life.py` script in a text editor.
   - Modify the `source_directory` and `destination_directory` variables to specify the directories you want to sort files from and move files to, respectively.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where you saved the `automate_life.py` script.
   - Run the script by executing the command: `python automate_life.py`.

3. **Sit Back and Relax**: The script will automatically organize your files by moving them from the source directory to destination directories based on their file extensions.

### Script Overview
- The `sort_files` function takes two parameters: `source_dir` and `destination_dir`.
- It iterates through each file in the `source_dir` directory.
- If the item is a file (not a directory), it extracts the file extension.
- It creates a destination folder based on the file extension if it doesn't already exist.
- Finally, it moves the file to the corresponding destination folder.

### Example
Suppose you have files in `/path/to/source/directory` that you want to organize, and you want to move them to `/path/to/destination/directory`. After customizing the source and destination directories in the script, you can run it to automate the file sorting process.

### Important Note
- Make sure to review and understand the script before running it, especially if you are working with important files. Test it on a small set of files to ensure it behaves as expected.

Enjoy a more organized file system with the help of this automation script! If you encounter any issues or have suggestions for improvement, feel free to reach out.
