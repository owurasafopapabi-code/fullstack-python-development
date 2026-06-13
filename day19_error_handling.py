try:
    result_value = float(input("Enter a result value: "))
    print(f"Result Value: {result_value}")
except ValueError:
    print("Invalid result value. Please enter a numeric value.")


file_name = input("Enter a file name: ")

try:
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.read()
    print()
    print("File Content")
    print(content)
except FileNotFoundError:
    print("File not found. Please check the file name and try again.")