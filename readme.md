# Results v4.0

## Description

I decided to rewrite this python project in order to improve previous versions.

The main idea is to obtain how many times a number is repeating in a list of 36 and 108 numbers.

I based the idea in the results of a local lottery who plays several times a week, so each list is the result of the winning combination.

After enter the data of each week, the program shows the numbers who have 2, 3, 4 and 5 or more repetitions separately in the shorter version of the game (36 numbers) and in the long version of the game (108 numbers).

The file named "main.py" is the launcher program, the file named "minis.py" contains the functions of the main program and the file named "dbaction.py" contains the functions for the database actions.

In version 2.0, I used 2 txt files storing the results of the last 6 weeks but now I use a database named "results.db" that contains a table named "games" with all de numbers of the 2 types of games. This database has created in SQLite.

I use SQL script files contains sql sentences to update the data after enter de new numbers, there are 2 SQL scripts (one for each game).

For this project I'm using 2 python modules ("os" and "tabulate") and elements like functions, lists, tuples and statements if, elif and for.

<br>

The program is still growing, so I'm going to still update the progress.

<br>

## Project Files

<br>

## Project Folders

<br>

> ### **If you think education is expensive, try ignorance. - Derek Bok**