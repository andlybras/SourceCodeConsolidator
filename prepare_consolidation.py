import os
import time
from executing_consolidation import executing_consolidation
from consolidated_file_name import consolidated_file_name

def validating_path_clock():
    clock_icons = ["🕐", "🕑", "🕒", "🕓", "🕔", "🕕", "🕖", "🕗", "🕘", "🕙", "🕚", "🕛"]
    print("")

    for clock in clock_icons:
        print(f"\r      🟢 Validating path... {clock} ", end="")
        time.sleep(0.2)

    print("")

def prepare_consolidation():
    print("\n" + "🔹" * 43)
    print("\n    🟢 Starting consolidation preparing")

    while True:

        raw_path_directory_to_consolidate = input("\n    🟡 Enter the path of the directory to consolidate: ")
        clen_path_directory_to_consolidate = raw_path_directory_to_consolidate.strip().strip("'\"")

        if os.path.isdir(clen_path_directory_to_consolidate) is False:
            validating_path_clock()
            print("\n        🔴 The entered path is not a valid directory. Please try again.")

        else:
            validating_path_clock()
            print("\n        🟢 Directory path validated successfully")
            consolidated_file_name()
            print("\n          🟢 Executing consolidation...")
            executing_consolidation()
            break