import argparse
import os
import yfinance as yf
import subprocess

def read_template(file_path):
    """Read the content from a markdown template file."""
    with open(file_path, 'r') as file:
        return file.read()

def mrk_pdf_converter(ticker):
    """Convert markdown report to PDF using Pandoc."""
    md_path = os.path.join('outputs', ticker, 'report.md')
    pdf_path = os.path.join('outputs', ticker, 'report.pdf')

    try:
        # Specify the resource path for Pandoc
        resource_path = os.path.join('outputs', ticker)
        
        # Additional options for minimal margins and full page
        pandoc_options = [
            'pandoc',
            md_path,
            '-o', pdf_path,
            '--resource-path', resource_path,
            '--variable', 'geometry:margin=1cm',  # Set minimal margins
            '--pdf-engine=pdflatex'  # Use pdflatex for better control over PDF output
        ]

        subprocess.run(pandoc_options)
        print(f"Report in markdown for {ticker} converted to PDF with minimal margins.")
    except FileNotFoundError:
        print("Pandoc is not installed or executable.")
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while generating PDF: {e}")

def generate_markdown_report(ticker, components):
    """Generate the markdown report for the given ticker with specified components."""
    # Dictionary mapping component names to their template file paths
    templates = {
        'price': ('template/markdown/price.md', '![Alt text](imgs/adjusted_close.png)'),
        'volume': ('template/markdown/volume.md', '![Alt text](imgs/volume.png)'),
        'moving_average': ('template/markdown/moving_average.md', '![Alt text](imgs/moving_average.png)'),
        'bollinger_bands': ('template/markdown/bollinger_bands.md', '![Alt text](imgs/bollinger_bands.png)'),
        'macd': ('template/markdown/macd.md', '![Alt text](imgs/macd.png)'),
        'rsi': ('template/markdown/RSI.md', '![Alt text](imgs/RSI.png)')
    }

    # Generate the markdown content
    markdown_content = ""
    for component in components:
        if component in templates:
            content, img_tag = templates[component]
            markdown_content += f"\n{read_template(content)}\n{img_tag}\n\n<!-- pagebreak -->\n"

    # Add a placeholder for Fundamental Indicators
    markdown_content += "\n## Fundamental Indicators (to be added later)\n"

    # Save markdown content to file
    output_path = f'outputs/{ticker}/report.md'
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w') as file:
        file.write(markdown_content)


def get_user_input():
    """Prompt the user for the ticker and components to include in the report."""
    default_ticker = "GOOGL"
    default_start_date = "2023-01-01"
    valid_components = ['price', 'volume', 'moving_average', 'bollinger_bands', 'macd', 'rsi']

    ticker = input(f"Enter the ticker symbol for the report (default: {default_ticker}): ").strip() or default_ticker
    start_date = input(f"Enter start date (YYYY-MM-DD, default: {default_start_date}): ").strip() or default_start_date
    
    print("Enter the components to include in the report (separated by commas):")
    print("Valid components: price, volume, moving_average, bollinger_bands, macd, rsi")
    components_input = input("Components (default: all): ").strip()
    
    if components_input:
        components = [component.strip() for component in components_input.split(',') if component.strip() in valid_components]
    else:
        components = valid_components

    if not components:
        print("No valid components selected. Using default components.")
        components = valid_components
    
    return ticker, start_date, components

def main():
    """Main function to execute the script."""
    ticker, start_date, components = get_user_input()

    skip_main = input("Skip generating component plots? (y/n): ").strip().lower() == 'y'
    if not skip_main:
        os.system(f"python src/main.py {ticker} {start_date}")

    generate_markdown_report(ticker, components)

    skip_pdf_generation = input("Skip PDF generation? (y/n): ").strip().lower() == 'y'
    if not skip_pdf_generation:
        mrk_pdf_converter(ticker)
    else:
        print(f"Skipping PDF generation for {ticker}.")

    print(f"Report for {ticker} generated successfully!")

if __name__ == "__main__":
    main()