samples = []

def get_interpretation(result_value):
    if result_value < 70:
        return "Low"
    elif 70 <= result_value <= 110:
        return "Normal"
    else:
        return "High"

number_of_sample_records = int(input("How many sample records do you want to enter?: "))

for sample_record in range(1, number_of_sample_records + 1):
    sample_id = input("Enter sample ID: ")
    patient_name = input("Enter patient name: ")
    test_name = input("Enter test name: ")
    result_value = float(input("Enter result value: "))

    interpretation = get_interpretation(result_value)
    print()

    sample = {
        "sample_id": sample_id,
        "patient_name": patient_name,
        "test_name": test_name,
        "result_value": result_value,
        "interpretation": get_interpretation(result_value)
    }

    samples.append(sample)


print("Sample Records")

for index, record in enumerate(samples, start=1):
    print(f"Sample {index}")
    print(f"Sample ID: {record['sample_id']}")
    print(f"Patient Name: {record['patient_name']}")
    print(f"Test Name: {record['test_name']}")
    print(f"Result Value: {record['result_value']}")
    print(f"Interpretation: {record['interpretation']}")
    print()
