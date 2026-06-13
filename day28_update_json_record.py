import json

def interpret_result(result_value):
    if result_value < 70:
        return "Low"
    elif 70 <= result_value <= 110:
        return "Normal"
    else:
        return "High"
    

def load_samples(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            loaded_sample = json.load(file)
        return loaded_sample
    except FileNotFoundError:
        print("File not found.")
        return []


def save_samples(file_name, samples):
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(samples, file, indent=4)


def display_sample(sample):
    print("Sample Record")
    print(f"Sample ID: {sample['sample_id']}")
    print(f"Patient Name: {sample['patient_name']}")
    print(f"Test Name: {sample['test_name']}")
    print(f"Result Value: {sample['result_value']}")
    print(f"Interpretation: {sample['interpretation']}")
    print("-" * 30)


def get_non_empty_input(prompt):
    while True:
        value = input(prompt).strip()

        if value != "":
            return value

        print("Field cannot be empty.")


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt).strip())
            return value
        except ValueError:
            print("Invalid input. Input must be a numeric value.")


def update_sample_results(samples):
    search_id = get_non_empty_input("Enter sample ID to update: ")
    print()

    found = False

    for sample in samples:
        if sample['sample_id'] == search_id:
            print("Current Sample Record")
            print("---------------------")
            display_sample(sample)
            print()

            new_result_value = get_float_input("Enter new result value: ")
            sample['result_value'] = new_result_value
            sample['interpretation'] = interpret_result(new_result_value)
            found = True
            print("Sample updated successfully.")

    if found == False:
        print("Sample not found.")


def main():
    file_name = "samples.json"

    samples = load_samples(file_name)

    update_sample_results(samples)
    print()

    save_samples(file_name, samples)

    print("Updated Sample Records")
    print()
    for sample in samples:
        display_sample(sample)


if __name__ == "__main__":
    main()