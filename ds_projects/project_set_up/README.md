# Project Set Up

So, you've decided to start a data science project. Great! Now what...?

## Software Setup

### Windows: Getting a terminal environment

Max OS and Linux have build in terminal applications, but unfortunately Windows does not have thie natively.
There are several options for Windows users:

* [Windows Subsystem for Linux (WSL)](https://docs.microsoft.com/en-us/windows/wsl/install-win10): Probably the closest thing to Linux on a Windows machine (without running a virtual environment). This provides a Bash shell and common \*nix tools, as well as access to a package management system for easy installation of software.
* [git-bash](https://gitforwindows.org/): A Bash emulator useful Linux/Unix tools such as git, ssh, and find. Unfortunately, git-bash does not have a built in package manager.
* [Cygwin](https://www.cygwin.com/): This tool also provides a Bash terminal and common \*nix tools. 

Pick one of these (we recommend WSL) and install it, and you'll be well on your way to a terminal-like experience on your Windows machine.
The instructions below will routinely include terminal commands, so you'll have to complete this step before continuing. 

### Package Manager

It will be much easier to install certain software through the use of a package manager.
Here are our recommendations:

* Mac: use [Brew](https://brew.sh/)
* Linux: If you have a Debian based distro (like Ubuntu), you probably already have [Apt](), and if you have a RedHat based distro (like CentOS) , you probably already have [Yum](http://yum.baseurl.org/). If you're using some other distro, you probably already know how to install software on your system.
* Windows: With WSL, you should have access to a package manager automatically. With Cygwin, you can try [this](https://github.com/transcode-open/apt-cyg) (at present the author has not tried this, so you are on your own here).

### Python and pip

You should install the latest version of [Python 3](https://www.python.org/downloads/). 

#### Apt
```
sudo apt-get update
sudo apt install python3
sudo apt install python3-pip
```

#### Yum
```
sudo yum update
sudo yum install python3
sudo yum install python-pip
```

#### Brew
In Brew, pip3 is installed automatically with Python 3.
```
brew update
brew install python3
```

#### Check your installation
If you've successfully installed pip, the following command should print 
```
python3 --version
pip3 --version
```

### virtualenv

You will probably need 3rd party Python packages for your project.
In some cases, you will use different packages for each project. 
All is well until (gasp!) two projects use packages which conflict with each other. 
This happens more often than you might think, especially if you are using older packages which depend on older versions of other packages.

One remedy for this is to encapsulate the Python packages for a project in a virtualenv.
This is *like* having a separate python installation for each project, each using it's own set of packages.

install virtualenv with pip:
```
pip3 install virtualenv
```
Test the installation with:
```
virtualenv --version
```

#### Create a virtualenv

To create a virtualenv for your project, navigate to the project directory.
You can then create a virtualenv with
```
virtualenv venv
```
which makes a directory called venv that will contain the virtualenv.

#### Activating a virtualenv

To run Python using the virtualenv, you need to "activate" it, like so:

```
source venv/bin/activate
```

Any packages you install with `pip install` while a virtualenv is activated will be installed only for that virtualenv.

#### Deactivating a virtualenv

To stop using a virtualenv, simply deactivate it with:
```
deactivate
```

### Jupyter Notebook

[Jupyter Notebook](https://jupyter.org/index.html) is an implementation of [Literate Programming](https://en.wikipedia.org/wiki/Literate_programming), an idea introduced by Donald Knuth. 
It's essentially a way to "Create and share documents that contain live code, equations, visualizations and narrative text."
It's a great tool for exploratory data analysis, not only because it allows you to quickly change and rerun code, but also because it allows you to easily annotate your code for someone else to follow along and reproduce your work.

install Notebook using the following command

```
pip3 install jupyter
```

#### Running Jupyter Notebook

To use Jupyter Notebook, you will start a local server with the command:
```
jupyter notebook
```
You can then navigate using a web browser to [http://localhost:8888](http://localhost:8888).

You can open a specific notebook with 
```
jupyter notebook notebook.ipynb
```
and use a custom port with 
```
jupyter notebook --port 9999
```


### Git & Github

### Your Favorite IDE


## Computer Environment

### Environment Variables

In our project we'll want to import Python modules by using paths relative to the source code directory, so let's add our source code to the PYTHONPATH enironment variable.

We want to use a configuration file for our project, so let's set an environment variable that points to that file.



