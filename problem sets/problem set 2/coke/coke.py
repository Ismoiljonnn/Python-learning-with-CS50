def main():
  amount_due = 50

  while amount_due > 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))

    if coin in [25, 10, 5]:
      amount_due -= coin
    
  change_oved = abs(amount_due)
  print(f"Change Owed: {change_oved}")

main()