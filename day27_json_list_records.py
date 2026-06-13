import json

def interpret_result(result_value):
    if result_value < 70:
        return "Low"
    elif 70 <= result_value <= 110:
        return "Normal"
    else:
        return "High"


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value != "":
            return value
        
        print("Field must not be empty.")


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def get_int_input(prompt):
    while True:
        try:
            value = int(input(prompt).strip())
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def collect_sample():
    sample_id = get_non_empty_input("Enter sample ID: ")
    patient_name = get_non_empty_input("Enter patient name: ")
    test_name = get_non_empty_input("Enter test name: ")
    result_value = get_float_input("Enter result value: ")
    interpretation = interpret_result(result_value)

    sample = {
        "sample_id": sample_id,
        "patient_name": patient_name,
        "test_name": test_name,
        "result_value": result_value,
        "interpretation": interpretation
    }

    return sample


def save_to_json(file_name, sample):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(sample, file, indent=4)
    print()


def load_json_to_dictionary(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        loaded_samples = json.load(file)
    print()
    print("Loaded Sample Records")
    print()
    return loaded_samples


def display_sample(sample):
    print("Sample Record")
    print(f"Sample ID: {sample['sample_id']}")
    print(f"Patient Name: {sample['patient_name']}")
    print(f"Test Name: {sample['test_name']}")
    print(f"Result Value: {sample['result_value']}")
    print(f"Interpretation: {sample['interpretation']}")
    print("-" * 30)


def main():

    file_name = "samples.json"

    samples = []

    number_of_sample_records = get_int_input("How many sample records do you want to enter? ")

    for sample_record in range(1, number_of_sample_records + 1):
        sample = collect_sample()

        samples.append(sample)

    save_to_json(file_name, samples)
    print("Sample records saved to JSON successfully.")

    loaded_samples = load_json_to_dictionary(file_name)
    for sample in loaded_samples:
        display_sample(sample)


if __name__ == "__main__":
    main()