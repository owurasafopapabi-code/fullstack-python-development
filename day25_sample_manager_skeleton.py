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
        
        print("This field cannot be empty.")


def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
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


def display_sample(sample):
    print("Sample Record")
    print("-------------")
    print(f"Sample ID: {sample['sample_id']}")
    print(f"Patient Name: {sample['patient_name']}")
    print(f"Test Name: {sample['test_name']}")
    print(f"Result Value: {sample['result_value']}")
    print(f"Interpretation: {sample['interpretation']}")


def add_sample(samples):
    sample = collect_sample()
    samples.append(sample)
    print("Sample added successfully.")
    print()


def view_samples(samples):
    if not samples:
        print("No samples available.")
        print()
        return
    
    print("All Sample Records")
    print()
    
    for sample in samples:
        display_sample(sample)
        print()
    print()


def search_sample(samples):
    sample_id = get_non_empty_input("Enter sample ID to search: ")

    print()
    print(f"Searching for sample ID {sample_id}")

    value_found = False

    for sample in samples:
        if sample['sample_id'] == sample_id:
            print("Sample Found")
            display_sample(sample)
            value_found = True

    if value_found == False:
        print("Sample not found.")

    print()

    return True


def show_menu():
    print("Sample Manager Menu")
    print("-------------------")
    print("1. Add sample")
    print("2. View samples")
    print("3. Search sample")
    print("4. Exit")


def handle_menu_choice(choice, samples):
    if choice == "1":
        add_sample(samples)
    elif choice == "2":
        view_samples(samples)
    elif choice == "3":
        search_sample(samples)
    elif choice == "4":
        print("Goodbye.")
        return False
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")

    return True


def main():
    samples = []

    while True:
        show_menu()

        choice = get_non_empty_input("Enter your choice: ")
        print()

        should_continue = handle_menu_choice(choice, samples)

        if should_continue == False:
            break
    print()

if __name__ == "__main__":
    main()