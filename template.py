import os
from pathlib import Path
import logging

# used instead of print statement to understand each step in terminal
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:') 

project_name = 'cnnClassifier'

list_of_files = [
    "github/workflows/.gitkeep",
    f"source/{project_name}/__init__.py",
    f"source/{project_name}/components/__init__.py",
    f"source/{project_name}/utils/__init__.py",
    f"source/{project_name}/config/__init__.py",
    f"source/{project_name}/config/configuration.py",
    f"source/{project_name}/pipeline/__init__.py",
    f"source/{project_name}/entity/__init__.py",
    f"source/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html"
]
print(list_of_files)

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir, filename = os.path.split(file_path)

    # Creating file directory or path using makedirs
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Creating files inside the directory
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, "w") as f:
            pass
        logging.info(f"Creating empty file: {file_path}")
    else:
        logging.info(f"{filename} already exists")