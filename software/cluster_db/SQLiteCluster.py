# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-21 14:15:22
# @Last Modified 2016-03-21
# @Last Modified time: 2016-03-21 15:32:58

# this is the primary control for the database 
# that will be used in the raspberry pi cluster

# since sqlite is limited to 2GB in the raspberry
# pi due to it being 32-bit, the database will be
# designed off of a cluster of multiple sqlite 
# instances.

# each pi will have 4 databases that it will own
# along with a backup of each database on its 
# siblings in order to promise maximum redundancy

# All applications will be evenly distributed
# throughout the databases and will be seperated 
# by the tables they require


from snippets import *
import sqlite3

class SQLiteClutster():
    """ the primary class that controls all 
        database functionality for the cluster
    """
    def __init__(self, pi_count=4, dbs_per_pi=4):
        self.pi_count = pi_count
        self.dbs_per_pi = dbs_per_pi
        self.hostname = get_host_name() # finds out if its name is pi-123or4

cluster_db = SQLiteClutster()
