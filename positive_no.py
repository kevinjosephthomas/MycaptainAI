#To print All Positive Numbers
def print_positive_numbers(num_list):
    positive_numbers = [num for num in num_list if num > 0]
    print(", ".join(map(str, positive_numbers)))

list1 = [12, -7, 5, 64, -14]
list2 = [12, 14, -95, 3]

print("Input: list1 =", list1)
print("Output:", end=" ")
print_positive_numbers(list1)

print("Input: list2 =", list2)
print("Output:", end=" ")
print_positive_numbers(list2)
