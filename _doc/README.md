# _Doc

This directory will contain the documentation for the package. This will be automatically generated from python files through Sphinx documentation tool.

## What is Sphinx?

Well, As mentioned earlier, It is a python package documentation tool. It reads the docstrings in python code and converts  them in to easily readable html format. Sphinx is also capable of converting the documentation into LaTeX format(PDF). The underlaying file format in this documentation is reStructuredText (RST) format, which is a markup language. It is necessary to write proper sphinx-readable docstrings to generate better documentation. See the files in  `_rsc` directory for standard docstring format.

#### reStructuredText:

It is generally uses for textual data in the python documentation. It has it own syntax to define headings, subheadings, bold and italic letters, weblinks, and code blocks. This syntax will be read by sphinx engine and it regenerates beautiful web documents. 

It is important to follow correct syntax, indentation, and space between the commands in rst files and docstrings. There are few .rst files in this directory so please feel free to have a glance at the syntax. After making the web documentation out of this files, you will understand how to use them for your own projects.

## Sphinx installation:

If Sphinx haven't installed in your system, follow this commands to install it and its supporting modules.

#### Installation in windows:

Open command prompt as administrator and use below command to install sphinx in your machine.

```
 pip install -U sphinx
```

 `sphinx-build --version` Use this command to check sphinx version.

Sphinx offers flexibility in changing the webpage format.  *read_docs*  is the most popular theme. In order to install it use this command  `pip install sphinx_rtd_theme`.

So far, we installed all the required modules that necessary to develop documentation.

## Documentation:

* Since the current projects has already dedicated this folder(_doc) for the documentation, open this directory in file explorer and open command prompt. 

* `sphinx-quickstart` use this command to start the documentation.

  * Procced with default options and provide information such as 
    * project name
    * author name
    * release version

*  It will create few file and folder in this directory. 

* Now, we have to modify `conf.py` file according to the our project file structure. 

* Open `conf.py`

  * Uncomment the lines 13th-15th and replace the line 15th with this code `sys.path.insert(0, os.path.abspath('../_src'))`. 
  * Add `'sphinx.ext.autodoc'` in the extension list (line no. 33).
  * Also, change html theme from `'alabaster'` to `'sphinx_rtd_theme'`  (line no. 50).

* Lets go back to the command prompt.  Use  ` sphinx-apidoc -o . ../_src` to generate `.rst` for source code in *_src* folder. This command reads the *.py* files in *_src* directory and creates relevant `.rst` files in current working directory.

* Above command creates multiple `.rst` file along with `index.rst` and `modules.rst`

* `index.rst` file defines the contents of developed web-page. we have to add few details to this file so open `index.rst`  and update the file with below content.

* ```
  Project_name Documentation
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  
  Write Project description here.
  
  This documentation is organized into a couple sections:
  
  * :ref:`intro`
  * :ref:`install`
  * :ref:`modules`
  
  .. _intro:
  
  .. toctree::
     :maxdepth: 2
     :caption: Introduction:
  
     1_introduction
     2_contact
     
  .. _install:
  
  .. toctree::
     :maxdepth: 2
     :caption: Installation:
  
     3_install
  
  .. _modules:
  
  .. toctree::
     :maxdepth: 2
     :caption: Modules:  
  
     modules
  
  Indices and tables
  ==================
  
  * :ref:`genindex`
  * :ref:`modindex`
  * :ref:`search`
  
  ```

* Please don't mind this syntax. You get complete idea after seeing the final web documentation. 

* Finally, we are onto last step of this process.

* In command prompt use command, `make html` . This creates multiple html files in *_build/html* directory if the docstrings and `.rst` file are in correct format. Otherwise, it returns error in command prompt.

* After executing all the commands correctly, Open *index.html* in *_build/html* directory to see the project documentation.

## Final notes:

The above mentioned procedure is best suitable for the file structure of this project. To develop the documentation of different type of file structure, few modifications need to be added based the respective file structure. 

**Note:** Please read this documentation in GitHub or markdown editor like Typora.

#### Existing file description:

* `1_introduction.rst` :  contains the information of the project
* `2_contact.rst`: Contact information of contributors.
* `3_install.rst` : Package installation procedure. 