# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-21 14:15:22
# @Last Modified by:   CodyKochmann
# @Last Modified time: 2016-03-21 14:28:10

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

pi_count = 4   # the number of raspberry pis
dbs_per_pi = 4 # number of databases per pi

class SQLiteClutster():
    """ the primary class that controls all 
        database functionality for the cluster
    """
    def __init__(self, pi_count, dbs_per_pi):
        self.pi_count = pi_count
        self.dbs_per_pi = dbs_per_pi

global cluster_db
cluster_db = SQLiteClutster(pi_count,dbs_per_pi)

