def interpret_result(result_value):
    if result_value < 70:
        return "Low"
    elif 70 <= result_value <= 110:
        return "Normal"
    else:
        return "High"
    

sample_id = input("Enter sample ID: ")
patient_name = input("Enter patient name: ")
test_name = input("Enter test name: ")
result_value = float(input("Enter result value: "))

with open("sample_record.txt", "w", encoding="utf-8") as file:
    file.write("Sample Record\n")
    file.write(f"Sample ID: {sample_id}\n")
    file.write(f"Patient Name: {patient_name}\n")
    file.write(f"Test Name: {test_name}\n")
    file.write(f"Result Value: {result_value}\n")
    file.write(f"Interpretation: {interpret_result(result_value)}\n")
    file.write("-" * 30 + "\n")

print()
print("Sample record saved successfully")

with open("sample_record.txt", "r") as file:
    content = file.read()

print()
print("Saved Sample Record")
print(content)