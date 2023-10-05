# *Python Project Environment*

Uses the standard python3 library (version 3.11).

* Ensure the following are installed:
  * pip
  * pytest
  * The project itself (two options)
    * Install manually with command `python3 -m pip install -e .`
    * Install `requirements.txt`

## *Run Configuration Description*

Three primary files:

* Source Code `nhl_lines.py`
  * not meant to run - import within another program to utilize the class.
* client demonstration file `client.py`
  * Run this to utilize the program and demo the methods of the Lines class imported from the source code `nhl_lines.py`
  * Follow instructions prompted when you run the program!
* three tests within the tests directory
  * test both primary methods and the read-in helper method contained in `nhl_lines.py`. One file for each test. Must
    have pip and pytest installed in order to run the tests.

## *How to run the test cases*

1. ensure pip and pytest packages are downloaded
2. ensure you have the entire project cloned locally, as you will need to import from the source code in src directory,
   and you will need the data files in the data directory. Otherwise, the paths will need to be updated if the project
   file structure is changed.
3. Run the test program!

