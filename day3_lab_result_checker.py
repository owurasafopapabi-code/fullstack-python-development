patient_name = input("Enter patient name: ")
test_name = input("Enter test name: ")
result_value = float(input("Enter result value: "))

print()
print("Lab Result Interpretation")
print(f"Patient: {patient_name}")
print(f"Test: {test_name}")
print(f"Result Value: {result_value}")

if result_value < 70:
    print("Interpretation: Low")
elif result_value >= 70 and result_value <= 110:
    print("Interpretation: Normal")
else:
    print("Interpretation: High")

print(f"Whis is this")
# who's is this