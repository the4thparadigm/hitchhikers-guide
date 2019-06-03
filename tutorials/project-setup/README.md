# Project Setup
Your kitchen is clean and you're ready to start cooking, so let's go over how to setup a data science project.

## Machine setup
If you haven't already, complete all the instructions on the [machine setup page](../machine-setup/README.md).

## Directory structure
An organized directory structure is key to an effective project.

Here is an example structure. You may only need some of the components included in this structure, but it is a good template.
```
my-project/
|-- venv/
|-- repo/
    |-- .gitignore
    |-- README.md
    |-- LICENSE
    |-- requirements.txt
    |-- __init__.py
    |-- cfg/
    |   |-- config.yml
    |-- data/
    |   |-- raw/
    |   |-- Processed
    |-- notebooks/
    |-- src/
    |   |-- features/
    |   |-- models/
    |   |-- utils/
    |   |-- visualizations/
    |-- test/
    |   |-- features/
    |   |-- models/
    |   |-- utils/
    |   |-- visualizations/
    |-- output/
    |   |-- figures/
    |   |-- logs/
```

We'll discuss each directory below.

* `my_project`: This is the root directory for the project. You can make the name appropriate for the data science project.

* `venv`: This directory contains the virtualenv for this project. Actually, you shouldn't manually create this directory. Instead, in the project root, run `virtualenv venv` to create the virtualenv

* `repo`: Everything (well, mostly everything) in this directory is part of the git repository. When you create this folder, you can navigate inside it and run `git init` to create a new git repository. Among the files in this folder is requirements.txt, which contains all python packages used in this project. This folder might have the same name as the folder containing it, so it will look like `my-project/my-project`.

* `cfg`: This directory contains all configuration files used for the project. Config files specify things like project directories, login credentials, and modeling parameters

* `data`: All data used in the project lives here. The raw, unmodified data should go in `raw`, and any processed, cleaned, or filtered data should go in `processed`

* `notebooks`: This is where any jupyter notebooks should go

* `src`: Any python code that is not a jupyter notebook should go here. Any code for generating, loading, cleaning, or processing features should be in `features`. Any code that has to do with defining, training, testing, loading, or saving models should go in `models`. Any additional code with no where else to live should go in `utils`, for example, code that interacts with a database or web API. Lastly, `visualizations` contains any code used for generating visualizations. In many cases, it is useful to have an `__init__.py` in every folder in either `src` or `test` - this helps manage importing modules.

* `test`: This directory mirrors the directory structure of `src`, and contains any code written to test the performance of the code in `test`.

* `output`: This directory is a place to put any visualizations, models, or other output produced for the project
* The `__init__.py` files tell Python that this is a python package, so that modules you write can be imported conveniently.

### Environment Variables
In our project we'll want to import Python modules by using paths relative to the source code directory, so let's add the project directory to the PYTHONPATH enironment variable.
To set an environment variable in bash, simply add an export statement to your `.bashrc` file that points to the project root:

`export PYTHONPATH=$PYTHONPATH:/path/to/my_project/`

where you replace `/path/to/my_project` with the path to the root directory of your project.

We want to use a configuration file for our project, so let's set an environment variable that points to that file. Again, add the following to your `.bashrc`:

`export MYPROJECTROOT="/path/to/git_repo/"`

where you replace `/path/to/git_repo/` with the path to the git repository directory.

Note: If you are running multiple projects, it may make sense to change `MYPROJECTROOT` to some name that reflects your project, like `DENVERCRIMEROOT`

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
