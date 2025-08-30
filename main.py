def get_book_text(path):
    with open(path) as f:
        return f.read()
def main():
    path = "books/frankenstein.txt"
    text = get_book_text(path)
    words = text.split()
    num_words = len(words)
    print(f"{num_words} words found in the document")
if __name__ == "__main__":
    main()
