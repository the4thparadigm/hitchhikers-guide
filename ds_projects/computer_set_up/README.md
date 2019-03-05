# Computer Setup

Here are some initial steps for setting up your computer for a data science project.

## Windows: Getting a terminal environment

Max OS and Linux have build in terminal applications, but unfortunately Windows does not have this natively.
There are several options for Windows users:

* [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install-win10): Probably the closest thing to Linux on a Windows machine (without running a virtual environment). This provides a Bash shell and common \*nix tools, as well as access to a package management system for easy installation of software.
* [git-bash](https://gitforwindows.org/): A Bash emulator with useful Linux/Unix tools such as git, ssh, and find. Unfortunately, git-bash does not have a built in package manager.
* [Cygwin](https://www.cygwin.com/): This tool also provides a Bash terminal and common \*nix tools. 

Pick one of these (we recommend WSL with the latest version of Ubuntu) and install it, and you'll be well on your way to a terminal-like experience on your Windows machine.
The instructions below will routinely include terminal commands, so you'll have to complete this step before continuing. 

[Here is a quick guide to basic operations in the Bash terminal](https://medium.com/@grace.m.nolan/terminal-for-beginners-e492ba10902a)

## Package Manager

It will be much easier to install certain software through the use of a package manager.
Here are our recommendations:

* Mac: use [Brew](https://brew.sh/)
* Linux: If you have a Debian based distro (like Ubuntu), you probably already have [Apt](https://manpages.debian.org/stretch/apt/apt.8.en.html), and if you have a RedHat based distro (like CentOS) , you probably already have [Yum](http://yum.baseurl.org/). If you're using some other distro, you probably already know how to install software on your system.
* Windows: With WSL, you should have access to a package manager automatically (if you installed Ubuntu, it comes with Apt). With Cygwin, you can try [this](https://github.com/transcode-open/apt-cyg) (at present the author has not tried the Cygwin option, so you are on your own here).

## Python and pip

You should install the latest version of [Python 3](https://www.python.org/downloads/) and [pip](https://pypi.org/project/pip/), which is the package installer for python. 
All python packages and some other software (like Jupyter Notebook) will be installed with pip instead of the package manager.

### Apt
```
sudo apt-get update
sudo apt install python3
sudo apt install python3-pip
```

### Yum
```
sudo yum update
sudo yum install python3
sudo yum install python-pip
```

### Brew
In Brew, pip3 is installed automatically with Python 3.
```
brew update
brew install python3
```

### Check your installation
If you've successfully installed pip, the following command should print 
```
python3 --version
pip3 --version
```

## virtualenv

You will probably need 3rd party Python packages for your project.
These extend the functionality of Python to do things like fast linear algebra, machine learning, and interacting with a database.
In some cases, you will use different packages for different projects.
All is well until (gasp!) two projects use packages which conflict with each other. 
This happens more often than you might think, especially if you are using older packages which depend on older versions of other packages.

One remedy for this is to encapsulate the Python packages for a project in a "virtual environment" (virtualenv).
This is *like* having a separate python installation for each project, each using it's own set of packages, except that you don't have to install python multiple times. 
Instead, the same python executable is used for each virtualenv, but it is accessed through a shortcut in the directory that contains the virtualenv. 
This directory all holds Python packages installed in that virtualenv.

Install virtualenv with pip:
```
pip3 install virtualenv
```

If that doesn't work you may have to install with your package manager, for example:

#### In Apt

```
sudo apt install virtualenv
```

Test the installation with:
```
virtualenv --version
```

### Create a virtualenv

To create a virtualenv for your project, navigate to the project directory.
You can then create a virtualenv with
```
virtualenv venv
```
which makes a directory called venv that will contain the virtualenv.

### Activating a virtualenv

To run Python using the virtualenv you created, you need to "activate" it. 
This involves running a Bash script which modifies environment variables to include the virtualenv Python executable and packages
from your project directory, run:

```
source venv/bin/activate
```

Any packages you install with `pip install` while a virtualenv is activated will be installed only for that virtualenv. 
This helps compartmentalize packages within a virtualenv.
For more advanced computing environments, several people may be working the same server file system.
In this case, it can be useful for a virtualenv to also be stored on the server, so that all users can use and update the same set of Python packages.

### Deactivating a virtualenv

To stop using a virtualenv, simply deactivate by running `deactivate` from any location

## Jupyter Notebook

[Jupyter Notebook](https://jupyter.org/index.html) is an implementation of [Literate Programming](https://en.wikipedia.org/wiki/Literate_programming), an idea introduced by Donald Knuth. 
It's essentially a way to "Create and share documents that contain live code, equations, visualizations and narrative text."
It's a great tool for exploratory data analysis, not only because it allows you to quickly change and rerun code, but also because it allows you to easily annotate your code for someone else to follow along and reproduce your work.

install Jupyter Notebook using the following command

```
pip3 install jupyter
```

### Running Jupyter Notebook

Unlike a typical Python script, Jupyter Notebook is a server application that you access via a web browser.
From there, you can navigate through your file system, create and edit notebook files, and run Python code.
So to use Jupyter Notebook, you will start a local server with the command:
```
jupyter notebook
```
Make sure to do this from a terminal window that is a the root directory of your project, so you will be able to access all project files from this directory. 
Running the server also will cause the terminal window to "hang", unless you run it as a background process. 
We recommend not doing this anyways since Jupyter Notebook will print output to the terminal, making it not practical to also use that terminal for other purposes.

When you start Jupyter Notebook, it will print a URL (probably <http://localhost:8888>) that you can use to access the server.

If you want to run jupyter notebook and immediately open a specific notebook, you can run: 
```
jupyter notebook notebook.ipynb
```
More advanced users may want to specify the port like so:
```
jupyter notebook --port 9999
```

## Using Jupyter Notebook with a virtualenv

As we mentioned, virtualenvs allows you to isolate the Python projects you use for a particular project.
However, the default behavior of Jupyter Notebook is to run Python outside of any virtualenvs. 
So in order to use a virtualenv with Jupyter Notebook, a few steps must be taken:

First, activate the virtualenv you would like to use with Jupyter Notebook:
```
source venv/bin/activate
```
Then, install ipykernel if you haven't already:
```
pip3 install ipykernel
```
*Note: If this does not work, you may have to downgrade your version of tornado and try again:*
```
pip3 uninstall tornado
pip3 install tornado==4.5.3
```

Lastly, create a kernel that Jupyter Notebook can use.
It's probably best to change `projectname` to the name of your project, or something that you can easily identify from Jupyter Notebook
```
ipython kernel install --user --name=projectname
```
Now when you run Jupyter Notebook and have a notebook open, you can use the dropdown menu to change to the virtualenv kernel you just made:
Kernel > Change kernel > projectname




## Git & Github

Now you have some of the basic software installed, so you're ready to start writing some code.
But this is a team project, so how do we all write code for the same project that we all can use?
By utilizing [version control](https://en.wikipedia.org/wiki/Version_control). 
One of the most popular version control systems is [git](https://git-scm.com), which takes a little getting used to, but is very useful once you get the hang of it.
For some quick and dirty explanations of how git works, try [here](https://marklodato.github.io/visual-git-guide/index-en.html) or [here](https://agripongit.vincenttunru.com/).
Install Git from [here](https://git-scm.com/downloads).

Version control with Git works through the creation and updating of *repositories*, which are special folders that not only contain the current version of files, but also the full history of changes made to those files (and other things, like who made the changes).
Websites like <github.com> offer to host repositories for their users, so that their work can be easily shared with the general public.
Github also serves as a central repository where everyone working on a project can send their updates so others can view and use them.
Create a github account [here](https://github.com/join).

4th Paradigm projects are kept on the "the4thparadigm" github account, so you'll need access to that.
Contact a club officer to get access.

## Your Favorite IDE

Now we can actually start writing code, as long as you have your favorite text editor or integrated development environment (IDE) installed. 
There are many, many options of IDE, but for Python development, we've listed a few of the most popular 

* VSCode is a great option for editing Python. It is fast, lightweight, highly configurable, and has some convenient version control integration. It can be downloaded [here](https://code.visualstudio.com/). Make sure to install the Python extension through the VSCode application.

* [Pycharm](https://www.jetbrains.com/pycharm/) is another popular option, also with version control integration. Students can get the professional edition for [free](https://www.jetbrains.com/student/).

* For some more options and general information about IDEs, check out [this article](https://realpython.com/python-ides-code-editors-guide/#visual-studio-code).

Of course, you could always just stick with a basic text editor like [vim](https://www.vim.org/), [emacs](https://www.gnu.org/software/emacs/), or [nano](https://www.nano-editor.org/), all of which can be used directly from the terminal.
Each of these has it's own learning curve, but it's really handy to be able to quickly edit text files from the terminal, so it would be worth learning at least one of these.
In some instances, like when ssh'ing to a remote machine, it is much simpler to just use a terminal based text editor than mess with copying files back and forth, mounting a network drive, or using X11 forwarding to get GUI based editors.

# Conclusion

These steps should be a good start towards getting your computer ready to work on a data science project!
Every project is different, and they may have specific needs that were not covered here.
