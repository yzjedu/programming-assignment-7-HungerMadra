import csv

# Constants for column indices
BUDGET_INDEX = 2
GROSS_INDEX = 3
PROFIT_INDEX = 4

# Function that loads movie data from a CSV file and returns it as a list of lists.
def load_movie_data(filename):
    """Load movie data from a CSV file into a list of lists."""
    with open(filename, mode='r', newline='') as file:
        reader = csv.reader(file)
        # Read header
        header = next(reader)
        # Read data rows
        data = [row for row in reader]
    return header, data

# Function that adds a profit column to the movie data.
def add_profit_column(movie_data):
    """Add a profit column to the movie data."""
    for row in movie_data:
        budget = float(row[BUDGET_INDEX])
        gross = float(row[GROSS_INDEX])
        profit = gross - budget
        row.append(f"{profit:.2f}")  # Add profit column with two decimal places

# Function that prints the movies with the highest and lowest profits.
def print_min_and_max_profit(movie_data):
    """Find and print movies with the highest and lowest profits."""
    if not movie_data:
        print("No data available.")
        return
    
    # Initialize min and max profit
    min_profit = float('inf')
    max_profit = float('-inf')
    min_profit_movie = None
    max_profit_movie = None

    for row in movie_data:
        profit = float(row[PROFIT_INDEX])
        if profit < min_profit:
            min_profit = profit
            min_profit_movie = row
        if profit > max_profit:
            max_profit = profit
            max_profit_movie = row

    print(f"Movie with the highest profit: {max_profit_movie}")
    print(f"Movie with the lowest profit: {min_profit_movie}")

# Function that saves the movie data with the profit column to a new CSV file.
def save_movie_data(movie_data, output_filename):
    """Save the updated movie data with the profit column to a new CSV file."""
    with open(output_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Write header with new profit column
        writer.writerow(['Date', 'Title', 'Budget', 'Gross', 'Profit'])
        # Write data rows
        writer.writerows(movie_data)

def main():
    # Load movie data
    header, movie_data = load_movie_data('movies.csv')
    
    # Add profit column
    add_profit_column(movie_data)
    
    # Identify and print movies with min and max profit
    print_min_and_max_profit(movie_data)
    
    # Save updated data
    save_movie_data(movie_data, 'updated_movies.csv')

if __name__ == "__main__":
    main()
