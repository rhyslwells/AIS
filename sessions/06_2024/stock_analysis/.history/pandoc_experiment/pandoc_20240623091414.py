import subprocess

# Define the paths and options
md_path = 'markdown.md'
pdf_path = 'output.pdf'
resource_path = '.'  # Assuming resources are in the current directory

# Additional options for minimal margins and full page
# Additional options for improved styling
pandoc_options = [
    'pandoc',
    md_path,
    '-o', pdf_path,
    '--resource-path', resource_path,
    '--variable', 'geometry:margin=1.5cm',  # Set minimal margins
    '--variable', 'fontsize=11pt',  # Set font size
    # '--variable', 'linestretch=1.5',  # Set line spacing
    '--pdf-engine=pdflatex',  # Use pdflatex for better control over PDF output
    '--highlight-style', 'tango',  # Syntax highlighting style for code blocks
    # '--template', custom_template_path  # Use a custom LaTeX template
]

# Run the pandoc command
subprocess.run(pandoc_options)

print("Complete")