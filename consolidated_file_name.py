def consolidated_file_name():
    
    while True:
        
        raw_consolidated_file_name = input("\n        🟡 Enter the name for the consolidated file (without extension): ")
        clean_consolidated_file_name = raw_consolidated_file_name.strip()

        if clean_consolidated_file_name == "":
            print("\n          🔴 The file name cannot be empty. Please try again.")

        else:
            file_name = clean_consolidated_file_name + ".txt"
            print(f"\n          🟢 Consolidated file will be named: {file_name}")
            break
        
    return file_name