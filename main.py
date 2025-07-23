import sys
from stats import get_num_words
from stats import get_num_characters
from stats import show_reports

def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        return file_contents


def main():
   if len(sys.argv) < 2:
       print("Usage: python3 main.py <path_to_book>")
       sys.exit(1)
   content =  get_book_text(sys.argv[1])
   num_words = get_num_words(content)
   characters = get_num_characters(content)
#    print(f"{num_words} words found in the document")
#    print(characters)
  
   show_reports(characters, num_words)

  





main()

