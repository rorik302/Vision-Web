def generate_content(blocks):
    content = ''
    for block in sorted(combine_blocks(blocks), key=lambda bl: bl.sorting):
        content += ''.join(block.template)

    return content


def combine_blocks(qs_list):
    bl = []
    for qs in qs_list:
        [bl.append(item) for item in qs]
    return bl
