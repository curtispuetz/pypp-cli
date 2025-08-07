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
- built-in collections (lists, tuples, dict keys and value, sets) always own their data. This means that when you put 
data into one of these the data is always moved into the collection and not a reference or a copy. It means that when
you access an element of the collection that you either get a reference to the data or a copy of the data. To get a 
reference you would do a: Ref[MyElementType] = my_list[0].
- You can use 'list_reserve' to reserve space in a list. It does nothing for the Python interpreter, but for the C++
provides a potential performance boost just the std::vector.reserve() function does.
- Don't name anything in your class methods the same names as your class fields. Because it will break the C++.
- For inheritance, but super().__init__() as the first like of the child class for consistent C++ behavior.
- The behavior of constants and type aliases is a tiny bit nuanced if you are defining them not at the module level 
(i.e. inside
a function, class or other logic). I don't care about this because I only define these at the module level
anyway. But if you define these not at the module level, it will function as expected if you name it starting 
with an underscore. But if you don't name it starting with an underscore the constant or type alias is always extracted 
to the header file in the transpiled C++ (this is the little nuance).
- When setting a default dict variable you must specify it as auto.
- pypp_time must be imported exactly like this 'import pypp_python.stl.pypp_time as pypp_time'
