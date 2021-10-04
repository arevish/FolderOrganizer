# Folder Formatter    ![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

## Problem Statement:
Created a program to "Organize and Prettify my Folder"

**what it do**
Suppose you have a folder, and its path is also given. It takes three input arguments, which are:

Full path of the folder as input strings.

Dictionary file

File Format

`("C://", "name.txt", "jpg")`
The function will perform these tasks:

* First, it will check all the files present in the folder whose paths are given as an input argument.
* Then it will *capitalize* the first letter of each file. 
* If the file's name is present in a *dictionary file*, then it will *not capitalize* the first letter. It will only capitalize the first letter of the files, which are not present in the dictionary file. 
* The function renames the file names to numbers whose format is the same as mentioned in the input parameter like 1.jpg.
* After performing these tasks, your folder will be prettified as all the first letters of the files will be capitalized except for those whose names are present in the dictionary file. And the files having the same format as given in the input argument will rename to number to identify files easily.

### Module used
python module os

## PRE-REQUISITES
Your laptop with 3.7.x (onwards) installed.

**NOTE:** Those with Linux and MacOSX would have Python installed by default, no action required.

Windows: Download the version for your laptop via https://www.python.org/downloads/

**NOTES**
In your preferred editor, make sure indentation is set to "4 spaces".

## Run using Python3.8+
1. Clone or download repositiory: https://github.com/arevish/FolderOrganizer.git
2. In source folder, run `python3 'FolderOrganizer.py'` to start program, optionally, run with `--help` argument to see other runtime options.
