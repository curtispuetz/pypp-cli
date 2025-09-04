# Py++ (Compiled Python) - (Transpiles to C++) - Release v1.0.0 coming soon
This project's first version will be released soon (likely within a week from today, which is Sept. 2nd). You will not find any usage instructions yet. Check back later.

Upon Release, Py++ will be a Python framework for writing Python projects which can be transpiled into C++ (CMake) projects. 

Below you will find sections: 
- The goal
- Is the goal realized?
- Brief introduction to the Py++ CLI
- Brief introduction to writing code for a Py++ project and how the transpilation works (Including examples)
- Other details (Py++ project structure and running with the Python interpreter)
- Py++ libraries (contribute to Py++ with your own libraries)
- List of other details about writing Py++ code
- The bad (about Py++)
- The good (about Py++)
- My contact information

## The goal
The primary goal of this project is to provide C++ level performance with a Python syntax for software projects.

## Is the goal realized?

To a large degree, yes, it is. I've done a decent amount of benchmarking 
and found that the Py++ code I wrote is performing in 
no detectable difference (of greater than 2%) compared to the identical C++ code I would write.

This is an expected result because when you use Py++ you are effectively
writing C++ code, but with a Python syntax. In the code you write, you
have to make sure that types are defined for everything, that no variables 
go out of scope, and that there are no dangling references, etc.,
just like you would in C++. The code is valid Python code, which can be run with the Python
interpreter, but can also be transpiled to C++ and then built into an executable program.

Not all C++ features are supported, but enough that I care about are supported (or will be in future Py++ versions), so that I am content to use Py++ instead of C++.

In the rest of this document, I will give a brief idea about how to use Py++ and how Py++ works, as an introduction. Then, before the v1.0.0 release, I will have complete documentation on a website that explains every detail possible so you can work with Py++ with a solid reference.

## Brief introduction to the Py++ CLI
The Py++ CLI can be installed with pip and allows you to transpile your Python project and build and run the generated C++ CMake project with simple commands.


You can initialize your Py++ project in your current directory with:

`pypp init`

After you have written some Python, you can transpile your project to C++ with:

`pypp do transpile format`

Then, you can build your C++ code with:

`pypp do build`

Then, you can run your generated executable manually, or you can use pypp to run it with (the executable is called 'main' in this example):

`pypp do run -e main`

Or instead of doing the above 3 commands separately, you can do all these steps at once with:

`pypp do transpile format build run -e main`

## Brief introduction to writing code for a Py++ project and how the transpilation works

The Py++ transpiler will generate C++ .h and .cpp files for each single Python module you write. So, you don't have to worry about the two different file types. 

Let's look at some examples.

### Examples

#### 1) Basic function

If you write the following code in a Python module of your project:

```python
# example_1.py
def my_function(a: list[int], b: list[int], c: int) -> list[int]:
    ret: list[int] = [c, 2, 3]
    assert len(a) == len(b), "List lengths should be equal"
    for i in range(len(a)):
        ret.append(a[i] + b[i])
    return ret
```

This will transpile to C++ .h and .cpp files:

```cpp
// exmaple_1.h
#pragma once

#include "py_list.h"

PyList<int> my_function(PyList<int> &a, PyList<int> &b);
```

```cpp
// example_1.cpp
#include "example_1.h"
#include "pypp_assert.h"
#include "py_str.h"

PyList<int> my_function(PyList<int> &a, PyList<int> &b, int c) {
    PyList<int> ret = PyList({c, 2, 3});
    assert(a.len() == b.len(), PyStr("List lengths should be equal"));
    for (int i = 0; i < a.len(); i += 1) {
        ret.append(a[i] + b[i]);
    }
    return ret;
}
```
You will notice that we use type hints everywhere in the Python code. As mentioned already, this is required for Py++.
You will also notice that a Python list type is transpiled to the PyList type. The PyList type is a thin wrapper around 
the C++ std::vector, so the performance is effectively equivalent to std::vector.
(for Python dicts and sets, there are similar PyDict and PySet types, which thinly wrap std::unordered_map and std::unordered_set).

You'll also notice that there is an assert function included in the C++ file, and that a Python string transpiles to a PyStr type.

#### 2) Pass-by-value
Let's do another example with some more advanced features. You may have noticed that in the last example, the PyList function parameters were
pass-by-reference (i.e. the & symbol). This is the default in Py++ for types that are not primitives (i.e. int, float, etc., which are always pass-by-value). 
This is how you tell the Py++ transpiler to pass-by-value for a non-primitive type:

