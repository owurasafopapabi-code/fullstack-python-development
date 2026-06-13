samples = [
    {
        "sample_id": "S001",
        "patient_name": "Ama Mensah",
        "test_name": "Fasting Blood Sugar",
        "result_value": 95.0,
        "interpretation": "Normal"
    },
    {
        "sample_id": "S002",
        "patient_name": "Kojo Boateng",
        "test_name": "Fasting Blood Sugar",
        "result_value": 65.0,
        "interpretation": "Low"
    },
    {
        "sample_id": "S003",
        "patient_name": "Abena Owusu",
        "test_name": "Fasting Blood Sugar",
        "result_value": 120.0,
        "interpretation": "High"
    },
    {
        "sample_id": "S004",
        "patient_name": "Kwadwo Safo",
        "test_name": "Fasting Blood Sugar",
        "result_value": 100.0,
        "interpretation": "Normal"
    }
]


value_filter = input("Enter interpretation to filter by Low/Normal/High: ").title()

print()
print(f"{value_filter} Results")
print()

value_found = False

for sample in samples:
    if sample["interpretation"] == value_filter:
        print(f"Sample ID: {sample['sample_id']}")
        print(f"Patient Name: {sample['patient_name']}")
        print(f"Test Name: {sample['test_name']}")
        print(f"Result Value: {sample['result_value']}")
        print(f"Interpretation: {sample['interpretation']}")
        print()
        value_found = True

if value_found == False:
    print("No matching records found.")


search_filter = input("Enter sample ID to search: ")

search_found = False

for sample in samples:
    if sample["sample_id"] == search_filter:
        print()
        print("Sample Search Result")
        print(f"Sample ID: {sample['sample_id']}")
        print(f"Patient Name: {sample['patient_name']}")
        print(f"Test Name: {sample['test_name']}")
        print(f"Result Value: {sample['result_value']}")
        print(f"Interpretation: {sample['interpretation']}")
        print()
        search_found = True

if search_found == False:
    print("Sample not found.")

    