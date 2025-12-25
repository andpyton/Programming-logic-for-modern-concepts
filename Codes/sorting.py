
# Sorting numbers, smallest to largest.

while True:

    try:

        size = int(input("Type size of the list (value bigger than 0): "))

        if (size<=0):

            print("You need type a value bigger than 0.")

        else:
            break

    except ValueError:

        print("Try again, not recognized...")

list1 = []

while (len(list1)<size):

    add_number = int(input("Type a positive or negative number: "))
    list1.append(add_number)

# This function will sort the values ​​from smallest to largest number.

def sorting_smallest_to_largest(list1, size):

    i=0

    for i in range(size-1):

        for j in range (i+1, size):

            if list1[j] < list1[i]:

                list1[i], list1[j] = list1[j], list1[i]

            else:
                continue

    return list1


print(f'List sorted: {sorting_smallest_to_largest(list1, size)}')

                
