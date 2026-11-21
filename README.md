# python-practice

Daily Python practice: small scripts and projects.

## Expense Summary Tool

A small Python script that reads a CSV file of expenses, adds up the spending in each category, and saves a summary. It is useful for students tracking pocket money, small shop owners, or anyone who keeps their spending in a spreadsheet.

### What you need
- Python 3 installed
- A CSV file named `expenses.csv` in the same folder as `expenses.py`, with these columns in the first line:

```
date,category,amount
2026-11-01,food,120
```

### How to run
1. Download or copy `expenses.py` and put it in the same folder as your CSV file.
2. If your file has a different name, change the file name in the line `open("expenses.csv")` inside `expenses.py`.
3. Open a terminal in that folder and run:

```
python expenses.py
```

### What it produces
- The overall total of all expenses
- The amounts grouped by category
- The single biggest expense and the category it belongs to
- A file called `summary.csv` with one line per category and its total <!-- check: does your file have the header line "category,total"? -->

### Notes
- If a row has an amount that is not a number (for example `abc`), the script skips that row and prints a warning,so the rest of the file is still processed.
- The `amount` column is read as text and converted to a number, so values like `120` or `85.5` both work.
- Only the biggest expense is reported, not the smallest.