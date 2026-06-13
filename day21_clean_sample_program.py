def interpret_result(result_value):
    if result_value < 70:
        return "Low"
    elif 70 <= result_value <= 110:
        return "Normal"
    else:
        return "High"
    

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
    
    print("Sample Record")

    print(f"Sample ID: {sample['sample_id']}")
    print(f"Patient Name: {sample['patient_name']}")
    print(f"Test Name: {sample['test_name']}")
    print(f"Result Value: {sample['result_value']}")
    print(f"Interpretation: {sample['interpretation']}")


def main():
    sample = collect_sample()

    display_sample(sample)


if __name__ == "__main__":
    main()