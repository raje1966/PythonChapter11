# Process: An instance of a program (e.g. python interpretor)
# + Takes advantage of multiple CPUs and cores.
# + Seperate memory space --> Memory is not shared between processes.
#+ Great for CPU-bound processing.
#+ New process is stated independently from other processes.
# + Processes are interruptable/killable.
# + One GIL for each process --> avoids GIL limitation.

# - Heavyweight.
# - Starting a process is slower than starting a thread.
# - More memory.
# - IPC (inter-process communication) is more complicated.