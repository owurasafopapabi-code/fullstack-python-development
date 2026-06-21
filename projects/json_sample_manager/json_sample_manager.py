# JSON Sample Manager
# A beginner command-line application for managing laboratory sample records using JSON storage.


import json
from pathlib import Path

def interpret_result(result_value):
    """Returns low, normal, or high for result values of patient."""
    if result_value < 70:
        return "Low"
    elif 70 <= result_value <= 110:
        return "Normal"
    else:
        return "High"
    

def get_non_empty_input(prompt):
    """Ensures user input field is not empty."""
    while True:
        value = input(prompt).strip()
        if value != "":
            return value
        print("Field must not be empty.")


def get_float_input(prompt):
    """Ensures user enters a valid number."""
    while True:
        try:
            value = float(input(prompt).strip())
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def load_samples(file_name):
    """
    Loads sample from JSON file and returns a list of dictionary. 
    If file does not exist, it returns empty list.
    """
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            loaded_samples = json.load(file)
        return loaded_samples
    except FileNotFoundError:
        print("No file found.")
        return []


def save_samples(file_name, samples):
    """Saves the full list of sample dictionaries to JSON."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(samples, file, indent=4)


def collect_sample():
    """Takes patient sample details, create and return a sample dictionary."""
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


def print_separator():
    print("-" * 30)


def display_sample(sample):
    """Displays one sample record clearly."""
    print("Sample Record")
    print("-------------")
    print(f"Sample ID: {sample['sample_id']}")
    print(f"Patient Name: {sample['patient_name']}")
    print(f"Test Name: {sample['test_name']}")
    print(f"Result Value: {sample['result_value']}")
    print(f"Interpretation: {sample['interpretation']}")
    print_separator()


def add_sample(samples, file_name):
    """Calls the collect_sample() and append the sample to samples, and save the updated list to JSON."""
    sample = collect_sample()
    samples.append(sample)
    save_samples(file_name, samples)
    print("Sample added successfully.")
    print()


def view_samples(samples):
    """Displays all sample records except no sample exist."""
    if not samples:
        print("No samples available.")
        print()
        return
    print("All Sample Records")
    for sample in samples:
        display_sample(sample)
        print()
    print()


def search_sample(samples):
    """Searches for sample ID and displays the sample."""
    search_id = get_non_empty_input("Enter sample ID to search: ")
    found = False
    for sample in samples:
        if sample["sample_id"] == search_id:
            print("Sample Found")
            display_sample(sample)
            found = True
    if found == False:
        print("Sample not found.")
    print()


def filter_samples_by_interpretation(samples):
    """Filters and displays all matching records."""
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
    print()


def update_sample(samples, file_name):
    """Finds a sample by ID, updates its value, recalculates status, and saves to JSON."""
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
            sample["result_value"] = new_result_value

            sample["interpretation"] = interpret_result(new_result_value)

            save_samples(file_name, samples)
            found = True
            print("Sample updated successfully.")

    if found == False:
        print("Sample not found.")
    print()


def show_menu():
    """Displays menu for JSON Sample Manager."""
    print("JSON Sample Manager")
    print("-------------------")
    print("1. Add sample")
    print("2. View samples")
    print("3. Search sample")
    print("4. Filter samples")
    print("5. Update sample result")
    print("6. Exit")


def handle_menu_choice(choice, samples, file_name):
    if choice == "1":
        add_sample(samples, file_name)
    elif choice == "2":
        view_samples(samples)
    elif choice == "3":
        search_sample(samples)
    elif choice == "4":
        filter_samples_by_interpretation(samples)
    elif choice == "5":
        update_sample(samples, file_name)
    elif choice == "6":
        print("Goodbye.")
        return False
    else:
        print("Invalid choice. Please select 1, 2, 3, 4, 5, or 6.")
    
    return True


def main():
    project_folder = Path(__file__).resolve().parent
    file_name = project_folder / "samples.json"
    
    samples = load_samples(file_name)

    while True:
        show_menu()
        choice = get_non_empty_input("Enter a choice to choose from the menu: ")
        print()

        should_continue = handle_menu_choice(choice, samples, file_name)

        if should_continue == False:
            break
    print()


if __name__ == "__main__":
    main()