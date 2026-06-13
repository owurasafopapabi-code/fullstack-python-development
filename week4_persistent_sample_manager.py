# Project Name: Persistent Sample Record Manager

def interpret_result(result_value):
    """Returns low, normal or high when a result value is received."""
    if result_value < 70:
        return "Low"
    elif 70 <= result_value <= 110:
        return "Normal"
    else:
        return "High"
    

def clear_file(file_name):
    with open(file_name, "w", encoding="utf-8") as file:
        file.write("")


def save_sample_record(file_name, sample_id, patient_name, test_name, result_value, interpretation):
    """Creates a file and save sample records of patient in persistent_sample_records.txt."""
    with open(file_name, "a", encoding="utf-8") as file:
        file.write("Sample Record\n")
        file.write(f"Sample ID: {sample_id}\n")
        file.write(f"Patient Name: {patient_name}\n")
        file.write(f"Test Name: {test_name}\n")
        file.write(f"Result Value: {result_value}\n")
        file.write(f"Interpretation: {interpretation}\n")
        file.write("-" * 30 + "\n")
    

def read_sample_records(file_name):
    """Reads sample records and count the number of records in the file."""
    records_count = 0

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            lines = file.readlines()

        print("\nSaved Sample Records")

        for line in lines:
            if line.strip() == "Sample Record":
                records_count = records_count + 1
            print(line.strip())

        print(f"\nTotal Sample Records: {records_count}")

    except FileNotFoundError:
        print("No saved sample records found.")


def main():

    file_name = "persistent_sample_records.txt"

    try:
        number_of_sample_records = int(input("How many sample records do you want to enter: "))
    except ValueError:
        print("Invalid Entry. Please enter a numeric value.")
        return

    clear_file(file_name)

    for sample_record in range(1, number_of_sample_records + 1):

        sample_id = input("Enter sample ID: ")
        patient_name = input("Enter patient name: ")
        test_name = input("Enter test name: ")

        try:
            result_value = float(input("Enter result value: "))
        except ValueError:
            print("Invalid result value. Please enter a numeric value.")
            continue

        interpretation = interpret_result(result_value)
        print()

        save_sample_record(file_name, sample_id, patient_name, test_name, result_value, interpretation)

    print("Sample records saved successfully.")
    read_sample_records(file_name)


if __name__ == "__main__":
    main()