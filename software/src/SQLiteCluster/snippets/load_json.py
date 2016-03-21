# loads a json file

def load_json(file_path):
    with open(file_path,'r') as f:
        tmp = f.read()
        from json import loads 
        return(loads(tmp))
        