```python
# example_2.py
from pypp_python import Valu

def my_function(a: Valu(list[int]), b: Valu(list[int])) -> list[int]: ...
```
And the generated C++ will be using pass-by-value:
```cpp
// example_2.h
#pragma once

#include "py_list.h"

PyList<int> my_function(PyList<int> a, PyList<int> b);
```

Py++ also provides a function that transpiles to std::move (`from pypp_python import mov`). This can be used when calling the function.

#### 3) Variable out of scope
Since in C++, when a variable goes out of scope, you can no longer use it, in Py++ it is the same. Let's show an example of that. This is valid Python code, but it is not compatible with Py++:

```python
# example_3a.py
def var_out_of_scope(condition: bool) -> int:
    if condition:
        m: int = 42
    else:
        m: int = 100
    return 10 * m
```

Instead, you should write the following, so you are not using an out-of-scope variable:
```python
# example_3.py
def var_not_out_of_scope(condition: bool) -> int:
    m: int
    if condition:
        m = 42
    else:
        m = 100
    return 10 * m
```
And this will be transpiled to C++ .h and .cpp files:

```cpp
// example_3.h
#pragma once

int var_not_out_of_scope(bool condition);
```

```cpp
// example_3.cpp
#include "example_3.h"

int var_not_out_of_scope(bool condition) {
    int m;
    if (condition) {
        m = 42;
    } else {
        m = 100;
    }
    return 10 * m;
}
```

#### 4) Classes
In Py++, you can define classes.

```python
# example_4.py
class Greeter:
    def __init__(self, name: str, prefix: str):
        self.name = name
        self.prefix = prefix

    def greet(self) -> str:
        return f"Hello, {self.prefix} {self.name}!"
```
This will be transpiled to C++ .h and .cpp files:

```cpp
// example_4.h
#pragma once

#include "py_str.h"

class Greeter {
  public:
    PyStr &name;
    PyStr &prefix;
    Greeter(PyStr &a_name, PyStr &a_prefix) : name(a_name), prefix(a_prefix) {}
    PyStr greet();
};
```

```cpp
// example_4.cpp
#include "example_4.h"

PyStr Greeter::greet() {
    return PyStr(std::format("Hello, {} {}!", prefix, name));
}
```

