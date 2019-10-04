Debugging is the process of _finding_ and _resolving_ problems in your code. As [Wikipedia](https://en.wikipedia.org/wiki/Debugging) puts it, debugging tactics:

> [...] can involve **interactive** debugging, control flow analysis, unit testing, integration testing, log file analysis, monitoring at the application or system level, memory dumps, and profiling.

In this exercise, we will focus on Interactive debugging & control flow analysis, the basics of debugging.

## The Python Debugger

One great thing about Python is that it comes with an included debugger, ready to use! The documentation has an [extensive article about the `pdb` module](https://docs.python.org/3/library/pdb.html) that you can should have a look to. We are going to use [`ipdb`](https://pypi.org/project/ipdb/), a variant of `pdb` which gives you a better developer experience with tab completion, syntax highlighting, etc.

Let's get to the bottom of it right away. In this exercise folder, you will find an `app.py` which contains a program. This program has a bug, let's use the Python debugger to find it!

```bash
python hello.py john lennon
```

What is the problem with the output of this program? Let's try to debug this problem! It seems there is a problem with the creation of the concatenated full name. Let's try to debug this. Insert the following line just after the `def full_name`:

```python
import ipdb; ipdb.set_trace()
```

Go back to the terminal and run the command again:

```bash
python hello.py john lennon
```

The program will **halt** at the line you inserted the `pdb.set_trace()`:

```bash
> [...]data-challenges/01-Python/01-Programming-Basics/04-Debugging/hello.py(9)full_name()
      8
----> 9     name = f"{first_name.capitalize()}{last_name.capitalize()}"
     10     return name

ipdb>
```

ℹ️ `ipdb` is not a module which is available by default in Python, so you need to `conda install ipdb` (something we did on Setup day). Alternatively, you can use the default `pdb` module embedded in Python:

```python
import pdb; pdb.set_trace()
```

It's time to play with the debugger. From there, you can do two things:

1. Control the flow of the program, telling the debugger to execute the next line, to step in a function or step out from it.
2. Have a look at the current memory, basically what is stored in variables at this moment. The program is halted so that you can have a closer look to its internals.

Type this:

```bash
ipdb> sys.argv
# => ['hello.py', 'john', 'lennon']
```

See how it works? You just asked the debugger to call the `sys.argv` and look what is stored in this array.

Our problem is that there is a missing space between `John` and `Lennon`. So we would like to have a look at the local variable `name`. Let's type:

```bash
ipdb> name
# => *** NameError: name 'name' is not defined
```

Why do we get this `NameError`? Where are we halted? To check at which line the program is halted, you can type:

```bash
ipdb> ll
# 4     def full_name(first_name, last_name):
# 5         import pdb; pdb.set_trace()
# 6  ->     name = f"{first_name.capitalize()}{last_name.capitalize()}"
# 7         return name
```

The program stopped **before** the line pointed by the little arrow `->`. This means that the `name` variable has **not yet been assigned**, thus we get the "`name` is not defined" error. OK, everything is clear now!

We are inside a function. Something useful is to display the argument list of the current function:

```bash
ipdb> args
# first_name = 'john'
# last_name = 'lennon'
```

What we can do now? We can ask the debugger to execute the next line with:

```bash
ipdb> next
```

Here you go, the debugger advanced by one line and executed it. You can see where the program is halted now with:

```bash
ipdb> ll
```

See how the little arrow `->` advanced? Now we can check what's inside the `name` variable:

```bash
ipdb> name
# => 'JohnLennon'
```

That's it! We have identified the culprit line! The interpolation is missing a space.

You can let the program runs until the next breakpoint (or the end of it) with:

```bash
ipdb> continue
```

Fix the `full_name` method in `hello.py`, and run the program again. Don't forget to remove the debugger line! That's something that easily forget and add to a commit. Some teams might want to add a [pre-commit hook](http://blog.keul.it/2013/11/no-more-pdbsettrace-committed-git-pre.html) to prevent this from happening.

## Going further

The previous section was about understanding the basic commands of the debugger. You can think of it as a DVD player with the following buttons:

- Pause (`pdb.set_trace()` in the source code)
- Next frame (`next`)
- Play (`continue`)

There are [many more debugger commands](https://docs.python.org/3/library/pdb.html#debugger-commands) like `step` or `return`.

## Solving this challenge

Now that you have learnt how to debug a faulty code, you can run the tests for this challenge:

```bash
./check.sh
```

You can see that the implementation we ask you is a tad more complicated. We want the `full_name` method to behavor correctly whitespace-wise when given an empty first name _or_ an empty last name.

 💡 **Tip**: have a look at the [`str.join(iterable)`](https://docs.python.org/3.7/library/stdtypes.html?highlight=join#str.join) method.