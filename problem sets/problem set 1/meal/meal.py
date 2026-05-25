def main():
    time_input = input("What time is it? ").strip()

    converted_time = convert(time_input)

    if 7.0 <= converted_time <= 8.0:
        print("breakfast time")
    elif 12.0 <= converted_time <= 13.0:
        print("lunch time")
    elif 18.0 <= converted_time <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")

    return float(hours) + float(minutes) / 60.0

if __name__ == "__main__":
    main()
