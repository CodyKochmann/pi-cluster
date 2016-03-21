# loads a json file

import read_file 

def load_json_file(file_path):
    from json import loads
    return(loads(read_file(file_path)))