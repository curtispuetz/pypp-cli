# Notes about py++ (only the C++ won't work)
- If you define a function with an underscore at the start of its name, then it shouldn't be imported in other files,
and it shouldn't be used in the file it is in before its definition. This is because the transpiler does not put these
functions in the .h file. So, if its not in the .h file it can't be included in C++ elsewhere and also in C++ (unlike 
Python) you can't use a function before its definition. The purpose of the underscore feature is that it can be used to
potentially make the C++ build faster.
- Just like the above note, type aliases with an underscore work the same way.
- A note about numpy arrays. I thought that supporting numpy arrays in py++ was essential and I spent a lot of time 
trying to support them.
However, I don't think so anymore because the main reason people use numpy arrays in python instead of just a list or a
multidimensional list is for performance. But, if you are using py++ then you are totally fine to use that list because
you will get the performance from the executable generated from the C++ build. So, you might as well use lists instead 
of numpy arrays, and the only sacrifice is that your code will run slower with the Python interpreter. I don't think 
this is that important since you are already getting the C++ build.
- When you use the pypp_time_start() or pypp_time_per_counter_start() functions you need to specify the return type as 
auto (from pypp.custom_types import auto)