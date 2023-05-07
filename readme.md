#### Provide a link to your source control repository
https://github.com/Shanzie/BladeHill_T1A3

## Introduction

The watchlist application is designed to help you keep track of movies and series you want to watch. It allows you to add movies and series to a watchlist, view and manage your list, and pick a random movie or series to watch.

## System Requirements

- Operating System: Windows, MacOS, or Linux
- Python: 3.7 or higher

## Dependencies

The watchlist application requires the following Python modules to be installed:

- json
- random
- argparse

## Installation

1. Download or clone the watchlist application from the project's repository.
2. Extract the files to your desired location.
3. Open a terminal or command prompt window.
4. Navigate to the directory where you extracted the files.
5. Run the command chmod +x watchlist.sh
6. Run the command ./watchlist.sh

### Usage

Using the watchlist is quite simple after running the last command in the installation process you will be prompted with a text based user interface that shows you your options. Proceed from there and the program should naturally guide you through the process.



# Feature Implementation

#### Feature: Add movie to Watchlist
- Add option to user menu to add a movie to the Watchlist
- When the user selects add movie, prompt the user to enter the movie name, genre, and release date
- Create a dictionary object for the movie and add it to the Watchlist JSON file
- Check if the movie is already in the watchlist and display an error message if it is
- **Priority:** High
- **Deadline:** 2 days

#### Feature: Remove movie from Watchlist
- Add option to user menu to remove a movie from the Watchlist
- When the user selects remove movie, prompt the user to enter the movie name
- Remove the movie from the Watchlist JSON file if it exists, or display an error message if it doesn't
- **Priority:** High
- **Deadline:** 2 days

#### Feature: Display Watchlist
- Add option to user menu to display the current Watchlist
- Read the Watchlist JSON file and display the movie titles, genres, and release dates in a formatted table
- **Priority:** High
- **Deadline:** 2 days

#### Feature: Search Watchlist
- Add option to user menu to search the Watchlist for a movie
- When the user selects search, prompt the user to enter a movie name
- Search the Watchlist JSON file for the movie and display the movie details if it exists, or display an error message if it doesn't
- **Priority:** Medium
- **Deadline:** 4 days

#### Feature: Export Watchlist
- Add option to user menu to export the Watchlist to a CSV file
- Read the Watchlist JSON file and convert it to a CSV format
- Save the CSV file in the same directory as the Watchlist Python script
- **Priority:** Low
- **Deadline:** 7 days

#### Feature: Import Watchlist
- Add option to user menu to import a Watchlist from a CSV file
- Prompt the user to select a CSV file to import
- Read the CSV file and convert it to a valid Watchlist JSON file format
- Import the Watchlist JSON file and replace the current Watchlist
- **Priority:** Low
- **Deadline:** 7 days

#### Feature: Pick a Random Movie
- Add option to user menu to pick a random movie from the Watchlist
- When the user selects pick movie, choose a random movie from the Watchlist
- Display the randomly selected movie to the user
- **Priority:** medium
- **Deadline:** 3 days

## Checklist for each feature:

Add movie to Watchlist:
- Add option to user menu ✓
- Prompt user for input ✓
- Create dictionary object for movie ✓
- Add dictionary to Watchlist file ✓
- Check if movie already exists in Watchlist ✓

Remove movie from Watchlist:
- Add option to user menu ✓
- Prompt user for input ✓
- Remove movie from Watchlist ✓
- Check if movie exists in Watchlist ✓

Display Watchlist:
- Add option to user menu ✓
- Read Watchlist file ✓
- Display movie titles, genres, and release dates ✓
- Format table output ✓
- Show Episode Number and Series x

Search Watchlist:
- Add option to user menu ✓
- Prompt user for input ✓
- Search Watchlist file ✓
- Display movie details ✓
- Display error message if movie not found ✓

Export Watchlist:
- Add option to user menu ✓
- Read Watchlist file ✓
- Convert Watchlist to CSV format ✓
- Save CSV file to directory ✓

Import Watchlist:
- Add option to user menu ✓
- Prompt user for CSV file ✓
- Read CSV file ✓
- Convert CSV file to Watchlist format ✓
- Replace current Watchlist ✓

Pick a Random Movie:
- Add option to user menu ✓
- Pick a random movie from Watchlist ✓
- Display the randomly selected movie ✓

## Testing the Program

#### Test 1 - Adding a movie and series to the list

First I tried to add the movie 

![](/docs/image.png)