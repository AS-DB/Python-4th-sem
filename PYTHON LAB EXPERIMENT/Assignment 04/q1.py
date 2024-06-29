#wap to print second largest and smallest element in a list of 10 integer without using the sort function.


a = eval(input("Enter the list integer elements: "))

# Convert the list to a set to remove duplicates, then back to a list
b = list(set(a))

if len(b) < 2:
    print("List must have at least two distinct elements.")
else:
    # Initialize second smallest and largest to infinity and negative infinity respectively
    second_smallest = float('inf')
    second_largest = float('-inf')

    # Loop through the elements to find the second smallest and largest
    for i in b:
        if i < second_smallest:
            second_smallest = i
        if i > second_largest:
            second_largest = i

    # Remove second smallest and largest elements from the list
    b.remove(second_smallest)
    b.remove(second_largest)

    # Find the new minimum and maximum values
    new_minimum = min(b)
    new_maximum = max(b)

    print("Second smallest element:", second_smallest)
    print("Second largest element:", second_largest)
