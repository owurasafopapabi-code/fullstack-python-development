def interpret_result(result_value):
    """Returns low, normal, or high when result value is not in a range."""
    if result_value < 70:
        return "Low"
    elif 70 <= result_value <= 110:
        return "Normal"
    else:
        return "High"
    

def get_non_empty_input(prompt):
    """Returns string that is not empty."""
    while True:
        value = input(prompt).strip()

        if value != "":
            return value
        
        print("This field cannot be empty.")


def get_float_input(prompt):
    """Keeps asking until the user enters a valid number."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a numeric value.")


def collect_sample():
    """Returns a dictionary of validated user inputs."""
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
    """Prints out sample record"""
    print("Sample Record")

    print(f"Sample ID: {sample['sample_id']}")
    print(f"Patient Name: {sample['patient_name']}")
    print(f"Test Name: {sample['test_name']}")
    print(f"Result Value: {sample['result_value']}")
    print(f"Interpretation: {sample['interpretation']}")


def main():
    sample = collect_sample()
    print()
    display_sample(sample)


if __name__ == "__main__":
    main()