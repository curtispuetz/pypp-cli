# Compy (a Python to C++ transpiler)
This project is a work-in-progress. Below you will find sections: The goal, The idea, How is this possible?, 
The inspiration, Why not cython, pypy, or Nuitka?, and What works today?

## The goal
The primary goal of this project is to make the end-product of your Python projects execute faster.
## The idea
The idea is to transpile your Python project into a C++ cmake project, which can be built
and executed much faster, as C/C++ is the fastest high-level language of today.

You will be able to run your code either with the Python interpreter, or by transpiling it to C++ and then 
building it with cmake. The steps will be something like this:
1. install compy
2. setup your project with cmd: `compy init`
3. install any dependencies you want with cmd: `compy install [name]` (e.g. compy install numpy)
4. run your code with the python interpreter with cmd: `python my_file.py`
5. transpile your code to C++ with cmd: `compy transpile` 
6. build the C++ code with cmake commands

Furthermore, the transpiling will work in a way such that you will easily be able to recognize your 
Python code if you 
look at the transpiled C++ code. What I mean by that is all your Python modules will have a
corresponding .h file and, if needed, a corresponding .cpp file in the same directory structure, and 
all names 
and structure of the Python code will be preserved in the C++. Effectively, the C++ transpiled 
code will be as close as possible to the Python code you write, but just in C++ rather 
than Python. 

Your project will consist of two folders in the root, one named python where the Python 
code you write will go, and one named cpp where the transpiled C++ code will go.

### But how is this possible?
You are probably thinking: how is this possible, since Python code does not always have a direct C++
equivalent?

The key to making it possible is that not all Python code will be compatible with compy. This means that
in order to use compy you will need to write your Python code in a certain way (but it will still all 
be valid Python code that can be run with the Python interpreter, which is unlike Cython where you 
can write code which is no longer valid Python).

Here are some of the bigger things you will need to do in your 
Python code (not a complete list; the complete list will come later):
- Include type annotations for all variables, function/method parameters, and function/method return types.
- Not use the Python None keyword, and instead use a compyOptional which you can import.
- Not use my_tup[0] to access tuple elements, and instead use tg(my_tup, 0) (where you import tg)
- You will need to be aware that in the transpiled C++ every object is passed as a reference or constant reference, so
you will need to write your Python so that references are kept to these objects because otherwise there will be a bug
in your transpiled C++ (this will be unintuitive to Python programmers and I think the biggest learning point or gotcha 
of compy. I hope most other adjustments will be simple and i'll try to make it so.)

Another trick I have employed so far, that is probably worthy of note here, is in order to translate something
like a python string or list to C++ I have implemented PyStr and PyList classes in C++ with identical 
as possible methods to the python string and list types, which will be used in the C++ transpiled code.
This makes transpiling Python to C++ for the types much easier.

## The Inspiration 
My primary inspiration for building this is to use it for the indie video game I am currently making.

For that game I am not using a game engine and instead writing my own engine (as people say) in OpenGL.
For writing video game code I found writing in Python with PyOpenGL to be much easier and faster for me 
than writing it in C++. I also got a long way with Python code for my game, but now I am at the point
where I want more speed.

So, I think this project could be useful for game engine or video game development! Especially if 
this project starts supporting openGL, vulkan, etc.

Another inspiration is that when I was doing physics/math calculations/simulations in Python in my years 
in university, it would have been very helpful to be able to transpile to C++ for those 
calculations that took multiple days running in Python.

## Why not cython, pypy, or Nuitka?
Why build compy when you can use something similar like cython, pypy, or Nuitka, etc. that speeds up your
python code? 

Because from research I have found that these programs, while they do improve speed, do not typically reach 
the C++ level of speed. compy should reach C++ level of speed because the executable built is literally from 
C++ code.

For cython, I mentioned briefly earlier, I don't like that some of the code you would write for it is 
no longer valid Python code. I think it would be useful to have two options to run your code 
(one compiled and one interpreted).

I think it will be useful to see the literal translation of your Python code to C++ code. On a personal
note, I am interested in how that mapping can work.

## What works currently?
- Most basic feature of the Python language, aside from some things that are more fancy and non-essential 
(e.g. nested list comprehensions).
  - functions
  - if-else statements
  - numbers/math
  - strings, lists, sets, dicts, defaultdict, and tuples
  - exception handling and raising exceptions
  - for and while loops
  - for loops with enuemrate, zip, or reversed
  - range and slice keywords
  - printing with the print() function
  - classes
  - @dataclass
  - @configclass (a custom compy decorator for constant variables in a class)
  - interfaces with ABC and @abstractmethod decorators
  - type variables
  - lambda functions
  - the yield and yield from keywords
  - isinstance() is effectively supported by using the compy Uni type where you specify all the possible types
and can then call an isinst() method.
- file-io (with the standard Python open() function)
- certain functions from the math and time libraries

For a complete picture of what works currently and how it works, take a look at 
the test_dir where there is a python directory and a cpp directory containing the C++ code 
transpiled from the python directory.

## What doesn't work currently?
- Match-case statements (just use if-else statements instead)
- Nested functions (i.e. functions inside functions)
- It would be hard to spell out everything here. In general, a lot of the things are rough around the edges 
(i.e. not all features are inlcuded or some features are accessed in a different way than usual Python), but the basic 
features of Python are.

For more details on what you can and cannot do look at things_cant_do.md. Note that this file is a WIP at the moment, 
and it could have wrong information in a few cases and it is very unorganized, but most of the information is there.