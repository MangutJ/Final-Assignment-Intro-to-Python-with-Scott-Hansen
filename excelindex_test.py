# Import the functions
from excelindex import find_num, find_string

# Example usage of find_num function
col_num = find_num("A")
print("Numeric value of the column is:", col_num)

# Example usage of find_string function
col_string = find_string(33)
print("String representation of the column number is:", col_string)
