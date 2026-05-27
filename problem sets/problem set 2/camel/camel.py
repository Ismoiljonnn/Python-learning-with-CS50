def main():
  camel = input("camelCase: ")
  snake = ""

  for char in camel:
    if char.isupper():
      snake += "_" + char.lower()
    else:
      snake += char
  
  print("snake_case:", snake)

main()