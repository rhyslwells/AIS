import subprocess

# Define the paths and options
md_path = 'markdown.md'
pdf_path = 'output.pdf'
resource_path = '.'  # Assuming resources are in the current directory

# Additional options for minimal margins and full page
pandoc_options = [
    'pandoc',
    md_path,
    '-o', pdf_path,
    '--resource-path', resource_path,
    '--variable', 'geometry:margin=1cm',  # Set minimal margins
    '--pdf-engine=pdflatex'  # Use pdflatex for better control over PDF output
]

# Run the pandoc command
subprocess.run(pandoc_options)

print("Complete")