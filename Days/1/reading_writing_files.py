import csv #Imports CSV module for writing and reading CSV files
import os #Imports this module that allows to check for file existance



"""

Mode	Meaning
"r"	    Read (default, error if file doesn’t exist)
"w"	    Write (creates file, overwrites existing content)
"a"	    Append (creates file if missing, adds to existing content)
"x"	    Exclusive creation (errors if file exists)
"r+"	Read & write (file must exist)
"w+"	Read & write (overwrites file)
"a+"	Read & append (creates if missing)

Look at Pandas, Install node and do the same code for javascript

"""

def get_headers_and_first_column(filename):
    """Reads a CSV file and returns the headers and first column as lists."""
    with open(filename, "r") as file:  # Open the CSV file in read mode. 'as' creates a tempory reference
        reader = csv.reader(file)  # Create a CSV reader object to read the file. Allows the code to iterate over the rows
        headers = next(reader)  # Extract the first row, which contains headers
        first_column = [row[0] for row in reader]  # Extract the first column from all remaining rows
    
    return headers, first_column  # Return the headers and first column as a tuple

def get_unique_filename(base_name="exported_data", extension=".csv"):
    """Generates a unique filename by incrementing a number if the file exists."""
    counter = 1  # Start with file number 1
    while True:  # Infinite loop that keeps checking for available filenames
        filename = f"{base_name}_{counter}{extension}"  # Create a filename like exported_data_1.csv
        if not os.path.exists(filename):  # Check if this filename already exists
            return filename  # If not, return this filename to use it
        counter += 1  # If the file exists, increase the counter and check again

def export_to_csv(headers, first_column):
    """Exports the first header and first column values to a uniquely named CSV file."""
    filename = get_unique_filename()  # Get a unique filename (e.g., exported_data_1.csv)

    with open(filename, "w", newline="") as file:  # Open the file in write mode
        writer = csv.writer(file)  # Create a CSV writer object to write data
        writer.writerow([headers[0]])  # Write only the first header (column name)
        for value in first_column:  # Loop through each value in the first column
            writer.writerow([value])  # Write each value in a new row
    
    print(f"Data exported successfully to {filename}")  # Print success message with filename

# Example usage:
csv_file = "PM25.csv"  # Define the input CSV file name
headers, first_column = get_headers_and_first_column(csv_file)  # Extract headers & first column
export_to_csv(headers, first_column)  # Export the data to a new CSV file