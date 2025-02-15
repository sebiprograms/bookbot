path_to_file = "books/frankenstein.txt"

def wordcount(text):
  words = text.split()
  print(len(words))

def charcount(text):
  chars = {}
  for key in text.lower():
    if key not in chars:
      chars[key] = 0
    chars[key] += 1
  print(chars)
    

def main():
  with open(path_to_file) as f:
    file_contents = f.read()
    print(file_contents)
    wordcount(file_contents)
    charcount(file_contents)

__name__ == '__main__' 

main()


