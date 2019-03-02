# Project Set Up

So, you've decided to start a data science project. Great! Now what...?

## Computer Set Up

If you haven't already, check out the [Computer Setup Page](../computer_set_up/README.md) for instructions on installing the necessary software.

## Directory Set Up

An organized directory structure is key to an effective data science project.
Here is one structure you can use:

```
my_project
|
|-- venv
|
|-- git_repo
    |    .gitignore
    |    README.md
    |    LICENSE
    |    requirements.txt
    |    __init__.py
    |
    |-- config
    |       config.yml
    |
    |-- data
    |   |
    |   |-- raw
    |   |
    |   |-- Processed
    |
    |-- notebooks
    |
    |-- src
    |   |   __init__.py
    |   |
    |   |-- features
    |   |       __init__.py
    |   |
    |   |-- models
    |   |       __init__.py
    |   |
    |   |-- utils
    |   |       __init__.py
    |   |
    |   |-- visualizations
    |   |       __init__.py
    |
    |-- test
    |   |   __init__.py
    |   |
    |   |-- features
    |   |       __init__.py
    |   |
    |   |-- models
    |   |       __init__.py
    |   |
    |   |-- utils
    |   |       __init__.py
    |   |
    |   |-- visualizations
    |   |       __init__.py
    |
    |-- output
```

We'll discuss each directory below.

* `my_project`: This is the root directory for the project. You can make the name appropriate for the data science project.

* `venv`: This directory contains the virtualenv for this project. Actually, you shouldn't manually create this directory. Instead, in the project root, run `virtualenv venv` to create the virtualenv

* `git_repo`: Everything (well, mostly everything) in this directory is part of the git repository. When you create this folder, you can navigate inside it and run `git init` to create a new git repository. Among the files in this folder is requirements.txt, which contains all python packages used in this project

* `config`: This directory contains all configuration files used for the project. Config files specify things like project directories, login credentials, and modeling parameters

* `data`: All data used in the project lives here. The raw, unmodified data should go in `raw`, and any processed, cleaned, or filtered data should go in `processed`

* `notebooks`: This is where any jupyter notebooks should go

* `src`: Any python code that is not a jupyter notebook should go here. Any code for generating, loading, cleaning, or processing features should be in `features`. Any code that has to do with defining, training, testing, loading, or saving models should go in `models`. Any additional code with no where else to live should go in `utils`, for example, code that interacts with a database or web API. Lastly, `visualizations` contains any code used for generating visualizations.

* `test`: This directory mirrors the directory structure of `src`, and contains any code written to test the performance of the code in `test`.

* `output`: This directory is a place to put any visualizations, models, or other output produced for the project


The `__init__.py` files tell Python that this is a python package, so that modules you write can be imported conveniently.


## Computer Environment

### Environment Variables

In our project we'll want to import Python modules by using paths relative to the source code directory, so let's add the project directory to the PYTHONPATH enironment variable.
To set an environment variable in bash, simply add an export statement to your `.bashrc` file that points to the project root:

`export PYTHONPATH=$PYTHONPATH:/path/to/my_project/`

where you replace `/path/to/my_project` with the path to the root directory of your project.

We want to use a configuration file for our project, so let's set an environment variable that points to that file. Again, add the following to your `.bashrc`:

`export MYPROJECTROOT="/path/to/git_repo/"`

where you replace `/path/to/git_repo/` with the path to the git repository directory.

Note: If you are running multiple projects, it may make sense to change `MYPROJECTROOT` to some name that reflects your project, like `DENVERCRIMEROOT`
