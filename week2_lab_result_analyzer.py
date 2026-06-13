def interpret_result(result_value):
    if result_value < 70:
        return "Low"
    elif 70 <= result_value <= 110:
        return "Normal"
    else:
        return "High"


def calculate_average(total_value, number_of_results):
    return total_value / number_of_results


result_records = []
result_values = []

low_count = 0
normal_count = 0
high_count = 0

number_of_lab_results = int(input("How many lab results do you want to enter?: "))

for each_result in range(1, number_of_lab_results + 1):
    patient_name = input(f"Patient {each_result} name: ").title()
    test_name = input(f"Test {each_result} name: ").title()
    result_value = float(input(f"Result {each_result} value: "))
    print()

    interpretation = interpret_result(result_value)

    result_output_format = f"{patient_name} - {test_name} - {result_value} - {interpretation}"
    result_records.append(result_output_format)
    result_values.append(result_value)

    if interpretation == "Low":
        low_count = low_count + 1
    elif interpretation == "Normal":
        normal_count = normal_count + 1
    else:
        high_count = high_count + 1


total_result_value = 0

for value in result_values:
    total_result_value = total_result_value + value

average = calculate_average(total_result_value, number_of_lab_results)

highest_value = result_values[0]
lowest_value = result_values[0]

for value in result_values:
    if value > highest_value:
        highest_value = value

    if value < lowest_value:
        lowest_value = value


print("Lab Result Records")
for index, record in enumerate(result_records, start=1):
    print(f"{index}. {record}")

print()
print("Lab Result Summary")
print(f"Number of Results: {number_of_lab_results}")
print(f"Total Result Value: {total_result_value}")
print(f"Average Result Value: {average}")
print(f"Highest Result Value: {highest_value}")
print(f"Lowest Result Value: {lowest_value}")
print(f"Low Results: {low_count}")
print(f"Normal Results: {normal_count}")
print(f"High Results: {high_count}")