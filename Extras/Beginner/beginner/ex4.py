# Initialize the given list
my_list = [1, 2, 3, 4, 5]

# Determine the length of the list
list_length = len(my_list)

# Loop through the first half of the list
for i in range(list_length // 2):
    # Swap elements at indices i and -(i + 1)
    my_list[i], my_list[-(i + 1)] = my_list[-(i + 1)], my_list[i]

# Print the reversed list
print(my_list)
