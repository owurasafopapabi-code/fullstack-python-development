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
            print("Wrong input. Field must be a numeric value.")
    

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
    print("Sample saved to JSON successfully.")


def load_json_to_dictionary(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        loaded_sample = json.load(file)
    print()
    print("Loaded Sample Record")
    return loaded_sample


def display_sample_from_json_to_dictionary(loaded_sample):
    print(f"Sample ID: {loaded_sample['sample_id']}")
    print(f"Patient Name: {loaded_sample['patient_name']}")
    print(f"Test Name: {loaded_sample['test_name']}")
    print(f"Result Value: {loaded_sample['result_value']}")
    print(f"Interpretation: {loaded_sample['interpretation']}")


def main():
    file_name = "sample.json"

    sample = collect_sample()

    save_to_json(file_name, sample)
    
    dictionary_file = load_json_to_dictionary(file_name)
    display_sample_from_json_to_dictionary(dictionary_file)
    


if __name__ == "__main__":
    main()