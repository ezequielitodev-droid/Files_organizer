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