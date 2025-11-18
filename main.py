import os
from dotenv import load_dotenv
from pathlib import Path
from files_organizer.core import run_organizer

load_dotenv()

if __name__ == "__main__":
    folder_path = os.getenv("DOWNLOAD_PATH")
    if folder_path is None: raise ValueError("The environment variable FOLDER_TO_ORGANIZE is not defined")

    run_organizer(Path(folder_path))