""" Start a Data Analytics Project"""

import pathlib

def create_project_directory(directory_name: str): # add type hinting to params
    """
    Creates a project sub-directory.
    : param directory_name: Name to be created, e.g. "test"
    """
    pathlib.Path(directory_name).mkdir(exist_ok=True)

def main():
    """ Scaffold a project. """
    create_project_directory(directory_name='test') # name the parameter
    create_project_directory(directory_name='docs') # name the parameter

if __name__ == '__main__':
    main()
