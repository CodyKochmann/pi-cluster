# -*- coding: utf-8 -*-
# @Author: CodyKochmann
# @Date:   2016-03-21 16:41:46
# @Last Modified 2016-03-22
# @Last Modified time: 2016-03-22 01:14:45

from get_database_names import get_database_names
from get_next_database import get_next_database
from build_local_dbs import build_local_dbs

# ensure the databases are already generated
build_local_dbs()
