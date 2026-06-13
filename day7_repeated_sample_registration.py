user_choice = "yes"

while user_choice == "yes":

    sample_id = input("Enter sample ID: ")
    patient_name = input("Enter patient name: ")
    test_name = input("Enter test name: ")
    print()

    print("Sample Registered")
    print(f"Sample ID: {sample_id}")
    print(f"Patient Name: {patient_name}")
    print(f"Test Name: {test_name}")
    print()

    user_choice = input("Do you want to register another sample? yes/no: ").lower()

print("Registration ended.")
