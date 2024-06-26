# I want this application to build a markdown report. 


import argparse

parser = argparse.ArgumentParser(description='Analyze a stock')
parser.add_argument('ticker', type=str, help='the stock ticker to analyze, e.g. GOOGL', nargs='?')
args = parser.parse_args()
ticker = args.ticker
if not ticker:
    raise ValueError('Please provide a stock ticker')


start_date = input("Enter a start date (YYYY-MM-DD): (e.g. 2023-01-01) ")
examples = ["2023-01-01", "2019-01-01", "2020-01-01"]
print(f"Examples: {examples}")



# pass into main.py
ticker = "VEOEY"
# start_date = "2023-01-01"
- run src/main.py

-


- store markdown file in outputs\ticker folder