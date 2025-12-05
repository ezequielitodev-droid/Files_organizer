import logging
import os
from dotenv import load_dotenv
from pathlib import Path
from files_organizer.resource_loader import load_env

load_env()

def create_log_structure() -> None:

    Path(f"{os.getenv("FODER_SAFE_MOVE_FILE")}").mkdir(parents=True, exist_ok=True)

    structure = [
        os.getenv("SAFE_MOVE_FILE_LOG"), 
        os.getenv("SAFE_COPY_FILE_LOG"), 
        os.getenv("BACKUP_FOLDER_LOG"), 
        os.getenv("SCAN_FILE_LOG"), 
        os.getenv("CLASSIFY_FILE_LOG"), 
        os.getenv("DECIDE_DESTINATION_LOG"),
        os.getenv("RUN_ORGANIZER_LOG")
    ]

    for file_path in structure:
        file = Path(f"{file_path}")
        file.parent.mkdir(parents=True, exist_ok=True)
        file.touch(exist_ok=True)

create_log_structure()

# Setting up Logging:

format = logging.Formatter(
    fmt="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

logger_move = logging.getLogger("mover")
logger_move.setLevel(logging.INFO)

fh_move = logging.FileHandler(f"{os.getenv("SAFE_MOVE_FILE_LOG")}", encoding="utf-8" )
fh_move.setLevel(logging.INFO)

fh_move.setFormatter(format)

logger_move.addHandler(fh_move)



logger_copy = logging.getLogger("copiar")
logger_copy.setLevel(logging.INFO)

fh_copy = logging.FileHandler(f"{os.getenv("SAFE_COPY_FILE_LOG")}", encoding="utf-8")
fh_copy.setLevel(logging.INFO)

fh_copy.setFormatter(format)

logger_copy.addHandler(fh_copy)



logger_backup = logging.getLogger("backup")
logger_backup.setLevel(logging.INFO)

fh_backup = logging.FileHandler(f"{os.getenv("BACKUP_FOLDER_LOG")}", encoding="utf-8")
fh_backup.setLevel(logging.INFO)

fh_backup.setFormatter(format)

logger_backup.addHandler(fh_backup)



logger_scan = logging.getLogger("scan")
logger_scan.setLevel(logging.INFO)

fh_scan = logging.FileHandler(f"{os.getenv("SCAN_FILE_LOG")}", encoding="utf-8")
fh_scan.setLevel(logging.INFO)

fh_scan.setFormatter(format)

logger_scan.addHandler(fh_scan)



logger_classify = logging.getLogger("classify")
logger_classify.setLevel(logging.INFO)

fh_classify = logging.FileHandler(f"{os.getenv("CLASSIFY_FILE_LOG")}", encoding="utf-8")
fh_classify.setLevel(logging.INFO)

fh_classify.setFormatter(format)

logger_classify.addHandler(fh_classify)



logger_destination = logging.getLogger("destination")
logger_destination.setLevel(logging.INFO)

fh_destination = logging.FileHandler(f"{os.getenv("DECIDE_DESTINATION_LOG")}", encoding="utf-8")
fh_destination.setLevel(logging.INFO)

fh_destination.setFormatter(format)

logger_destination.addHandler(fh_destination)



logger_organizer = logging.getLogger("organizer")
logger_organizer.setLevel(logging.INFO)

fh_organizer = logging.FileHandler(f"{os.getenv("RUN_ORGANIZER_LOG")}", encoding="utf-8")
fh_organizer.setLevel(logging.INFO)

fh_organizer.setFormatter(format)

logger_organizer.addHandler(fh_organizer)