months = [
  "January", "February", "March", "April", "May", "June",
  "July", "August", "September", "October", "November", "December"
]

def main():
  while True:
    date = input("Date: ").strip()

    try:
      if "/" in date:
        month, day, year = date.split("/")
        month = int(month)
        day = int(day)
        year = int(year)

        if 1 <= month <= 12 and 1 <= day <= 31:
          print(f"{year}-{month:02d}-{day:02d}")
          break

      else:
        if "," not in date:
          continue

        parts = date.replace(",", "").split()

        if len(parts) == 3:
          month_name, day_str, year_str = parts

          if month_name in months:
            month = months.index(month_name) + 1
            day = int(day_str)
            year = int(year_str)

            if 1 <= day <= 31:
              print(f"{year}-{month:02d}-{day:02d}")
              break

    except ValueError:
      pass

main()