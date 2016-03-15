The workload for the raspberry pis will be shared over an array of task lists stored on each pi. This will work the same way a master task list will work, the only difference is that each pi will be checking every other pi's task list to see if they have any work that needs to be done. 

The task list will be stored in SQLite. The reason for this is the exact reason why many suggest against using SQLite, single threaded writing of memory. When only one thing can be written to the database at a time, it limits the process and prevents data corruption from happening.

The jobs will be prioritized based on a cross of the date that the job was created and which pi has the largest list of tasks to complete. While one thread will be handling communication and one thread will be eliminating jobs, a pi is to only solve its own jobs if it's jobs are the next in line in the clusters workload.
