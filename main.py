import json
import glob
import os
import shutil
import sys

# Rename an item (file or dir) using a mapping dictionary
def rename_item(item, mapping_dict):
    new_item = item
    # Iterate over dict and map keys to values in new_item string
    for key, value in mapping_dict.items():
        new_item = new_item.replace(key, value)

    # If file is being renamed
    if item != new_item:
        print('Renaming: ' + item + ' ------> ' + new_item)
        try:
            os.rename(item, new_item)
        except OSError as exc:
            print(exc)
    pass

# Process a directory
def process_directory(directory, mapping_dict):
    for subdir,dirs,files in os.walk(directory):
        # Process files
        for f in files:
            full_path = os.path.join(subdir, f)
            rename_item(full_path, mapping_dict=mapping_dict)
        # Process subdirectories
        for d in dirs:
            full_path = os.path.join(subdir, d)
            rename_item(full_path, mapping_dict=mapping_dict)
            process_directory(full_path, mapping_dict=mapping_dict)
    pass


def main():
    # Load mapping dictionary
    with open("mapping_dict.json") as f:
        mapping_dict = json.load(f)

    # Define target directory from command line
    if len(sys.argv) > 1 &  os.path.isdir(sys.argv[1]):
        print('Target: ' + sys.argv[1])
        print('')
    else:
        raise Exception('Directory not specified!')
    
    # Define destination directory
    work_dir = sys.argv[1]
    dest_dir = work_dir + "_copy"

    if os.path.exists(dest_dir):
        raise Exception('Directory ' + dest_dir + ' exists already.')

    # Create full copy of original directory into destination directory
    shutil.copytree(work_dir, dest_dir)
    
    # Process directory
    process_directory(dest_dir, mapping_dict=mapping_dict)

    
if __name__ == "__main__":
    main()