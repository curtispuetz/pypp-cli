# Things you can't do in py++ (only the C++ won't work)
#### Note: some things in here could be old, or could be removed from the list in the future. The list is also a WIP.
- overwrite built-in Python keywords
- use variables out of their scope
- let things have references to variables that have gone out of scope and deleted (this is like the hard one)
- define a variable without a Python type hint
- use variables differently from their type hints
- Name things with these names:
  - PyStr
  - etc.
- Use those class override method things
- Name a file in the root of the src dir:
  - py_str.py
  - pypp_util
- print something other than a string (for now)
- print with multiple args (i.e. print(a, b))
- You cannot do integer math and expect a float returned
- del my_list[i] (use my_list.pop(i) instead)
- Use multiline string literals as comments
- In Python you can assume a dict maintains insertion order, but in a the C++ build you can't
- dict.get() method does not have the second 'default value' argument
- Use the Python None. Instead you use PyppOpt (optional)
- Print an optional
- Make large tuples (use a list for large collections instead)
- Redefine variables
- Call methods or functions C++ reserved keywords (i.e. union, etc.)
  - Or maybe these can just be changed to 'keyword_' in the C++?
- <, <=, >=, > comparisons on sets.
- set values in a list via list slicing
- for loop else statements and type comments (what are for loop type comments?)
- name something 'pypp_hardcoded_it_tup'
- Iterate over a tuple (in pypp, tuples are just used as short data containers; lists, sets, or np arrays can be used 
for longer collections.)
- Use the pass keyword (use print('pass') instead perhaps)
- Use the caught exception as a name only with str() around it (i.e. for 'except Exception as e' e needs to be 
wrapped with str() if used)
- Reassign a reference (e.g. l: list[int] = [1, 2]; l = [];). This will not cause any errors, but will result in inconsistent behaviour between the Python and C++ execution.
- Use negative i for list.pop(i)
- Pass an empty list (or probably dict or set or any other collection?) somewhere. You need to first declare a variable so that you can specify the lists type (i.e. a: list[int] = []).
Additionally, you need to be careful when passing any collection inline, because C++ needs to be able to cast your collection
to the expected collection, which does work in most cases I think.
- Use 'global' and 'non local'
- Use curly braces inside f-string curly braces (e.g. f'{{a string}}, my dict: {{{0: 1}}}')
- Iterate over tuples
- Access range and slice attributes
- Use comparison operators for ranges and slices (i.e. slice(1) == slice(1))
- (tricky one) note that all returns in pypp are by value, so therefore you should avoid returning large objects except when that large object is constructed in the function/method, 
because in this case the C++ compiler optimizes it to not do a copy. This also means you shouldn't return some object and then modify that object and expect all references to that 
object to update. This one is so tricky! But I believe (not 100% sure yet) that as long as you don't program anything 'weird' you don't run into this issue. If you do something 
'weird' then you can run into this issue and there will be different behaviour between running with Python vs. C++. Note: I could easily solve this problem by adding
a Ref() wrapper so that I can specify
functions/methods to return a reference, and a pypp_ref() function to create a reference to a variable, but I won't right now, because I think it is not a pattern that a programming
language needs! Buy not adding these, users cannot use them, which I think is a good thing. I will see in the future if a use-case for it ever makes sense and then I would change my
mind. I don't think it makes sense because you never need a reference to an object in your current scope (just use the object you are trying to create a reference of) and you never
need to return a reference because you should instead inject that reference to where you need to by the normal means (i.e. passing as a function argument or constructor/setter 
injection)
- Create a dictionary inline and use its methods immediately (i.e. {0: 1}.keys())
- print a inline defined dictionary (i.e. print({0: 1}))