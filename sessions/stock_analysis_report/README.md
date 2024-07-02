## Overview

This is a simple applcation that can be used to generate a markdown report of stock data.

For a given ticker and start date it will return technical indicators plotted with a description of each indicator for what to look for.

## Notes for construction.

### Todo

- [ ] Modularise (main:main) and (app: generate_markdown_report) creation function to allow optional parameters.
- [ ] edit main so only compute plots for user ask.
- [ ] How to batch do companies for a gicen start date.
- [ ] For a give ticker want add features to compare against others in industry.
- [ ] Save report.py as {ticker}_{start_date}_report.py
- [ ] Add title to markdown report i.e. ticker

### Remember

If new techical indicator is added to the stock data, it will need to be added to the app.
- [ ] Modularise (app: generate_markdown_report) creation function to allow optional parameters.

### Done:

- [X] Fix Close price to adjusted price
- [X] Clean markdown notes to standard format
- [X] edit markdown printer in app.py so that it shows images.
- [X] Edit user input to allow for the options to show specific outputs (e.g. only macd and rsi)

### Notes

- [ ] (seperate tool) Stock sentiments analysis grabber.