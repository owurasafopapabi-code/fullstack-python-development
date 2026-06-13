def interpret_result(result_value):
    if result_value < 70:
        return "Low"
    elif 70 <= result_value <= 110:
        return "Normal"
    else:
        return "High"
    

samples = []

low_count = 0
normal_count = 0
high_count = 0

number_of_sample_records = int(input("How many sample records do you want to enter?: "))

for sample_record in range(1, number_of_sample_records + 1):
    sample_id = input("Enter sample ID: ")
    patient_name = input("Enter patient name: ")
    test_name = input("Enter test name: ")
    result_value = float(input("Enter result value: "))
    interpretation = interpret_result(result_value)
    if interpretation == "Low":
        low_count = low_count + 1
    elif interpretation == "Normal":
        normal_count = normal_count + 1
    elif interpretation == "High":
        high_count = high_count + 1


    sample = {
        "sample_id": sample_id,
        "patient_name": patient_name,
        "test_name": test_name,
        "result_value": result_value,
        "interpretation": interpretation
    }

    samples.append(sample)
    print()


# Displaying all sample records
print("All Sample Records")
for index, each_sample in enumerate(samples, start=1):
    print()
    print(f"Sample {index}")
    print(f"Sample ID: {each_sample['sample_id']}")
    print(f"Patient Name: {each_sample['patient_name']}")
    print(f"Test Name: {each_sample['test_name']}")
    print(f"Result Value: {each_sample['result_value']}")
    print(f"Interpretation: {each_sample['interpretation']}")

print()
# Filtering records by interpretation
value_filter = input("Enter interpretation to filter by Low/Normal/High: ").title()

value_found = False

print(f"{value_filter} records")
for each_sample in samples:
    if each_sample['interpretation'] == value_filter:
        print(f"Sample ID: {each_sample['sample_id']}")
        print(f"Patient Name: {each_sample['patient_name']}")
        print(f"Test Name: {each_sample['test_name']}")
        print(f"Result Value: {each_sample['result_value']}")
        print(f"Interpretation: {each_sample['interpretation']}")
        print()

        value_found = True

if value_found == False:
    print("No matching records found.")


# Filtering records by searching for a particular sample ID
search_filter = input("Enter sample ID to search: ").title()

search_found = False

print()
for each_sample in samples:
    if each_sample['sample_id'] == search_filter:
        print(f"Sample ID: {each_sample['sample_id']}")
        print(f"Patient Name: {each_sample['patient_name']}")
        print(f"Test Name: {each_sample['test_name']}")
        print(f"Result Value: {each_sample['result_value']}")
        print(f"Interpretation: {each_sample['interpretation']}")
        print()

        search_found = True

if search_found == False:
    print("Sample not found.")


# Displaying counts on low/normal/high
print("Sample Record Summary")
print(f"Total Samples: {number_of_sample_records}")
print(f"Low Samples: {low_count}")
print(f"Normal Samples: {normal_count}")
print(f"High Samples: {high_count}")