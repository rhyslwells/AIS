Consider the following functions. I want to change this so that the user can specific which componets they want in the markdown report. There needs a way to parse the arguements and a modular way to add to markdown_content:

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
    markdown_content =f"""

{price_content}
![Alt text](imgs/adjusted_close.png)

<!-- pagebreak -->

{volume_content}
![Alt text](imgs/volume.png)

<!-- pagebreak -->

{moving_average_content}
![Alt text](imgs/moving_average.png)

<!-- pagebreak -->

{bollinger_bands_content}
![Alt text](imgs/bollinger_bands.png)

<!-- pagebreak -->


{macd_content}
![Alt text](imgs/macd.png)

<!-- pagebreak -->


{rsi_content}
![Alt text](imgs/RSI.png)

<!-- pagebreak -->

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

    generate_markdown_report(ticker)

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
        mrk_pdf_converter(ticker)
    else:
        print(f"Skipping PDF generation for {ticker}.")

    print(f"Report for {ticker} generated successfully!")

if __name__ == "__main__":
    main()