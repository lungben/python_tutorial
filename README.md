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

## Technology

This tutorial is written for Python 3.

The notebooks can be opened using Jupyter Notebook or Jupyter Lab.

It is assumed that all packages included in the Anaconda distribution are installed. If Miniconda is used, it may be required to install additional packages using

    conda install [-c conda-forge] package --yes
    
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

## Web Framework

Plotly

Flask

Dash and Dash Table

## Databases

[Relational Databases](notebooks/relational_databases.ipynb)

[No-SQL Databases](notebooks/no_sql_databases.ipynb)

## Additional Libraries

Quantlib

Luigi

Dask

SymPy

