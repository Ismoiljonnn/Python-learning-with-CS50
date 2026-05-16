def convert(text):
  matn = text.replace(":)", "🙂").replace(":(", "🙁")
  return matn

def main():
  msg = input()
  result = convert(msg)
  print(result)

main()