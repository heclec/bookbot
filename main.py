def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    sort_chars(count_characters(text), book_path, num_words)

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_characters(text):
    char_counts = {}
    lower_case = text.lower()
    for char in lower_case:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

def sort_chars(char_counts, book_path, num_words):
    print (f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")

    char_list = [{'char': char, 'count': count} for char, count in char_counts.items()]
    char_list.sort(reverse=True, key=lambda x: x['count'])
    for c in char_list:
        if c['char'].isalpha():
            print (f"The '{c['char']}' character was found {c['count']} times.")
    print ("--- End report ---")

main()