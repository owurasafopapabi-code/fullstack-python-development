samples = []

number_of_samples = int(input("How many samples do you want to enter?: "))

for number_of_sample in range(1, number_of_samples + 1):

    sample_id = input("Enter sample ID: ")
    patient_name = input("Enter patient name: ")
    test_name = input("Enter test name: ")
    print()

    sample_record = f"{sample_id} - {patient_name} - {test_name}"

    samples.append(sample_record)

print("Sample List")
for index, sample in enumerate(samples, start=1):
    print(f"{index}. {sample}")
