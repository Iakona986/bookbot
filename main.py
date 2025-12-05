import sys
from stats import wordcount
from stats import letter_count
from stats import sorted_count

def get_book_text(path):
    with open(path) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        file_path = sys.argv[1]
        book_content = get_book_text(file_path)
        word_count = wordcount(book_content)
        letters = letter_count(book_content)
        sort_count = sorted_count(letters)


        print ("============ BOOKBOT ============")
        print (f"Analyzing book found at {file_path}...")
        print ("----------- Word Count ----------")
        print (f"Found {word_count} total words")
        print ("--------- Character Count -------")
        for item in sort_count:
            char = item["char"]
            count = item["num"]
            print(f"{char}: {count}")
        print ("============= END ===============")

main()
