import os

def executing_consolidation(clean_path_directory_to_consolidate, file_name):
    
    parent_directory_items = os.listdir(clean_path_directory_to_consolidate)
    
    index_of_parent_directory_items = {}

    for index, item in enumerate(parent_directory_items, start=1):
        index_of_parent_directory_items[index] = item

    print("\n              🟢 DIRECTORY INDEX:\n")
    for key, value in index_of_parent_directory_items.items():
        print(f"              🔸 {key} ➖ {value}")


    print(f"\n                🟢 Consolidation executed successfully. The file '{file_name}' has been created.")