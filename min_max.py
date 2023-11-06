def find_min_max(arr, start, end):
    if start == end:
        # Only one element in the subarray
        return arr[start], arr[start]
    elif end - start == 1:
        # Two elements in the subarray
        if arr[start] < arr[end]:
            return arr[start], arr[end]
        else:
            return arr[end], arr[start]
    else:
        # More than two elements, divide and conquer
        mid = (start + end) // 2
        min1, max1 = find_min_max(arr, start, mid)
        min2, max2 = find_min_max(arr, mid + 1, end)

        # Compare local minimum and maximum from the two halves
        local_min = min(min1, min2)
        local_max = max(max1, max2)

        return local_min, local_max

def find_min_max_in_array(arr):
    if not arr:
        return None, None  # Handle an empty array

    min_val, max_val = find_min_max(arr, 0, len(arr) - 1)
    return min_val, max_val

# Example usage:
arr = [3, 7, 2, 8, 1, 5, 11, 4]
min_val, max_val = find_min_max_in_array(arr)
print("Minimum:", min_val)
print("Maximum:", max_val)