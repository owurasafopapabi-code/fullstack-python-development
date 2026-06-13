print()
number_of_samples = int(input("How many samples do you want to register: "))
print()

print("Sample Registration Summary")

for number_of_sample in range(1, number_of_samples + 1):
    print()
    
    sample_id = input(f"Enter sample {number_of_sample} ID: ")
    patient_name = input(f"Enter sample {number_of_sample} patient name: ")
    test_name = input(f"Enter sample {number_of_sample} test name: ")

    print()
    print(f"Sample {number_of_sample}")
    print(f"Sample ID: {sample_id}")
    print(f"Patient Name: {patient_name}")
    print(f"Test Name: {test_name}")
    