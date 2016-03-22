def get_host_name():
    # returns the hostname of the machine
    from socket import gethostname
    output = gethostname()
    if 'pi-' not in output:
        output='pi-1'
    return(output)
    