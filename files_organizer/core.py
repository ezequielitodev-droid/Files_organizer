from datetime import date
import os
from pathlib import Path
from dotenv import load_dotenv

from files_organizer.logging_config import (
    logger_scan,
    logger_classify,
    logger_destination,
    logger_organizer
)
from files_organizer.organizer import (
    extension_to_category,
    category_to_path
)
from files_organizer.utils import (
    backup_folder,
    safe_move_file
)

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

# The organizer function changes depending on the organization:

def run_organizer(src: Path) -> None: pass