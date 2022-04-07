Introduction
^^^^^^^^^^^^^

This project is intended to demonstrate the standard python project work-flow that is being followed at `Computational Mechanics lab <https://computationalmechanics.in/>`_. By presenting the basic folder structure, this project focuses of documentation of source code for easy collaborations. to presenting in a website through Sphinx documentation tool.

To demonstrate the entire workflow, this projects considered simple maths.py file containing two classes that stores two numbers and performs addition, subtraction, multiplication, and division operations on them. The python code presented is containing properly formatted docstrings, which is mandatory for better representation in final document.

Before starting, look a few open source projects documentation that generated using Sphinx and familiarize yourself with what we are going to finally make.

* `NURBS Python <https://nurbs-python.readthedocs.io/en/5.x/>`_
* `HDF5 for Python <https://docs.h5py.org/en/stable/>`_
* `SimPy <https://simpy.readthedocs.io/en/latest/>`_
* `Conda <https://conda.io/en/latest/>`_

Prerequisites
=============
To follow along with the examples, you need to install below packages into your system. 

*Note: If have installed updated versions of below packages, please ignore the following steps.*

* [Anaconda](https://www.anaconda.com/)

Anaconda Installation
---------------------

After downloading the Anaconda, follow `Anaconda Install <https://docs.anaconda.com/anaconda/install/>`_ instruction based on your system configuration. 

**Important:** *While installing the anaconda, make sure below boxes are checked.*

.. image:: https://user-images.githubusercontent.com/33441778/161914017-3b8b8a4b-79be-4cfc-aa12-bb36811cc2b1.png
    :width: 400

Sphinx Installation
-------------------

Open command prompt as administrator and use below command to install sphinx in your machine.

`pip install -U sphinx`

**Note:** *If you are not able to execute above command through command prompt, open anaconda prompt as administrator to execute the commands.*

`sphinx-build --version` Use this command to check sphinx version.

Sphinx offers flexibility in changing the webpage format.  *read_docs*  is the most popular theme. In order to install it use this command  

`pip install sphinx_rtd_theme`

So far, we installed all the required modules that necessary to develop documentation. Please refer to _doc/README.md for documentation process using Sphinx.

Authors
=======

* `Abhinav Gupta <abhigupta.io>`_
* `Bhagath Mamindlapelly <https://github.com/bhagath555>`_