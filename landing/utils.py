def generate_content(blocks):
    content = ''

    for block in blocks:
        content += ''.join(b.template for b in block)

    return content
