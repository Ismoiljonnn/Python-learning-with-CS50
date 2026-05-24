x = input("what is the Answer to the Great Question if Life, the universe, and Everything? ")

answer = x.strip().lower()

if answer == "42" or answer == "forty-two" or answer == "forty two":
  print("Yes")
else:
  print("No")