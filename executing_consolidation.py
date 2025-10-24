import os
import pathspec

def executing_consolidation(clean_path_directory_to_consolidate, file_name):
    
    spec = None
    gitignore_path = os.path.join(clean_path_directory_to_consolidate, '.gitignore')

    if os.path.exists(gitignore_path):
        print("\n              🟢 .gitignore found. Loading rules...")
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            patterns = f.read()
            spec = pathspec.PathSpec.from_lines('gitwildmatch', patterns.splitlines())

    else:
        print("\n              🟠 .gitignore not found. Indexing all files.")
    
    def walk_directory(current_path, current_relative_path, prefix, file_handle, spec, files_to_transcribe):
        
        try:
            items = os.listdir(current_path)

        except PermissionError:
            error_line = f"{prefix} [ACESSO NEGADO] {os.path.basename(current_path)}\n"
            print(f"              🟠 ACESSO NEGADO: {current_path}")
            file_handle.write(error_line)
            return 

        filtered_items = []
        item_data = {} 

        for item_name in items:
            if item_name == ".git":
                continue
            
            full_item_path = os.path.join(current_path, item_name)
            new_relative_path = os.path.join(current_relative_path, item_name)
            path_for_spec = new_relative_path.replace(os.path.sep, '/')
            
            if spec and spec.match_file(path_for_spec):
                continue
            
            if os.path.isdir(full_item_path) and spec and spec.match_file(path_for_spec + '/'):
                continue
            
            filtered_items.append(item_name)
            item_data[item_name] = (full_item_path, new_relative_path)

        filtered_items.sort()

        for index, item_name in enumerate(filtered_items, start=1):
            
            new_prefix = f"{prefix}{index}."
            full_item_path, new_relative_path = item_data[item_name]

            if os.path.isdir(full_item_path):
                console_line = f"                  🔸 {new_prefix} {item_name}/"
                file_line = f"{new_prefix} {item_name}/\n"

                print(console_line)
                file_handle.write(file_line)
                walk_directory(
                    full_item_path,
                    new_relative_path,
                    new_prefix,
                    file_handle,
                    spec,
                    files_to_transcribe 
                )
            
            else:
                console_line = f"                  🔸 {new_prefix} {item_name}"
                file_line = f"{new_prefix} {item_name}\n"

                print(console_line)
                file_handle.write(file_line)
                files_to_transcribe.append((full_item_path, new_relative_path))
    
    parent_dir_path = os.path.dirname(clean_path_directory_to_consolidate)
    full_save_path = os.path.join(parent_dir_path, file_name)
    files_to_transcribe = []

    print("\n                🟢 Generating recursive index...")

    try:
        with open(full_save_path, 'w', encoding='utf-8') as file:
            
            console_header = "\n                  🟢 DIRECTORY INDEX:\n"
            file_header = "--- DIRECTORY INDEX ---\n\n" 

            print(console_header)
            file.write(file_header)
            walk_directory(
                clean_path_directory_to_consolidate, 
                "",
                "",  
                file, 
                spec,     
                files_to_transcribe 
            )
            print("\n                    🟢 Index generated. Transcribing file contents...")
            
            content_header = "\n\n" + ("=" * 20) + " FILE CONTENTS " + ("=" * 20) + "\n\n"
            file.write(content_header)
            
            for full_path, relative_path in files_to_transcribe:
                file_header = f"--- Content of: {relative_path.replace(os.path.sep, '/')} ---\n\n"
                file.write(file_header)
                
                try:
                    with open(full_path, 'r', encoding='utf-8') as content_file:
                        content = content_file.read()
                        file.write(content)
                        
                except UnicodeDecodeError:
                    file.write(f"[Error: Could not read file. Content is likely binary.]\n")

                except Exception as e:
                    file.write(f"[Error reading file: {e}]\n")

                file.write("\n\n")

        print(f"\n                      🟢 Consolidation executed successfully. The file has been saved in:")
        print(f"                  {full_save_path}")

    except Exception as e:
        print(f"\n                🔴 An error occurred while trying to write the file: {e}")