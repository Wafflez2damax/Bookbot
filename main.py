import sys
from stats import get_num_words, get_character_count, sort_character_count
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
syspath = sys.argv[1]
def get_book_text(text):
    with open(text) as f:
        return f.read()
book = get_book_text(syspath)
def main():
    characters = get_character_count(book)
    char_list = sort_character_count(characters)
    count = get_num_words(book)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {syspath}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for item in char_list:
      ch = item["char"]
      if ch.isalpha():
        print(f"{ch}: {item['num']}")
    print("============= END ===============")
if __name__ == "__main__":
    main()
