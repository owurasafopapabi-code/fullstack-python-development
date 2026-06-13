def read_file(file_name):
    record_count = 0

    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()

    print("Saved Sample Records")
    print()

    for line in lines:
        if line.strip() == "Sample Record":
            record_count = record_count + 1
        print(line.strip())
    print(f"Total Sample Records: {record_count}")


read_file("sample_records.txt")
