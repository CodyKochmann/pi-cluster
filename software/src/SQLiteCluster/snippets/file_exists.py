# returns a boolean if the file exists

import read_file 

def file_exists(file_path):
    from os import path
    return(path.isfile(file_path))
