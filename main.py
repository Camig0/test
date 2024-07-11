import sort_file
import inputcmds

if __name__ == '__main__':
    mode: str = ''
    print('FILE SORTER PROGRAM')
    while mode != 'END':
        target_folder = inputcmds.get_target_dir()
        mode = inputcmds.mode()
        if mode == 'BK':
            print('should be selecting folder rn')

            BK_ = inputcmds.BK()
            keywords: list = list(BK_[0])
            folder_names: list = list(BK_[1])

            sort_file.sort_for_keyword(target_folder,keywords,folder_names)
