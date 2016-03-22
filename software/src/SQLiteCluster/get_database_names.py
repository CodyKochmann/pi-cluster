from load_config import *

def get_database_names():
    # returns an array of paths for the local database's to exist
    from snippets import get_host_name 
    output=[]
    hostname=get_host_name()
    for i in range(load_config("dbs_per_pi")):
        output.append("%s.%s.db"%(hostname,(i+1)))
    return(output)
