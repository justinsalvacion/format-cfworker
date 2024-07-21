import re

def format_html_for_cloudflare(html_code):
    formatted_html = html_code.replace('`', '\\`')
    formatted_html = formatted_html.replace('\\', '\\\\')
    formatted_html = re.sub(r'(["\'])', r'\\\1', formatted_html)
    
    return formatted_html

# Change the following path according to your requirement :
input_path = r'C:\temp\index.html'
output_path = r'C:\temp\index-format.html'

with open(input_path, 'r', encoding='utf-8') as file:
    html_code = file.read()

formatted_html = format_html_for_cloudflare(html_code)

with open(output_path, 'w', encoding='utf-8') as file:
    file.write(formatted_html)

