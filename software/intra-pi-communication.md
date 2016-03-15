The workload for the raspberry pis will be shared over an array of task lists stored on each pi. This will work the same way a master task list will work, the only difference is that each pi will be checking every other pi's task list to see if they have any work that needs to be done. 

The task list will be stored in SQLite. The reason for this is the exact reason why many suggest against using SQLite, single threaded writing of memory. When only one thing can be written to the database at a time, it limits the process and prevents data corruption from happening.
