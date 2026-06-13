def get_interpretation(result_value):
    
    if result_value < 70:
        return "Low"
    if 70 <= result_value <= 110:
        return "Normal"
    if result_value > 110:
        return "High"
    

sample_id = input("Enter sample id: ")
patient_name = input("Enter patient name: ")
test_name = input("Enter test name: ")
result_value = float(input("Enter result value: "))


sample = {
    "sample_id": sample_id,
    "patient_name": patient_name,
    "test_name": test_name,
    "result_value": result_value,
    "interpretation": get_interpretation(result_value)
}

print()
print("Sample Record")
print(f"Sample ID: {sample['sample_id']}")
print(f"Patient Name: {sample['patient_name']}")
print(f"Test Name: {sample['test_name']}")
print(f"Result Value: {sample['result_value']}")
print(f"Interpretation: {sample['interpretation']}")