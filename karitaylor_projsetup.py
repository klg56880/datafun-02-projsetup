''' This module provides functions for creating a series of project folders. '''

#import dependencies
import pathlib
import time
import karitaylor_utils

# Function 1: Create folders for a given range
def create_folders_for_range(start_year, end_year):
    for year in range(start_year, end_year):
        pathlib.Path(f"{year}").mkdir(exist_ok=True)

# Function 2: Create folders from a list of names
def create_folders_from_list(folder_list):
    for folder in folder_list:
        pathlib.Path(folder).mkdir(exist_ok=True)

# Function 3: Create prefixed folders
def create_prefixed_folders(folder_list, prefix):
    for folder in folder_list:
        pathlib.Path(f"{prefix}-{folder}").mkdir(exist_ok=True)

# Function 4: Create folders periodically
def create_folders_periodically(duration,period):
    start_time = time.time()
    while(time.time()-start_time < duration):
        current_time = time.time()-start_time
        pathlib.Path(f"Folder created at {round(current_time)} seconds").mkdir(exist_ok=True)
        time.sleep(period) 

# Create a path object
project_path = pathlib.Path.cwd()

# Define the new sub folder path
data_path = project_path.joinpath('data')

# Create new if it doesn't exist, otherwise do nothing
data_path.mkdir(exist_ok=True)

def main():

    # Print byline from imported module
    print(f"Byline:{karitaylor_utils}")

    # Call function 1 to create folders for a range (e.g. years)
    create_folders_for_range(start_year=2021, end_year=2024)

    # Call function 2 to create folders given a list
    folder_names = ['digital_format-svg', 'digital_format-png', 'digital_format-eps', 'digital_format-dxf']
    create_folders_from_list(folder_names)

    # Call function 3 to create folders using comprehension
    folder_names = ['svg', 'png', 'eps', 'dxf']
    prefix = 'digital_format-'
    create_prefixed_folders(folder_names, prefix)

    # Call function 4 to create folders periodically using while
    duration_secs = 5  # duration in seconds
    create_folders_periodically(duration=20, period=5)

if __name__ == '__main__':
    main()