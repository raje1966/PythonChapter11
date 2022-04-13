Threads:  An entity within the process that can be scheduled (also known as lightweight process)
A process can spawn multiple threads.
+  All threads within a process share the same memory.
+  Starting a thread is faster than starting a process.
+ Great for I/O - bound tasks.

- Threading is limited by GIL: Only one thread at a time.
- No effect for  CPU-bound tasks.
- Not interruptable/killable.
- Careful with race conditions.