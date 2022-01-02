# Udacity US Bikeshare Data Analysis Project

This project was a part of Udacity's Data Analysis Professional Nanodegree Program.

## Overview
In this project, we will use Python to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington.

- The code takes in raw input from the user.
- According to the input the code will import the data and will provide information by computing descriptive statistics.

## File used:
- US_bikeshare.py

## Softwares needed:
- Python 3

## Libraries needed:
- pandas
- time

## How to run the code:
 - Download and install [Python 3.7](https://www.python.org/downloads/)
 - install [pandas](https://pandas.pydata.org/pandas-docs/stable/getting_started/install.html)
 - Download by one of 2 methods:
   - Press "Code" and then press "Download Zip"
   - Use `git clone https://github.com/Ibrahim-MohamedH/Udacity-US-Bikeshare-Data-Analysis-Project.git` to download the files to your machine
 - unrar "csv files.rar" and make sure all of the content are in the same folder
 - run and test the code by typing `python US_bikeshare.py`

## Code explained in Detail:
The code interact with the user by taking raw input to create an interactive experience in the terminal that answers questions about the dataset depending on the users input.
The questions that will change the answers:
 
 - Which city would you like to see its data, (chicago, new york city, or washington)?
 - Would you like to filter both Months and Days?
 - (If person choose yes):
      - Which month would you like to filter the data according to? (ex: all, january, february, ... , june)
      - Which day would you like to filter the data according to? (ex: all, monday, tuesday, ... sunday)

The answers to the questions above will determine the city and timeframe on which you'll do data analysis. After filtering the dataset, users will see the statistical result of the data, and choose to start again or exit.

## Statistics Computed:

1. Popular times of travel (i.e., occurs most often in the start time)

- most common month
- most common day of week
- most common hour of day

2. Popular stations and trip

- most common start station
- most common end station
- most common trip from start to end (i.e., most frequent combination of start station and end station)

3. Trip duration

- total travel time
- average travel time

4. User info

- counts of each user type
- counts of each gender (only available for NYC and Chicago)
- earliest, most recent, most common year of birth (only available for NYC and Chicago)
 
