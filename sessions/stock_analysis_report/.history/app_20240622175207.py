import argparse
import os
import yfinance as yf

def get_args():
    """Parse and return command-line arguments."""
    parser = argparse.ArgumentParser(description='Analyze a stock and generate a markdown report.')
    parser.add_argument('ticker', type=str, help='The stock ticker to analyze, e.g. GOOGL', nargs='?')
    args = parser.parse_args()
    
    if not args.ticker:
        args.ticker = input("Enter a stock ticker (e.g. GOOGL): ")
        if not args.ticker:
            args.ticker = 'GOOGL'
    
    return args.ticker

def get_start_date():
    """Prompt the user for a start date and return it."""
    start_date = input("Enter a start date (YYYY-MM-DD) (e.g. 2023-01-01): ")

    if not start_date:
        start_date = '2023-01-01'

    return start_date


def generate_markdown_report(ticker):
    """Generate the markdown report for the given ticker."""
    # Read the content from the markdown templates
    with open('template/markdown/price.md', 'r') as file:
        price_content = file.read()
    with open('template/markdown/moving_average.md', 'r') as file:
        moving_average_content = file.read()
    with open('template/markdown/bollinger_bands.md', 'r') as file:
        bollinger_bands_content = file.read()
    with open('template/markdown/macd.md', 'r') as file:
        macd_content = file.read()
    with open('template/markdown/RSI.md', 'r') as file:
        rsi_content = file.read()
    with open('template/markdown/volume.md', 'r') as file:
        volume_content = file.read()

    # Generate the markdown content
    markdown_content =
    f"""
    ## Price

    {price_content}

    ![Alt text](outputs/{ticker}/imgs/adjusted_close.png)

    ## Technical Indicators

    {moving_average_content}

    ![Alt text](outputs/{ticker}/imgs/moving_average.png)

    {bollinger_bands_content}

    ![Alt text](outputs/{ticker}/imgs/bollinger_bands.png)

    {macd_content}

    ![Alt text](outputs/{ticker}/imgs/macd.png)

    {rsi_content}

    ![Alt text](outputs/{ticker}/imgs/RSI.png)

    {volume_content}

    ![Alt text](outputs/{ticker}/imgs/volume.png)

    ## Fundamental Indicators (to be added later)
    """
    # Save markdown content to file


    with open(f'outputs/{ticker}/report.md', 'w') as file:
        file.write(markdown_content)


def main():
    """Main function to execute the script."""
    ticker = get_args()
    start_date = get_start_date()

    skip_main = False
    while True:
        choice = input("Skip main.py? (y/n): ")
        if choice.lower() == "y":
            skip_main = True
            break
        elif choice.lower() == "n":
            break
        else:
            print("Invalid input. Please enter y or n.")

    if not skip_main:
        os.system(f"python src/main.py {ticker} {start_date}")

    skip_pdf_generation = False
    while True:
        choice = input("Skip PDF generation? (y/n): ")
        if choice.lower() == "y":
            skip_pdf_generation = True
            break
        elif choice.lower() == "n":
            break
        else:
            print("Invalid input. Please enter y or n.")

    if not skip_pdf_generation:
        os.system(f"pandoc -o outputs/{ticker}/report.pdf outputs/{ticker}/report.md")

    print(f"Report for {ticker} generated successfully!")

if __name__ == "__main__":
    main()
