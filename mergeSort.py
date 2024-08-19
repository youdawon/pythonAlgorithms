def merge_sort(arr):
  if len(arr) == 1:
    return arr

  centre = len(arr) // 2
  left_arr = merge_sort(arr[:centre])
  right_arr = merge_sort(arr[centre:])

  return merge(left_arr, right_arr)

def merge(left_arr, right_arr):
  sorted_arr = []
  left_index, right_index = 0, 0

  while left_index < len(left_arr) and right_index < len(right_arr):
    if left_arr[left_index] < right_arr[right_index]:
      sorted_arr.append(left_arr[left_index])
      left_index += 1
    else:
      sorted_arr.append(right_arr[right_index])
      right_index += 1

  sorted_arr.extend(left_arr[left_index:])
  sorted_arr.extend(right_arr[right_index:])

  return sorted_arr
    

# 사용 예시
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("정렬된 배열:", sorted_arr)
