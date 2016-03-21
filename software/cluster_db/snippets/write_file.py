# creates or updates a file with the given text

def write_file(file_path,text_to_write):
    with open(file_path,'w') as f:
        f.write(text_to_write)
        return
