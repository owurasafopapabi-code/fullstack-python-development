def interpret_result(result_value):
    if result_value < 70:
        return "Low"
    elif 70 <= result_value <= 110:
        return "Normal"
    else:
        return "High"
    

number_of_sample_records = int(input("How many sample records do you want to enter?: "))

with open("sample_records.txt", "w", encoding="utf-8") as file:
    file.write("")
    
for sample_record in range(1, number_of_sample_records + 1):
    sample_id = input("Enter sample ID: ")
    patient_name = input("Enter patient name: ")
    test_name = input("Enter test name: ")
    result_value = float(input("Enter result value: "))
    interpretation = interpret_result(result_value)

    with open("sample_records.txt", "a", encoding="utf-8") as file:
        file.write("Sample Record\n")
        file.write(f"Sample ID: {sample_id}\n")
        file.write(f"Patient Name: {patient_name}\n")
        file.write(f"Test Name: {test_name}\n")
        file.write(f"Result Value: {result_value}\n")
        file.write(f"Interpretation: {interpretation}\n")
        file.write("-" * 30 + "\n")

    print()
print("Sample records saved successfully")

with open("sample_records.txt", "r", encoding="utf-8") as file:
    content = file.read()

print()
print("Saved Sample Records")
print()
print(content)