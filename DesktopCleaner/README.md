## How the Code Works

Desktop Cleaner Script Explanation
This Python script organizes files in your Downloads folder by moving them into specific folders based on their file type (e.g., Images, Documents, Audio, etc.). Here's a breakdown of how the code works:

Prerequisites
Before running the script, ensure that you have Python installed on your system. You can download Python from here.

If you don't have any additional libraries installed (e.g., pathlib), you can install them via pip. However, most of the libraries used in this script (like os, shutil, and pathlib) come pre-installed with Python, so there's no need to install them separately.

To install any external libraries, you can use pip from the terminal:

```
pip install pathlib 
```

This line of code assigns the path to the user's "Downloads" folder to the variable download_folder. The Path.home() function retrieves the home directory of the current user, and the "Downloads" string is replaced with the appropriate path to the user's download folder on their system.

```
download_folder = str(Path.home() / "Downloads")  # Change the Downloads with your download folders path
```

Run the file:
```
python clener.py
```
