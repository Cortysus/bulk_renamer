import json
import glob
import os
import shutil
import sys

def rename_item(item, mapping_dict):
    new_item = item
    for key, value in mapping_dict.items():
        new_item = new_item.replace(key, value)

    if item != new_item:
        print('Renaming: ' + item + ' ------> ' + new_item)
        try:
            os.rename(item, new_item)
        except OSError as exc:
            print(exc)
    pass

def process_directory(directory, mapping_dict):
    for subdir,dirs,files in os.walk(directory):
        for f in files:
            full_path = os.path.join(subdir, f)
            rename_item(full_path, mapping_dict=mapping_dict)

        for d in dirs:
            full_path = os.path.join(subdir, d)
            rename_item(full_path, mapping_dict=mapping_dict)
            process_directory(full_path, mapping_dict=mapping_dict)
    pass


def main():
    with open("mapping_dict.json") as f:
        mapping_dict = json.load(f)

    if len(sys.argv) > 1 &  os.path.isdir(sys.argv[1]):
        print('Target: ' + sys.argv[1])
        print('')
    else:
        raise Exception('Directory not specified!')
    
    work_dir = sys.argv[1]
    dest_dir = work_dir + "_copy"

    if os.path.exists(dest_dir):
        raise Exception('Directory ' + dest_dir + ' exists already.')

    # Create full copy of original directory
    shutil.copytree(work_dir, dest_dir)
    
    process_directory(dest_dir, mapping_dict=mapping_dict)

    
if __name__ == "__main__":
    main()