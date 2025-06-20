# Notes about py++ (only the C++ won't work)
- The type of enumerate([1, 2]) should be enumerate[list[int]], but python expects a enumerate[int].
Using enumerate[list[int]] is the way it must be done in pypp for the C++ code to compile.
- Similarly to above, the type of zip([1, 2], {3, 4}) should be zip[list[int], set[int]], but python 
expects zip[tuple[int, int]].