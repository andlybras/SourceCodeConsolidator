import os

def executing_consolidation(clean_path_directory_to_consolidate, file_name):
    
    parent_directory_items = os.listdir(clean_path_directory_to_consolidate)
    
    index_of_parent_directory_items = {}

    for index, item in enumerate(parent_directory_items, start=1):
        index_of_parent_directory_items[index] = item

    save_path = os.path.join(clean_path_directory_to_consolidate, file_name)

    with open(save_path, 'w', encoding='utf-8') as file:
        
        console_header = "\n              🟢 DIRECTORY INDEX:\n"
        file_header = "--- DIRECTORY INDEX ---\n\n" 

        print(console_header)
        file.write(file_header)

        for key, value in index_of_parent_directory_items.items():
        
            console_line = f"              🔸 {key} ➖ {value}"
            file_line = f"{key} ➖ {value}\n" 

            print(console_line)
            file.write(file_line)


    print(f"\n                🟢 Consolidation executed successfully. The file '{file_name}' has been created.")