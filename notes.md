# Notes about py++ (only the C++ won't work)
- If you define a type alias with an underscore at the start of its name, it shouldn't be imported in other files. 
If it is it will break the C++ build because the transpiler puts these types aliases in the .cpp file,
while it puts type aliases without an underscore at the start of its name in the .h file. The purpose of the underscore
feature is that it can be used to potentially make the C++ build faster.