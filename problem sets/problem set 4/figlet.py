import sys
import random
from pyfiglet import Figlet

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
  selected_font = random.choice(fonts)
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
  if sys.argv[2] in fonts:
      selected_font = sys.argv[2]
  else:
      sys.exit("Invalid usage")
else:
  sys.exit("Invalid usage")

figlet.setFont(font=selected_font)

text = input("Input: ")
print("Output:")
print(figlet.renderText(text))