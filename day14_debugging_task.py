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
    }
]

search_id = input("Enter sample ID to search: ")

found = False

for sample in samples:
    if sample["sampleID"] == search_id:
        print("Sample Found")
        print(f"Sample ID: {sample['sample_id']}")
        print(f"Patient Name: {sample['patient_name']}")
        print(f"Test Name: {sample['test_name']}")
        print(f"Result Value: {sample['result_value']}")
        print(f"Interpretation: {sample['interpretation']}")
        found = True

if found == False:
    print("Sample not found.")