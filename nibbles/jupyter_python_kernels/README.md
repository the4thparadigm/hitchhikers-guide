# What is a Python Kernel and why does it matter?

If you have ever learned about or used Jupyter notebooks, you may have heard of something called a *kernel*. 
The toungue-in-cheek definition of a kernel is it's the thing you have to restart when you notebook freezes or otherwise stops behaving predictably.
Beyond this, many notebook users may not concern themselves with what a kernel is and may assume it's not that important. 
But kernels actually play a central role in how Jupyter operates (after all, a kernel is literally ["a central or essential part"](https://www.merriam-webster.com/dictionary/kernel) of something), and this directly impacts how data scientists use Jupyter.
Read on to find out more!

## The old way

Before there was Jupyter (or IPython, for that matter), there were basically just two ways that someone could use Python:
1. Run a python script. You write some code in a file, then call Python to run that file

```
~/my_project_folder$ python myscript.py
hello world
```

2. Use the interactive Python interpreter. You type commands one at a time into the interpreter, and the interpreter will run each command and print the output to the screen

```
~/my_project_folder$ python
Python 3.6.7 (default, Oct 22 2018, 11:32:17)
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 1+1
2
```

The second option uses something called a "read, evaluate, print loop" (REPL for short), so rather than deciding on all the code you want to run before running any of it, you can instead run one command at a time and observe the results before deciding what to run next

![python interpreter](python_interpreter.png)

This makes Python more *interactive*, which fits very nicely with the exploratory component of a data science project.
Here's the problem: this interactive interface is still limited to a terminal (or command line), so it's still quite limited.

Enter IPython and Project Jupyter.

## Project Jupyter

Project Jupyter (which started as IPython) attempts to create a richer, more interactive computing experience that enables easier collaboration and reproducability.
You can think of it as a step beyond the Python interpreter. 
This is accomplished by separating the REPL process into two distinct components, a *front end* and a *kernel*. 
The kernel handles the *read* and *execute* parts of REPL, and the front end handles the *print* component.
Along with these two components, there is a messaging protocol which enables the them to talk to each other.
This division of labor is powerful, because it separates a user's experience from the nuts and bolts of executing code.

![jupyter notebook](jupyter_notebook.png)

Perhaps the most popular use of this separation is the Jupyter Notebook.
Jupyter notebooks are an implementation of [literate programming](https://en.wikipedia.org/wiki/Literate_programming), where you can combine rich text (markdown) together with code and output.

## The Kernel

One advantage of having a separate kernel is that one can easily use the same familiar front end with a completely different kernel.
These Kernels don't even have to be in Python.
In fact, people have written Jupyter kernels for R, Julia, and Scala, just to name a few.
**Even within Python (and this is the critical piece), one can use many different kernels.**
to understand why, remember the components that go into a typical Python program

### Components of a Python program

Any Python program will consist of at least some user written code that will take advantage of Python's built in functions.
However, chances are high that they will also make use of one or more of the many packages developed by the Python community (see https://pypi.org/).
These packages aren't included with base Python, they have to be installed by the user.
Because of this, different Python users can use different combinations of Packages, and, *importantly*, this means two different users may run the same Python program and get different results.
This is why people share `requirements.txt` files and create virtual environments, in order to ensure that everyone can produce the same results when running the same program.

Now, what are the implications for Jupyter notebooks?
Essentially, for the Kernel to faithfully execute Python code, it must encompass not only base Python, but also the additional packages that were assumed to be present by the author of the program.
For example, if you write a program that uses Pandas version `0.23.0`, then assume that when a user runs my program, the statement `import pandas as pd` will import version `0.23.0`.

### Kernels for virtual environments

Virtual environments are a very popular way to create a self contained set of Python packages for a particular project that do not interfere with the packages used in a different projectd.
However, the default behavior of Jupyter is to use a Kernel that contains all packages installed for a user, but not any packages that are included in a particular virtual environment.
Thankfully, there is an easy way to create a kernel for a virtual environment and use that kernel for a Jupyter notebook.
For more detail, see [here](../../ds_projects/computer_set_up/README.md#using-jupyter-notebook-with-a-virtualenv)



## Conclusion

Hopefully you now have a better appreciation for the role that kernels play in Jupyter Notebooks, and why you should care about them.
Happy coding!




