"""
Generator implementation.
"""


def read_and_filter(file, words):
    """returns generator with found sentences"""
    if isinstance(file, str):
        file = open(file, 'r', encoding='utf-8')

    with file as file_handle:
        for line in file_handle:
            line = line.strip()
            if any(word.lower() in line.lower().split() for word in words):
                yield line
