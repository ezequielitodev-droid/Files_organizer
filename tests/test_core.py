import os
from files_organizer.core import (
    scan_files,
    classify_file,
    decide_destination,
    run_organizer
)
from pathlib import Path
from dotenv import load_dotenv


#path_test_scan = Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests/tests_folder")


#for item in scan_files(path_test_scan):
#    print(f"\n {item}")


#path_test_file_1 = Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests/tests_folder/file3.pdf")
#path_test_file_2 = Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests/tests_folder/file11.py")
#path_test_file_3 = Path("C:/Users/Ezequiel/Dev/automation_scripts/Level 1 - Fundamentals/download_organizer/tests/tests_folder/file7.png")

#classify_1 = classify_file(path_test_file_1)
#classify_2 = classify_file(path_test_file_2)
#classify_3 = classify_file(path_test_file_3)

#print("\n")
#print(classify_1)
#print("\n")
#print(classify_2)
#print("\n")
#print(classify_3)
#print("\n")

#destination_1 = decide_destination(classify_1)
#destination_2 = decide_destination(classify_2)
#destination_3 = decide_destination(classify_3)
#destination_4 = decide_destination("Popo")

#print(destination_1)
#print("\n")
#print(destination_2)
#print("\n")
#print(destination_3)
#print("\n")
#print(destination_4)
#print("\n")

path_test_organizer = Path(f"{os.getenv("DOWNLOAD_PATH")}")

run_organizer(path_test_organizer)