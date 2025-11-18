import os
from download_organizer.utils import (
    backup_folder,
    safe_move_file
)
from pathlib import Path
from download_organizer.organizer import (
    extension_to_category,
    category_to_path,
    TEMPORARY_EXTENSIONS
)
from download_organizer.logging_config import (
    logger_scan,
    logger_classify,
    logger_destination,
    logger_organizer
)
from dotenv import load_dotenv
from datetime import date

load_dotenv()

def scan_files(src: Path) -> list:
    
    """
    Scan a directory and return all files contained in it.

    This function inspects the given directory and collects every item that is a file.
    Subdirectories are ignored. The result is a flat list containing only the files
    directly inside the source folder. The process is logged, including success,
    warnings, and unexpected errors.

    Parameters
    ----------
    src : Path
        The directory to scan.

    Returns
    -------
    list
        A list of Path objects representing each file found in the directory.

    Notes
    -----
    - If the source path does not exist, a warning is logged and an empty list is returned.
    - If the source path exists but is not a directory, a warning is logged and an empty list is returned.
    - Only items that are regular files are included. Directories are ignored.

    Examples
    --------
    >>> from pathlib import Path
    >>> files = scan_files(Path("C:/Users/Ezequiel/Downloads"))
    >>> len(files) >= 0
    True
    """

    list_src = []

    try:

        if not src.exists(): raise FileNotFoundError(f"Sorce does not exist: {src}")

        if not src.is_dir(): raise FileNotFoundError(f"Source path is not a directory: {src}")

        for item in src.iterdir():
            if item.is_file(): list_src.append(item)

        logger_scan.info(f"Scan completed successfully. Items found: {len(list_src)}")
    
    except FileNotFoundError as e:
        
        logger_scan.warning(f"Scan failed: {e}")

    except Exception as e: 

        logger_scan.error(f"Unexpected error during scan: {e}")

    return list_src
        
def classify_file(file: Path) -> str:

    """
    Classifies a file based on its extension.

    The function extracts the file suffix, converts it to lowercase,
    and looks it up in the extension-to-category mapping. If the 
    extension exists in the mapping, its category is returned. 
    Otherwise, the function returns "unknown". The classification 
    result is also logged.

    Parameters:
        file (Path): The file to classify.

    Returns:
        str: The detected category for the file, or "unknown" if no
             matching extension is found.
    """

    ext = file.suffix.lower()

    classify = extension_to_category.get(ext, "unknown")

    logger_classify.info(f"File classified: {file.name} -> Category: {classify}")

    return classify
        
def decide_destination(classify: str) -> Path | None:

    """
    Determine the destination path for a given file category.

    Parameters
    ----------
    classify : str
        The category assigned to the file (e.g., "images", "documents").

    Returns
    -------
    Path | None
        A Path object pointing to the destination directory if the category
        exists in `category_to_path`. Returns None if the category is unknown.

    Notes
    -----
    If the category is not found, a warning is logged and None is returned.
    """

    destination_str = category_to_path.get(classify)

    if destination_str is None: 

        logger_destination.warning(f"Unknown category '{classify}'. No destination found.")
        logger_destination.info("Returning None as destination.")
        destination = None
    else: 
        destination = Path(destination_str)

        logger_destination.info(f"Category '{classify}' mapped to destination: '{destination}'")

    return destination

def organizer_files(src: Path) -> None:

    """
    Organize files in a directory by creating a backup, scanning, classifying, and moving them.

    This function performs a full workflow on the specified source directory:
    1. Creates a backup of the current files in a folder named with today's date.
    2. Scans the directory and collects all files.
    3. Classifies each file, decides its destination, and moves it safely.
    The process is logged, including success, warnings, and errors.

    Parameters
    ----------
    src : Path
        The directory to organize.

    Returns
    -------
    None
        This function does not return a value; its effect is modifying the filesystem.

    Notes
    -----
    - If the source path does not exist, a warning is logged and no action is taken.
    - Files are only moved if a valid destination is determined.
    - Backup and file movements are logged for traceability.
    - Only files (not directories) are considered in the workflow.

    Examples
    --------
    >>> from pathlib import Path
    >>> organizer_files(Path("C:/Users/Ezequiel/Downloads"))
    """

    # First part of the workflow: Backup

    path_backup = Path(f"{os.getenv("BACKUP_PATH")}")

    # Create today's backup folder

    today = date.today()
    date_string = str(today)
    path_backup_actual = path_backup / date_string

    backup_folder(src, path_backup_actual)

    # Second part of the workflow: Scan

    scanned_list = scan_files(src)

    # Third part of the workflow: Classify, decide destination, and move

    for item in scanned_list:

        
        # Classify

        classify = classify_file(item)

        # Decide destination

        destination = decide_destination(classify)

        # Move the file if destination exists

        if not (destination is None): safe_move_file(item, destination)

        else: logger_organizer.warning(f"Error moving file: {item.name}")

