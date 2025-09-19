# Directories allowed in a node directory

- child node directories
- z
- y


z directories contain implementation for that node.

y directories contain common code used by child nodes.

# node.py

The only other thing allowed in a node directory is node.py

# The golden rule

Nothing should be imported from a node except for from node.py

# Other notes

Each node is just a sub-process for the program, and the root node is the entire process.

# Other rule

The node should only contain a function or functions that can be called, or a class with a method
or methods that can be called. These are the sub-processes.