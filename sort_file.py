from pathlib import Path
import os
import shutil

test = r'C:\Users\Kulilits\Documents\Maco\Test Fol 1\Health Q1 PT pics\F\New folder'

def get_all_types(target_folder_path):
    target_folder: Path = Path(target_folder_path)
    file_types:list = []

    #CHECK IF WORKS
    file_types = list(map(lambda file: file.suffix.upper(),[file for file in target_folder.iterdir() if file.is_file()]))


    file_types = list(set(file_types))
    return file_types

def create_file_type_folders(target_folder_path, file_types=None):
    target_folder = Path(target_folder_path)
    if file_types is None:
        file_types = get_all_types(target_folder)
    for file_type in file_types:
        (target_folder / file_type).mkdir(parents=True, exist_ok=True)

def sort_for_keyword(target_folder_path,keywords: list,foldernames:list =[]):

    #Keywords should be a list. Foldernames should be a list
    #the folder name for keyword is same as index in foldername
    target_folder = Path(target_folder_path)
    cleaned_keywords = []
    cleaned_foldernames = []

    for i,keyword in enumerate(keywords): #makes sure that there are files that have that keyword

        is_in_filenames = any(keyword in file.name for file in target_folder.iterdir())
        if is_in_filenames:
            cleaned_foldernames.append(f"&arranged& {foldernames[i]}") #&arranged& is added so that the folders for  the organized stuff is not iterated through
            cleaned_keywords.append(keyword.lower())

    print(cleaned_keywords,cleaned_foldernames)

    for i, keyword in enumerate(cleaned_keywords): #makes a dir for each keyword
        foldername = cleaned_foldernames[i]
        (target_folder / foldername).mkdir(parents=True, exist_ok=True)

    for file in target_folder.iterdir(): #moves the files

        filename = file.name.lower()
        # FOR FUTURE ME: no need to make this a one liner
        if "&arranged&" in filename:
            pass
        else:
            for i, _keyword in enumerate(cleaned_keywords):
                if _keyword in filename:
                    folder_to_send = cleaned_foldernames[i]
                    if folder_to_send != '' or folder_to_send != None:
                        dir_path=f'{target_folder_path}/{folder_to_send}'
                        shutil.move(file, dir_path)

    for file in target_folder.iterdir():
        filename = file.name
        if '&arranged&' in filename:
            new_filename = filename.replace("&arranged&","")
            os.rename(str(file),f"{str(file.parent)}\\{new_filename}")


# create_folders_for_keyword(test,['Q3','Q1','New'],['Quarter 3','Quarter 1','Random'])