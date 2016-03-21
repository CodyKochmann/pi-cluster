# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-21 14:15:22
# @Last Modified by:   CodyKochmann
# @Last Modified time: 2016-03-21 14:18:04

# this is the primary control for the database 
# that will be used in the raspberry pi cluster

# since sqlite is limited to 2GB in the raspberry
# pi due to it being 32-bit, the database will be
# designed off of a cluster of multiple sqlite 
# instances.

# each pi will have 4 databases that it will own
# along with a backup of each database on its 
# siblings in order to promise maximum redundancy


