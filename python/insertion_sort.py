arr = [1, 2, 2, 41, 412, 413, 1000]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr

def insertion_sort_rev(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key > arr[j]:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
    return arr

if __name__ == '__main__':
    print(insertion_sort(arr))
    print(insertion_sort_rev(arr))
