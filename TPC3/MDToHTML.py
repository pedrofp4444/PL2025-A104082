import re

def markdown_to_html(markdown_text):
    lines = markdown_text.split('\n')
    html = []
    list_buffer = []

    def process_inline(text):
        # Bold
        text = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', text)
        # Italic
        text = re.sub(r'\*(.*?)\*', r'<i>\1</i>', text)
        # Images (process before links to avoid conflicts)
        text = re.sub(r'!\[([^\]]*?)\]\(([^\)]*?)\)', r'<img src="\2" alt="\1"/>', text)
        # Links
        text = re.sub(r'\[([^\]]*?)\]\(([^\)]*?)\)', r'<a href="\2">\1</a>', text)
        return text

    for line in lines:
        # Headers
        header = re.match(r'^\s*(#+)\s*(.*)', line)
        if header:
            level = len(header.group(1))
            content = header.group(2).strip()
            processed = process_inline(content)
            html.append(f"<h{level}>{processed}</h{level}>")
            if list_buffer:
                html.append("<ol>")
                html.extend([f"<li>{item}</li>" for item in list_buffer])
                html.append("</ol>")
                list_buffer = []
            continue
        
        list_item = re.match(r'^\s*(\d+)\.\s*(.*)', line)
        if list_item:
            processed_content = process_inline(list_item.group(2).strip())
            list_buffer.append(processed_content)
            continue
        
        if list_buffer:
            html.append("<ol>")
            html.extend([f"<li>{item}</li>" for item in list_buffer])
            html.append("</ol>")
            list_buffer = []
        
        processed_line = process_inline(line)
        html.append(processed_line)
    
    if list_buffer:
        html.append("<ol>")
        html.extend([f"<li>{item}</li>" for item in list_buffer])
        html.append("</ol>")
    
    return '\n'.join(html)

markdown_input = """
# Header
**Bold** and *italic* text
1. First item
2. Second item
3. Third item
[Link](http://example.com) and ![Image](http://image.com)
"""
result = markdown_to_html(markdown_input.strip())

with open('output.html', 'w') as f:
    f.write(result)
