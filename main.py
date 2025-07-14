from stats import get_book_text, words_num, count_characters, print_report
import sys

def main():
    if len(sys.argv) == 2:
        file_contents = get_book_text(sys.argv[1])
        characters_dic = count_characters(file_contents)
        sorted_item = print_report(characters_dic)
        total_words = words_num(file_contents)

        print(f"============ BOOKBOT ============\nAnalyzing book found at books/frankenstein.txt...\n----------- Word Count ---------\nFound {total_words} total words\n--------- Character Count -------")
        for i in range(0, len(sorted_item)):
            a = sorted_item[i]["char"]
            b = sorted_item[i]["num"]
            print(f"{a}: {b}")    
        print("============= END ===============")
    elif len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()


