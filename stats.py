def get_num_words(book):
    words = book.split()
    return len(words)
def get_character_count(book):
    letters = {}
    lower_words = book.lower()
    for ch in lower_words:
        if ch not in letters:
            letters[ch] = 1
        else:
            letters[ch] += 1
    return letters
def sort_on(items):
    return items["num"]
def sort_character_count(counts):
    organized = []
    for k, v in counts.items():
        if k.isalpha():
            item = {"char": k, "num": v}
            organized.append(item)
    organized.sort(reverse=True, key=sort_on)
    return organized
