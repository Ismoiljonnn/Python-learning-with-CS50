def main():
  student = get_student()
  print(f"{student[0]} from {student[1]}")


def get_student():
  student = {}
  student["name"] = input("Name: ")
  student["house"] = input("House: ")
  return student


if __name__ == "__main__":
  main()