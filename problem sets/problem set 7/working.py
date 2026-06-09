import re
import sys

def main():
  print(convert(input("Hours: ")))

def convert(s):
  pattern = r"^(1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM) to (1[0-2]|[1-9])(?::([0-5][0-9]))? (AM|PM)$"
  
  match = re.search(pattern, s)
  if match:
      h1, m1, ap1, h2, m2, ap2 = match.groups()
      m1 = m1 if m1 else "00"
      m2 = m2 if m2 else "00"
      return f"{time_format(h1, m1, ap1)} to {time_format(h2, m2, ap2)}"
  
  raise ValueError

def time_format(h, m, ap):
  h = int(h)
  if ap == "PM" and h != 12:
      h += 12
  elif ap == "AM" and h == 12:
      h = 0
  return f"{h:02}:{m}"

if __name__ == "__main__":
  main()