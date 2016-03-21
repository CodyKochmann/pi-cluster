# returns a boolean if the file exists

import read_file 

def file_exists(file_path):
    from os import path
    if(path.isfile(fname)):
        if(len(read_file(file_path))>0):
            return(True)
    return(False)
