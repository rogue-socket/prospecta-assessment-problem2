# Prospecta Assignment Problem 2

### Note: 
The solution to the case in the problem sheet(`data.csv`) is stored in `final1.csv` and for another test case(`data2.csv`) is stored in `final2.csv`

## Overview
This project processes expressions stored in a CSV file, evaluates them, and saves the results back into a new CSV file. It supports basic arithmetic operations between numbers and coordinates (spreadsheet-like references), using a combination of `pandas` and `regex` to parse and process the data.

The primary goal is to evaluate expressions in the format `=A1+B2`, where:
- `A1` and `B2` are cell references (coordinates).
- The expressions can involve basic arithmetic operations (`+`, `-`, `*`, `/`).
- Support is included for decimal and integer values as well.

### Key Features:
- Parses and evaluates expressions from a CSV file.
- Supports both numeric values and cell references (coordinates).
- Handles basic arithmetic operations (`+`, `-`, `*`, `/`).
- Outputs the evaluated results into a new CSV file.

---

## Project Structure

- `data2.csv`: Input CSV file that contains expressions to be evaluated.
- `final1.csv`: Output CSV file that stores the evaluated expressions.
- `main.py`: The main Python script that processes the CSV and evaluates the expressions.

---

## Requirements

This project requires the following Python libraries:
- `pandas`: For reading from and writing to CSV files.
- `re`: For extracting and parsing the components of the expressions.

You can install the required libraries using:
```bash
pip install pandas
```

## How It Works

1. **CSV Input**: The input CSV file (`data2.csv`) has cells containing expressions such as `=A1+B1`. These expressions may refer to other cells or involve direct numeric values.
   
2. **Expression Parsing**: The script parses each expression using regular expressions. It identifies:
   - Whether the expression is a simple arithmetic operation between numbers.
   - Whether the expression refers to coordinates (cell references) like `A1` or `B2`.
   
3. **Expression Evaluation**:
   - If both components are numbers, it evaluates the expression directly.
   - If the components are coordinates, it looks up the values in the relevant cells and evaluates the expression.
   
4. **Output CSV**: The results are written to a new CSV file (`final1.csv`).


## Usage

1. **Prepare the Input File**: Create or modify the `data2.csv` file to include expressions you want to evaluate. Example format: `A1: 10, B1: 20, C1: =A1 + B1`
2. **Run the Script**:
Run the `excel_formula.py` script in your terminal:
```bash
python excel_formula.py
```

## Error Handling

The script includes `try-except` blocks to handle various errors gracefully:
- **File Not Found**: If the input file is not found, the program will print an error message.
- **Invalid Expressions**: If the expression format is incorrect, the program will notify the user and skip that cell.
- **General Errors**: Any unexpected errors will be caught and printed without causing the program to crash.