Something very worthy of note for classes in Py++ is that the \_\_init\_\_ constructor 
method body cannot have any logic! It must only define the variables in the same
order that they came in the parameter list, as done in the Greeter example
above (you don't need type hints either). Py++ was designed this way for simplicity, and if users want to customize
how objects are built with custom logic, they can use factory functions. This
choice shouldn't limit any possibilities for Py++ projects; it just forces you to 
put that type of logic in factory functions rather than the constructor.

#### 5) dataclasses
In Py++ you can define dataclasses (with the frozen and slots options if you want).

```python
# example_5.py
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Greeter:
    name: str
    prefix: str

    def greet(self) -> str:
        return f"Hello, {self.prefix} {self.name}!"
```

This will be transpiled to C++ .h and .cpp files:

```cpp
// example_5.h
#pragma once

#include "py_str.h"

struct Greeter {
    const PyStr &name;
    const PyStr &prefix;
    Greeter(PyStr &a_name, PyStr &a_prefix) : name(a_name), prefix(a_prefix) {}
    PyStr greet();
};
```

```cpp
// example_5.cpp
#include "example_5.h"

PyStr Greeter::greet() {
    return PyStr(std::format("Hello, {} {}!", prefix, name));
}

```

If the frozen=True was omitted, then the consts in the generated C++ struct go away.

#### 6) Unions and Optionals
Unions and optionals are supported in Py++. So if you are used to using
Python's isinstance() function to check the type of an object, you can still
do something much like that with Py++s 'Uni' type. Note that in the following example, 'ug' stands for 'union get':

```python
# example_6.py
from pypp_python import Uni, ug, isinst, is_none


def union_example():
    int_float_or_list: Uni[int, float, list[int]] = Uni(3.14)
    if isinst(int_float_or_list, float):
        val: float = ug(int_float_or_list, float)
        print(val)
    # Union with None (like an Optional)
    b: Uni[int, None] = Uni(None)
    if is_none(b):
        print("b is None")
```

This will be transpiled to C++ .h and .cpp files:

```cpp
// example_6.h
#pragma once

void union_example();
```

```cpp
// example_6.cpp
#include "example_6.h"
#include "pypp_union.h"
#include "pypp_util/print.h"
#include "py_list.h"
#include "py_str.h"

void union_example() {
    Uni<int, double, PyList<int>> int_float_or_list(3.14);
    if (int_float_or_list.isinst<double>()) {
        double val = int_float_or_list.ug<double>();
        print(val);
    }
    Uni<int, std::monostate> b(std::monostate{});
    if (b.is_none()) {
        print(PyStr("b is None"));
    }
}

```

You cannot typically use None in Py++ code (i.e. something like `var is None`). Instead,
you use the union type as shown in this example with the is_none function.


## Other details
### Py++ project structure
When you initialize a Py++ project with the `pypp init` command, 4 folders are created:
```
/pypp_data
/cpp
/python
/resources
```
In the python directory, a virtual environment is created as well with the 
[pypp_python](https://pypi.org/project/pypp-python/) dependency installed. 
You write your project code inside the python directory. When you transpile your project, .h and .cpp files are 
generated and written to the cpp directory. The cpp directory also has some sub-directories, 'pypp' and 'libs'
(that may only show up after your first transpile). The 'pypp' directory contains the necessary C++ code for Py++
projects (like PyList, PyDict, and PySet, Uni, etc., mentioned above), and the 'libs' directory contains C++ code from any
installed libraries (which I will talk about in the next section).

When you write your project code in the python directory, every Python file at the root level must contain a main block.
This is because these files will be transpiled to main C++ files. So, for each Python file you have at the root level, you
will have an executable for it after transpiling and building. All other Python files you write must go in a python/src 
directory.

The pypp_data directory contains project metadata, and the resources directory is meant for storing files that your
program will load.

### Running your Py++ project with the Python interpreter

So far, I have talked about transpiling your code to C++, building, and 
running the executable. But nothing is stopping you from running your code with the Python interpreter, since the code you write is valid Python code. 

The program should run equivalently both ways (by running the executable or by running with the Python interpreter), so long as there are no bugs
in your code and you use the Py++ framework as intended.

You can run with the Python interpreter with the command:

`pypp run_python main.py`


## Py++ libraries (contribute to Py++ with your own libraries)

You can create Py++-compatible libraries and upload them to PyPI to contribute to the Py++ ecosystem 
(when a library is uploaded to PyPI, it can now be installed with pip by anyone). I have published one Py++ library so far, for GLFW (A library for opening windows) ([PyPI link](https://pypi.org/project/pypp-bridge-lib-glfw/))

People creating Py++ libraries will be necessary to make Py++ as enjoyable to use as a typical 
programming language like Python, C++, Java, C#, or anything else. This is because I likely don't have 
the time to make every type of library that a good programming language needs (i.e. like a JSON loading 
library, etc.) on my own.

To contribute to the Py++ project, instead of making changes to the Py++ source code and creating pull requests,
it's likely much better to contribute by creating a Py++ library instead. You are free to do that without anyone
reviewing your work!

You can add functionality to Py++ pretty much just as well as I can by creating libraries. In fact, the way I intend to add additional functionality
to Py++ now is by creating libraries. The Py++ transpiler source code is generally fixed at this point, besides the maintenance we will have to do and any 
additional features.
Instead of modifying the source code, 
the way to add more functionality is by creating libraries. If you create a
library that I think should be in the Py++ standard library, one of us can copy your code and add it to the source code as a standard library.

There are two types of Py++ libraries: pure-libraries, and bridge-libraries.

### Pure-libraries
Pure-libraries are libraries that are written with the Py++ framework. This is the easier of the two library types, but still very powerful.
You just write your Py++ code, transpile it to C++ (the generated C++ goes in a special folder), and then you can upload
your library to PyPI so anyone can install it to their Py++ project with pip.

To set up a pure-library, you run:

`pypp init_pure_lib`

This will create the PyPI project structure for you with a pyproject.toml file, create your virtual environment, and install a few required libraries in the virtual environment.

To transpile your pure-library you run:

`pypp do_pure_lib transpile format`

Before uploading your library to PyPI make sure you transpile your code, because the transpiled C++ code will be uploaded along with your Python code.

A pure library is set up to be built with hatching (you can change that if you want):

`python -m hatchling build`

### Bridge-libraries
Bridge-libraries will require some skill and understanding to compose, and are very necessary to build in order to get more functionality working in Py++.
After the v1.0.0 release of Py++ I plan to start making many bridge-libraries that I will need for my projects that I intend to use Py++ for (like a game engine).

In a bridge-library, what you will typically do is write Python code, C++ code, and JSON files. The Python code will be used by Py++ when running with 
the Python interpreter, the C++ code will be used by Py++ when the CMake project is being built, and the JSON files will tell Py++ how to transpile 
certain things. If that sounded confusing, let's look at a quick example.

Let's say that you want to provide support for the Python 'time' standard library (or something effectively equivalent to it) within Py++. You can create a bridge-library (let's call it "my_bridge_library" for the example) and add this Python code to it:

```python
# __init__.py
import time


def start() -> float:
    return time.time()


def end(start_time: float) -> float:
    return time.time() - start_time
```

and add this C++ code:

```cpp
// my_bridge_lib.h
#pragma once
#include <chrono>
#include <thread>

namespace pypp_time {
inline std::chrono::system_clock::time_point start() {
    return std::chrono::system_clock::now();
}

inline double end(std::chrono::system_clock::time_point start_time) {
    return std::chrono::duration_cast<std::chrono::duration<double>>(
               std::chrono::system_clock::now() - start_time)
        .count();
}
}
```

And add this JSON file that should be named call_map.json:

```json
// call_map.json
{
  "replace_dot_with_double_colon": {
    "pypp_time.": {
      "cpp_includes": {
        "quote_include": "my_bridge_lib.h"
      },
      "required_py_import": {
        "module": "my_bridge_lib",
        "name": "pypp_time"
      }
    }
  }
}
```

The idea here is that when you install this bridge-library to your Py++ project, you will be able to write this and it should work:

```python
# test_file.py
from my_bridge_lib import pypp_time
import auto from pypp_python
from foo.bar import some_process

def pseudo_fn():
    start_time: auto = pypp_time.start()
    some_process()
    print("elapsed time:", pypp_time.end(start_time))
```
That will work because it will be transpiled to the following C++:
```cpp
// test_file.cpp
#include "test_file.h"
#include "my_bridge_lib.h"
#include "pypp_util/print.h"
#include "foo/bar.h"

void pseudo_fn() {
    auto start_time = pypp_time::start();
    some_process();
    print(PyStr(std::format("elapsed time: {}", pypp_time::end(start_time))));
}
```

The JSON file you wrote told
the Py++ transpiler that when it sees a [call statement](https://docs.python.org/3/library/ast.html#ast.Call) in the Python code 
that starts with "pypp_time.", it should replace all dots in the caller string with double colons. It also told the Py++ transpiler
that when it sees such a call statement, it should add the C++ include for "my_bridge_lib.h" at the top of the file. From the C++ snippet above, you can see
that that is what the Py++ transpiler did in this case.

Another feature for creating bridge libraries is when you are specifying how the Py++ transpiler should behave in the JSON files, you
can provide custom Python functions that are used. This allows you to configure the Py++ transpiler to do anything. I have one Py++ bridge-library where you can see this in action. It is a [bridge-library for GLFW](https://github.com/curtispuetz/pypp-bridge-lib-glfw) that I mentioned earlier. You can see in this libraries [call_map.json](https://github.com/curtispuetz/pypp-bridge-lib-glfw/blob/master/pypp_bridge_lib_glfw/pypp_data/bridge_jsons/call_map.json) that there is a mapping function. The mapping function is executed if the call starts with "glfw.". The mapping function returns what the call string should be transpiled to. In this particular mapping function, it basically changes the call from snake_case to camelCase. This works for my GLFW bridge-library because every call to GLFW in the GLFW Python library is like `glfw.function_name(args...)` and 
in the C++ library is like `glfwFunctionName(args...)`. So, when you transpile the Python to C++, you want to change it from snake_case to camelCase and remove the dot, and this is what my mapping function does. There might be a few functions that my GLFW bridge-library does not work for, and when I find them
I will likely fix the issue by adding custom cases to the mapping function or maybe a combination of other things.

To set up a bridge-library, you run:

`pypp init_bridge_lib`

And again, a bridge library is set up to be built with hatching (you can change that if you want):

`python -m hatchling build`

## List of other details about writing Py++ code
- Tuples are transpiled to a PyTup type, and I think they are likely not performant with a large number of elements. In Py++ tuples are meant to only store a small number of elements.
- The yield and yield from Python keywords work in Py++. They transpile to the C++ [co_yield](https://en.cppreference.com/w/cpp/keyword/co_yield.html) and a custom macro.
- Almost all list, dict, and set methods work in Py++ with a few exceptions.
- A big thing about accessing tuple elements and dict elements is you have to use special functions that I've called 'tg' and 'dg' (standing for tuple get and dict get). It is, unfortunately, a little inconvenient, but something that I couldn't get a workaround for. It's really only resulting in a couple of extra characters for when you want to access tuple and dict elements.
- Quite a few string methods are supported, but quite a few are not. I will add more string methods in future Py++ releases. It's just a matter of having the time to add them.
- In Python, you can assume a dict maintains insertion order, but with Py++ you cannot.
- There is no way to tell the Py++ transpiler that a variable should be 'const' (i.e. the C++ const keyword). I don't think that is needed because I think the Py++ developer can manage without it, just like Python developers do.
- functions within functions are not supported
- Inheritance is supported
- 'global' and 'non local' are not supported
- enumerate, zip, and reversed are supported
- list, set, and dict comprehensions are supported.

All other details I will provide when I write the docs.

## The bad (about Py++)
Py++ will be rough around the edges. There will probably be lots of bugs at the beginning. Stability will only improve with time.

Features that are missing:
- Templates (i.e. writing generic code allowing functions to operate with various types without being rewritten for each specific type).
   - I will add templates in a future version. It is a high priority.
- All sorts of libraries that you would expect in a good programming language (i.e. multi-threading/processing, JSON, high-quality file-interaction, os interactions, unittesting, etc.)
   - Can be improved through library development.

I can't think of any other missing features at the moment, but I am sure that many will come up. 

Some features are excluded from Py++ on purpose because I don't think they are needed to write the Py++ code that I want to write. A big example of this is pointers. I don't see a reason to support them generically. But, if someone really wanted, they could probably create a bridge-library to support them generically. The reason I say "generically" is because I support a specific type of pointer in my GLFW bridge library ([reference](https://github.com/curtispuetz/pypp-bridge-lib-glfw/blob/master/pypp_bridge_lib_glfw/pypp_data/bridge_jsons/name_map.json)).

Py++ likely won't be useful for web development for a while.

## The good (about Py++)

- You can write code that performs as well as C++ (the #1 most performant high-level language) with a Python syntax.
    - (If you find something in Py++ that does not perform as well as something you could write in C++, please contact me with the details. I really want to identify these situations. My contact information is at the bottom.)
- I like that you can run the code in 2 ways: either quickly with the Python interpreter, or more slowly by transpiling and building first. It can sometimes be convenient to use the Python interpreter.
- You can create a prototype for your project in normal Python, and then later migrate the project to Py++. This is much easier than creating a prototype in Python and then migrating it to C++ (which is a common thing today for any project where you need high performance).
- The transpiler is very fast. Its execution time seems negligible compared to the CMake build time, so it is not the bottleneck.
- It will be useful for game engine development after bridge-libraries are made for OpenGL, Vulkan, GLM, and other common game engine libraries. This is actually the reason I started building Py++ (because I am making a game engine). Everyone uses C++ for game engines, and with Py++ you will be able to write C++ with a much easier syntax for game engines.
- It will be useful for engineering, physics, and other science simulations that require a long time to execute.
- It will maybe be useful for other applications. Perhaps data science, where people are doing some manual work on their data. In short, in the long run (after there is a larger ecosystem), it should be useful for almost anything that C++ is useful for.
- Py++ is extensible with pure-libraries and bridge-libraries.
- Py++ will be open source and free forever

## My contact information

Please feel free to contact me for any reason. I have listed ways you can contact me below.

If you find bugs or are thinking about creating a Py++ library, I'd encourage you to contact me and share 
with me what you are doing or want to do. Especially if you publish a Py++ library, I'd encourage you to let me know about it.

For bugs, you can also open an Issue on the [Py++ GitHub](https://github.com/curtispuetz/pypp-cli).

Ways to reach me:
- DM me on [my reddit](https://www.reddit.com/user/joeblow2322/).
- Email me at pypp.main@gmail.com
- tweet at me or DM me on X.com. To either my [Py++ account](https://x.com/CompiledPy) or my [personal account](https://x.com/curtispuetz) (your choice).

## Other Py++ repositories
- For C++ development: https://github.com/curtispuetz/pypp-cpp-dev
- pypp-python: https://github.com/curtispuetz/pypp-python
- GLFW bridge-library: https://github.com/curtispuetz/pypp-bridge-lib-glfw
