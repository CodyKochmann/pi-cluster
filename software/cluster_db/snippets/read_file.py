# returns the contents of a file

def read_file(file_path):
    with open(file_path,'r') as f:
        return(f.read())
        