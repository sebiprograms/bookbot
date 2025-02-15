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

def report(text, choice="default"):
  chars = {}
  for key in text.lower():
    if (key.isalpha()) & (key not in chars) & (key != ' '):
      chars[key] = 0
    if (key.isalpha()) & (key != ' '):
      chars[key] += 1
  sorted_report = sorted(chars.items())
  if choice == "default":
    for key, value in sorted_report:
      print(f"The '{key}' character was found {value} times")
  else:
    print(sorted_report)
    

def main():
  with open(path_to_file) as f:
    file_contents = f.read()
    #print(file_contents)
    #wordcount(file_contents)
    #charcount(file_contents)
    report(file_contents)

__name__ == '__main__' 

main()


