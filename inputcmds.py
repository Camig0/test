import tkinter
from tkinter import filedialog


def get_target_dir():
    tkinter.Tk().withdraw()  # prevents an empty tkinter window from appearing
    folder_path = filedialog.askdirectory()
    return folder_path
def mode():
    mode:str = ''
    while mode not in ('BK','FT','END'):
        print("""
        ===================MODES===================
         ~~~~~~~~~~~~~~by keyword: BK~~~~~~~~~~~~~
         ~~~~~~~~~~~~~by file type: FT~~~~~~~~~~~~
         ~~~~~~~~~~~~~end program: END~~~~~~~~~~~~
        ===========================================
         """)
        mode = input("INPUT MODE: ").upper()
    return mode
def BK(): #bykeyword


    #returns keyword and foldername
    inp:str = ''
    _keywords:list = []
    _folder_names: list = []
    print('INPUT KEYWORD FOLLOWED BY THE FOLDER FOR THAT KEYWORD')
    while inp.upper() != "END":

        keyword:str = input("keyword: ")
        folder_name:str = input("folder name: ")
        _keywords.append(keyword)
        _folder_names.append(folder_name)
        inp = input('ENTER END TO END INPUTING: ')
    return set(_keywords), set(_folder_names)