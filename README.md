# Python Tutorial
Juyper Notebook based Python tutorial

## Target Audience

* Python beginners with experience in other programming languages (like Java, C++), who want to learn the specialities and features of Python.

* Python programmers with medicore experience may find some useful information in this tutorial, too.

This tutorial is not intended for:

* Beginners with no (object-oriented) programming experience - basic programming concepts are not introduced in detail, but expected from the reader.

* Python experts (obviously...)

## Structure

This tutorial is not structured linearly (from chapter 1-x), but the notebooks covering specific topics are rather independent from each other.
I tried to illustrate the various points without requiring too much knowledge of other topics, but implicit dependencies could not be avoided.

## Docker-based Installation

1. Install Docker (including docker-compose)

    a. Windows 10 Professional: https://docs.docker.com/docker-for-windows/install/

    b. other Windows versions: https://docs.docker.com/toolbox/toolbox_install_windows/

    c. Linux (link is for Ubuntu): https://docs.docker.com/install/linux/docker-ce/ubuntu/

2. Install Git for Windows (in Linux usually already available): https://gitforwindows.org/

3. Clone this repository with Git into an empty directory

        git clone https://github.com/lungben/python_tutorial .


4. In [docker-compose.yml](docker-compose.yml), adjust the local paths (1st part before colon) in the *volume* statements to local directories (to be created beforehand).

5. Start the Jupyter and Database server:

        docker-compose up -d


6. Start Jupyter Lab: http://localhost:8888/lab

### Update Containers

    docker-compose down # stops and removes all containers
    docker-compose pull # downloads newest image versions
    docker-compose build # (re-) builds custom images
    docker-compose up -d # starts container
    
### Update Conda Packages

The official Jupyter Docker image usually does not contain the latest versions of the Conda packages.
To update all packages, use the following commands:

    docker exec -it tutorial_jupyter_1 bash # starts bash shell in Docker container
    conda update -n base --yes conda
    conda update --all --yes
    exit # exists container shell
    
__Warning:__ While updating all packages usually works fine for a local Conda installation, it seems to break the Jupyter Docker container rather often.
Fortunately it is easy to restore Docker containers to their original state, just follow the instructions for Update Containers above.

## Local Installation

### Anaconda

The Anaconda package contains a large number of libraries and can be used out-of-the-box for most parts of this tutorial (except external databases).

The drawback is that it includes also a number of libraries which are not required, therefore it may be a bit too heavy for many purposes.

https://www.anaconda.com/distribution/#download-section

Download Python 3.x version.

### Miniconda

Miniconda contains only the Conda package manager and its dependencies. It allows to create custom virtual environments with exactly the required packages. 

https://docs.conda.io/en/latest/miniconda.html

Create virtual environment for tutorial:

    conda update conda
    conda create -n tutorial python=3.7 ipython notebook juypterlab numpy pandas matplotlib seaborn scipy numba pytest sympy sqlalchemy
    activate tutorial

More packages may be installed later using 

    conda install -n tutorial package_name

## Technology

This tutorial is written for Python 3.7+. No effort has been made or will be made for compatibility to legacy Python versions (e.g. Python 2.7).

The notebooks can be opened using Jupyter Notebook or Jupyter Lab.

It is assumed that all packages included in the Anaconda distribution are installed. If Miniconda is used, it may be required to install additional packages using

    conda install [-c conda-forge] package --yes
    
## Useful JupyterLab Settings:

Keyboard shortcuts:

    {
        // Move cell up
        "notebook:move-cell-up": {
          "selector": ".jp-Notebook:focus",
          "command": "notebook:move-cell-up",
          "keys": [
            "Ctrl ArrowUp"
          ]
        },

        // Move cell down
        "notebook:move-cell-down": {
          "selector": ".jp-Notebook:focus",
          "command": "notebook:move-cell-down",
          "keys": [
            "Ctrl ArrowDown"
          ]
        }
    }
    
## Recommended Software

* Git for Windows (in Linux usually already available): https://gitforwindows.org/
* Miniconda or Anaconda: https://docs.conda.io/en/latest/miniconda.html
* PyCharm CE: https://www.jetbrains.com/pycharm/download/
* Docker: https://docs.docker.com/docker-for-windows/install/
    
# Table of Content

## Python General

[Variables and Data Types](notebooks/variables_and_data_types.ipynb)

[Loops, Iterators and Flow Control](notebooks/loops_iterators_and_flow_control.ipynb)

[Functions](notebooks/functions.ipynb)

[Classes](notebooks/classes.ipynb)

[Modules and Imports](notebooks/modules_and_imports.ipynb)

[Multithreading and Multiprocessing](notebooks/parallel_computing.ipynb)

[Logging and Exception Handling](notebooks/logging_and_exception_handling.ipynb)

[Unit Tests](notebooks/testing.ipynb)

## Numeric Calculations and Data Analysis

[Numpy](notebooks/numpy.ipynb)

[Pandas](notebooks/pandas.ipynb)

[Numba JIT Compiler](notebooks/numba_jit.ipynb)

[Plotting with Matplotlib and Seaborn](notebooks/plotting.ipynb)

[Interactive Visualizations with Plotly](notebooks/plotly.ipynb)

[Symbolic Computation using SymPy](notebooks/symbolic_computation.ipynb)

[Parallelization with Dask](notebooks/dask.ipynb)

Mathematical Finance with Quantlib

## Web Framework

[Flask Hello World Example](notebooks/flask_web_framework.ipynb)

Dash and Dash Table

## Databases

[Relational Databases](notebooks/relational_databases.ipynb)

[Object-Relational Mapping with SQLAlchemy](notebooks/sqlalchemy_orm.ipynb)

[MongoDB](notebooks/mongo_db.ipynb)

Redis

Batch Job Pipelining with Luigi
