import json

def interpret_result(result_value):
    if result_value < 70:
        return "Low"
    elif 70 <= result_value <= 110:
        return "Normal"
    else:
        return "High"


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            return value
        except ValueError:
            print("Invalid input. Enter a numeric value.")


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value != "":
            return value
        print("Field must not be empty.")


def load_samples(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            loaded_samples = json.load(file)
        return loaded_samples
    except FileNotFoundError:
        print("File not found.")
        return []
    

def display_sample(sample):
    print()
    print("Sample Record")
    print(f"Sample ID: {sample['sample_id']}")
    print(f"Patient Name: {sample['patient_name']}")
    print(f"Test Name: {sample['test_name']}")
    print(f"Result Value: {sample['result_value']}")
    print(f"Interpretation: {sample['interpretation']}")
    print("-" * 30)


def search_sample_by_id(samples):
    search_id = get_non_empty_input("Enter sample ID to search: ")
    print()
    found = False
    for sample in samples:
        if sample["sample_id"] == search_id:
            print("Sample Found")
            display_sample(sample)
            found = True
    if found == False:
        print("Sample not found.")


def filter_sample_by_interpretation(samples):
    filter_value = get_non_empty_input("Enter interpretation to filter by Low/Normal/High: ").title()
    print()
    print(f"{filter_value} Sample Records")
    found = False
    for sample in samples:
        if sample["interpretation"] == filter_value:
            display_sample(sample)
            found = True
    if found == False:
        print("No matching records found.")


def main():
    file_name = "samples.json"
    samples = load_samples(file_name)

    search_sample_by_id(samples)

    filter_sample_by_interpretation(samples)


if __name__ == "__main__":
    main()