import random

# Define the length of the array and the range of random numbers
array_length = 10  # You can change this to the desired length
min_value = 1      # Minimum random number
max_value = 100    # Maximum random number

# Generate the array of random numbers
random_array = [random.randint(min_value, max_value) for _ in range(array_length)]

# Print the array
print("Original Array", random_array)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L= arr[:mid]
        R= arr[mid:]
        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i +=1
            else:
                arr[k] = R[j]
                j +=1
            k +=1 
        while i < len(L):
            arr[k] = L[i]
            i +=1
            k +=1
        while j < len(R):
            arr[k] = R[j]
            j +=1
            k +=1
merge_sort(random_array)
print("Sorted array is: " , random_array)