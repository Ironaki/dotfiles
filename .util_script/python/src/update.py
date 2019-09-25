"""
Copy the file from src folder to the parent folder
Drop .py extension
Chmod the new file to 755

Change the FILES variable, if you add or delete files
"""

from shutil import copyfile
from os import chmod

# Change this variable, if you add or delete files
FILES = ["vocab", "lcinit", "csv2ledger_preprocess"]

for file_name in FILES:
    old_file = file_name+".py"
    new_file = "../"+file_name
    copyfile(old_file, new_file)
    chmod(new_file, 0o755)
    chmod(old_file, 0o644)
