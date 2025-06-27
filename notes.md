# Notes about py++ (only the C++ won't work)
- If you define a type alias with an underscore at the start of its name, it shouldn't be imported in other files. 
If it is it will break the C++ build because the transpiler puts these types aliases in the .cpp file,
while it puts type aliases without an underscore at the start of its name in the .h file. The purpose of the underscore
feature is that it can be used to potentially make the C++ build faster.
- I thought that supporting numpy arrays in py++ was essential and I spent a lot of time trying to support them.
However, I don't think so anymore because the main reason people use numpy arrays in python instead of just a list or a
multidimensional list is for performance. But, if you are using py++ then you are totally fine to use that list because
you will get the performance from the executable generated from the C++ build. So, you might as well use lists instead 
of numpy arrays, and the only sacrifice is that your code will run slower with the Python interpreter. I don't think this
is that important since you are already getting the C++ build.
- When you use the pypp_time_start() or pypp_time_per_counter_start() functions you need to specify the return type as auto
(from pypp.custom_types import auto)