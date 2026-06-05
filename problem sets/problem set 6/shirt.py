import sys
import os
from PIL import Image, ImageOps

def main():
  if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
  if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
  
  input_ext = os.path.splitext(sys.argv[1])[1].lower()
  output_ext = os.path.splitext(sys.argv[2])[1].lower()

  valid_exts = [".jpg", ".jpeg", ".png"]
  if input_ext not in valid_exts or output_ext not in valid_exts:
    sys.exit("Invalid output")

  if input_ext != output_ext:
    sys.exit("Input and output have different extensions")

  try:
    with Image.open(sys.argv[1]) as input_image:
      shirt = Image.open("shirt.png")
      size = shirt.size

      fitted_image = ImageOps.fit(input_image, size)
      fitted_image.paste(shirt, shirt)
      fitted_image.save(sys.argv[2])

  except FileNotFoundError:
    sys.exit("Input does not exist")

if __name__ == "__main__":
  main()