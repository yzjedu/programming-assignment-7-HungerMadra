[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/MfaW3-GZ)
# Programming Assignment 07: Movie Profit Analysis

## Notice

- **For this assignment you can work in a group of two or three members**
- Forming a group is totaly upto you

## Objective

This lab is designed to test your understanding of file handling, list manipulation, and basic data analysis in Python. You will process a CSV file containing movie data, compute the profit for each movie, and identify the movies with the highest and lowest profits.

## Problem Statement

You will write a Python program that:

1. Loads movie data from a CSV file.
2. Adds a column for each movie's profit (calculated as `gross - budget`).
3. Identifies and prints the movies with the highest and lowest profits.
4. Saves the updated movie data to a new CSV file.

### Tasks

1. **Load Movie Data**:

   - Implement the `load_movie_data(filename)` function to read data from a CSV file into a list of lists.

2. **Add Profit Column**:

   - Implement the `add_profit_column(movie_data)` function to add a profit column to the movie data.

3. **Identify Min and Max Profits**:

   - Implement the `print_min_and_max_profit(movie_data)` function to find and print details of the movies with the highest and lowest profits.

4. **Save Updated Data**:

   - Implement the `save_movie_data(movie_data, output_filename)` function to save the updated data to a new CSV file.

5. **Main Function**:
   - Implement the `main()` function to orchestrate the program's workflow.

## Submission

- Clone the project
- Follow the instructions on the README.md file and the comment on code
  - Complete the code
  - You can look into the `test_assignment.py` for inspiratin too
- **Test the program**: by running `pytest`
  - If the test passes
    - Push the project to the repository
      - If this is hard
      - Submit the assignment.py on moodle
