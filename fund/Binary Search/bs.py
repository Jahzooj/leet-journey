def binary_search(target, arr):
    start = 0
    end = len(arr) - 1

    while(start < end):
        mid = (start + end) // 2

        if target == arr[mid]:
            return mid
        elif target < arr[mid]:
            end = mid
        elif target > arr[mid]:
            start = mid + 1

    return start if arr[start] == target else -1

if __name__ == '__main__':
    arr = [5,8,12,18,25,27,33,37,52,74]
    index = binary_search(74, arr)

    print(f'the index of the targe element is {index}')