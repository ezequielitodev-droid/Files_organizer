import os
import sys
from dotenv import load_dotenv

def resource_path(rel_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, rel_path)
    return rel_path

def load_env():
    env_path = resource_path(".env")
    load_dotenv(env_path)