def get_host_name():
    # returns the hostname of the machine
    import socket
    return(socket.gethostname())