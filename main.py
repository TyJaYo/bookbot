def main():
  book_path = 'books/frankenstein.txt'
  text = get_book_text(book_path)
  word_count = count_words(text)
  char_counts = count_characters(text)
  print_report(book_path, word_count, char_counts)

def print_report(path, word_count, char_counts):
  print(f"--- Report on {path} ---")
  print(f"Word count: ~{word_count}\n")
  print("Character counts:")
  char_counts = {char: count for char, count in char_counts.items() if char.isalpha()}
  char_counts = dict(sorted(char_counts.items(), key=lambda item: item[1], reverse=True))
  for char, count in char_counts.items():
    print(f"{char}: {count}")
  print("--- End report ---")

def get_book_text(path):
  with open(path) as f:
    file_contents = f.read()
  return file_contents

def count_words(text):
  return len(text.split())

def count_characters(text):
  chars = {}
  for char in text:
    char = char.lower()
    if char in chars:
      chars[char] += 1
    else:
      chars[char] = 1
  return dict(sorted(chars.items()))

main()
