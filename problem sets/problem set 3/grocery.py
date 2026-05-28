def main():
  grocery_list= {}
  
  while True:
    try:
      item = input().strip().upper()

      if not item:
        continue
      
      if item in grocery_list:
        grocery_list[item] += 1
      else:
        grocery_list[item] = 1

    except EOFError:
      print()

      for sorted_item in sorted(grocery_list.keys()):
        print(f"{grocery_list[sorted_item]} {sorted_item}")
      break

main()