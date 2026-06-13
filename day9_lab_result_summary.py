result_values = []

number_of_lab_results = int(input("How many lab result values do you want to enter?: "))

for lab_result in range(1, number_of_lab_results + 1):

    # collecting each lab result values
    lab_values = float(input(f"Enter lab result {lab_result} value: "))

    # adding each lab values to the result value list
    result_values.append(lab_values)


total_result_value = 0


for each_result in result_values:
    # total result value calculation
    total_result_value = total_result_value + each_result

# highest result value
highest_value = result_values[0]

# lowest result value
lowest_value = result_values[0]

for each_result in result_values:
    if each_result > highest_value:
        highest_value = each_result

    if each_result < lowest_value:
        lowest_value = each_result

# average result value calculation
average_result_value = total_result_value / len(result_values)

print()
print("Lab Result Summary")
print(f"Number of Results: {number_of_lab_results}")
print(f"Total Result Value: {total_result_value}")
print(f"Average Result Value: {average_result_value}")
print(f"Highest Result Value: {highest_value}")
print(f"Lowest Result Value: {lowest_value}")
