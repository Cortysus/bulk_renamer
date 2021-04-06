# Bulk Renamer
 Bulk file and folder renamer with mapping dictionary.
 Creates a copy of a target directory and renames all the files and subdirectories in it, according to a mapping dictionary.
 It is compatible with Python 2.7.18.
 
 Copies are created in the same parent directory of the target directory.

 ## Test
 For a quick look at the program's functionality, execute the following command in the cloned repository:
 ```
 python main.py orig_folder
 ```
 
 This command will create a new folder `orig_folder_copy`. All the files and subdirectories of `orig_folder` are copied into `orig_folder_copy` and renamed according to `mapping_dict.json`.
 
 ## Use
 In order to use the program, create a `mapping_dict.json` with your desired renaming mapping. 
 Use the program on a custom directory `folder_to_bulk_rename` by executing the following command:
 ```
 python main.py folder_to_bulk_rename
 ```

 Caveauts:
 - the `main.py` and `mapping_dict.json` files MUST be in the same directory. 
 - It is preferable to put `main.py` and `mapping_dict.json` in a higher directory than `folder_to_bulk_rename`, but it is not necessary.
