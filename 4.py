def bubbleSort(array):
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp


input_str = input("Enter numbers separated by spaces: ")
data = [int(x) for x in input_str.split()]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)

//Enter numbers separated by spaces: -2 0 9 11 45 -9
Sorted Array in Ascending Order:
[-9, -2, 0, 9, 11, 45]//
