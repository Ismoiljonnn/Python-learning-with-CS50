def main():
  text = input("Input: ")
  result = ""

  vowels = "aeiouAEIOU"

  for char in text:
    if char not in vowels:
      result += char

  print("Output: ", result)

main()