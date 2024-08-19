def quickSort(arr):

  if len(arr) <= 1:
    return arr

  pivot = arr[len(arr) // 2]

  left_arr = quickSort([ num for num in arr if num < pivot ])
  centre = [ num for num in arr if num == pivot ]
  right_arr = quickSort([ num for num in arr if num > pivot ])

  return left_arr + centre + right_arr
  

arr = [9, 7, 5, 11, 12, 2, 14, 3, 10, 6]
print(quickSort(arr))