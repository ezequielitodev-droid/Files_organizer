import logging
import os
from dotenv import load_dotenv

load_dotenv()

#Configuramos los Logging:

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

fh_organizer = logging.FileHandler(f"{os.getenv("ORGANIZER_FILES_LOG")}", encoding="utf-8")
fh_organizer.setLevel(logging.INFO)

fh_organizer.setFormatter(format)

logger_organizer.addHandler(fh_organizer)