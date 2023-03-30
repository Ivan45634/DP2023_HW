def lines_with_word(filename, words):
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line_words = line.strip().lower().split()
            if any(word.lower() in line_words for word in words):
                yield line.strip()
