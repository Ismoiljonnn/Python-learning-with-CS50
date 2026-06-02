def main():
  word = input("Input: ")
  print(f"Output: {shorten(word)}")


def shorten(word):
  result = ""

  for letter in word:
    if letter.lower() not in ['a', 'e', 'i', 'o', 'u', 'o']:
      result += letter
  return result

if __name__ == "__main__":
  main()