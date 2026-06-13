def interpret_result(result_value):
    if result_value < 70:
        return "Low"
    elif 70 <= result_value <= 110:
        return "Normal"
    else:
        return "High"


def print_separator():
    print("-" * 30)


def collect_sample():
    sample_id = input("Enter sample ID: ")
    patient_name = input("Enter patient name: ")
    test_name = input("Enter test name: ")
    result_value = float(input("Enter the result value: "))

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
    
    print(f"Sample ID: {sample['sample_id']}")
    print(f"Patient Name: {sample['patient_name']}")
    print(f"Test Name: {sample['test_name']}")
    print(f"Result Value: {sample['result_value']}")
    print(f"Interpretation: {sample['interpretation']}")
    print_separator()


def main():

    samples = []

    number_of_samples = int(input("How many samples do you want to enter? "))

    for number_of_sample in range(1, number_of_samples + 1):
        sample = collect_sample()
        print()
        samples.append(sample)

    print("All Sample Records")
    print()
    for each_sample in samples:
        display_sample(each_sample)


if __name__ == "__main__":
    main()