.. _gettingstarted:

===============
Getting Started
===============

Getting started, in terms of development environment setup, should be very easy since the project is written in pure Python with zero required dependencies. However, please follow the steps carefully because it will make your life easier later on. 

Getting the source code
^^^^^^^^^^^^^^^^^^^^^^^

All of the source code for this project is version controlled using git and shared on GitHub. You will need to have git installed on your computer, then follow these steps: 

1. Create a folder on your computer and inside that folder run::

      git init

2. Add the repo as your remote::

     git remote add origin git@github.com:yonathanF/Repair-Graph-Compression.git

 * If that didn't work, you might have to use https version instead::

    git remote add origin https://github.com/yonathanF/Repair-Graph-Compression.git


You now have all of the source code. But there is one more thing to setup. We are using virtual environments to avoid different results between different team members, so we will need to setup Virtual Env and download our dependencies. [1]_ Follow these steps:

1. Get Python 3, if you don't already have it. [3]_

2. Download Pip. Their site has a quick setup [2]_ but if you are on linux, you might want to consider downloading it using your package manager. 

3. Create a virtual environment. Go to the folder you created above, and run::
   
     python3 -m venv env/
        
4. Activate the virtual env. You want to do this step very time you work on this project. On Posix systems::

     source env/bin/activate

  * If you are on Windows::

     env\bin\activate.bat

5. Install the dependencies::

     pip install -r requirements/requirements_dev.txt
   

That's it! You are good to go. You might want to run the last command to stay upto date when we add new packages, but that's it for now!

Tools
^^^^^
There are some tools in place to make life easier. These are either the easiest to use or the standards in the community. 

Unit Tests 
----------
Although this isn't a software development project, we still need some level of confidence in the quality of the code. At minimum we would like to know the code does its most basic task correctly, and so you must provide unit tests that test the happy path. Usually two or three tests are enough but you should try to cover as many edge cases as possible. We use Python's own `Unittest` please don't use any other frameworks since it will just be more work to keep track of them. Here are some commands to get you started:: 

   python -m unittest discover -s tests # run all tests 
   python -m unittest tests.test_file_name # run a module of tests
   python -m unittest tests.test_file_name.TestCaseName # to run a single test case
   python -m unittest tests.test_file_name.TestCaseName.test_method_name # to run a single test in a given test case 

You should run these commands in the highest level of the directory (same level as `tests/`).

Coverage
--------

We use line coverage to measure out unit tests' coverage. While this isn't the best metric for it, we just need the bare minimum and this does it for us. The package `Coverage.py` should already be on your system if you went through the setup steps above. You can generate a report using this::

   coverage run --source='.' -m unittest discover -s tests/
   coverage html # recommended
   coverage report # to just see the numbers

Try to have 80% coverage or more at all times. 

Linting
-------

Python is very opinionated, perhaps a little too much, but this makes it easy to work in teams. Linting is a way to check your code for known bad practice, possible bugs, and style problems. The CI server will reject your code if the linter returns none 0 values, so please check it locally before pushing. Pylint should be part of your env already. Here is how to use it::

   pylint folder/python_file_name.py # to lint a single file
   pylint folder/ # to lint all the python files within 
   pylint folder1 folder2 folder3   # to lint multiple python folders

There are some rules that are useless and we ignore them (e.g. whitespace). If you come across a rule that you think is useless, please discuss with the team to add it to the ignore list. 

Contribution Guidelines
^^^^^^^^^^^^^^^^^^^^^^^

As we add more and more code to the project, it must agree upon some basic rules to avoid stepping on each other. There are tools in place to make this easier (e.g. Git, linters,TravisCI, etc) but at the end of the day, it's all about communication. If in doubt, use one of the communication channels to talk to someone. 

Working with Git
----------------

Git is both powerful and annoying. Fortunately, we only need some features to operate: pull, push, commit, merge, branch. Google everything else. 

**Commit often** 

Think of it like hitting save. Your last commit for the feature/fix/etc should be VERY detailed. Don't use `-m` for it. Write a *subject line* (a single sentence summary of what you did), followed by an empty line, followed by a paragraph describing *what* you solved/fixed, followed by an empty line, followed by a paragraph describing *how* you solved it. Follow this format strictly for the last commit. This makes the code changes amazingly traceable using git (e.g. someone can see who changed a given line, when, why, and how). 

**Branch often** 

Think of it like copy-pasting the source code into a new folder. Branches are very lightweight and an amazing way to isolate different works. Don't be afraid to have many branches; you can quickly delete them if you need to. By using branches to isolate your work, you can avoid merge conflicts for the most part. Here are a few rules related to branches: 

1. Name your branches using the following format: `theme_area_firstName`. The theme should be something like `bugfix` or `refactoring`. The area should be more specific to what you are fixing, refactoring, etc; e.g. `graphs` or `generator`. And, ofcourse, the firstname should be your first name. 

2. You can't push to the branches `master` and `development`. You need to make a pull request and at least 1 person needs to review it and TravisCI must green light it, before it gets merged into either of those branches. This is because `master` should always be stable and `development` should be stable enough for us to branch off of when we do work.

3. Related to (2) above, use the Git Workflow. [4]_ Branch off of development, do your work there, write unit tests, etc, push it to Travis, get the green light, and make a pull request. If you are working with someone else on the same problem/feature, you should create a different branch to combine your works. Handle your merge conflicts there and make a    pull request from the combined branch. Pull request into development only. 

**Use issues** 

Issues are the team's todo list. They make it really easy to discuss code, progress, and larger goals. For example, if you have a line like `Issue #12` in your commit, GitHub will link that commit in the issue comments. GitHub also  provides a board for Agile development. All new issues go into the Backlog. When we decide to work on a given issue, we move it into Todo. It's then moved into In Progress once someone starts working on it. When the issue is closed, Automation will put the issue into the Done column. This makes it easy to see who's doing what and how much time we need to finish whatever feature/fix. 


File Organization
-----------------

The file organization is self explanatory, but for completeness sake: 

* Graph directory --> Contains graphs, and cluster
* Nodes directory --> Contains nodes
* Repair directory --> Contains the Repair algorithm (both compression and decompression) 
* Algorithms directory --> Contains algorithms that run on graphs 
* Utils directory --> General tools like the graph visualizer and GraphML generator 
* Tests directory --> All the tests 
* Docs directory --> Contains this documentation 
* Requirements directory --> Contains the production and development requirements 


.. [1] The main program doesn't need any of these packages. They are used for generating this documentation, and linting tools. 

.. [2] https://pip.pypa.io/en/stable/installing/
.. [3] https://www.python.org/downloads/
.. [4] https://www.atlassian.com/git/tutorials/comparing-workflows
