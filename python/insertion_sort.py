arr = [1000,2,413,412,41,2,1]

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = key
        print(arr)
    return arr

if __name__ == '__main__':
    print(insertion_sort(arr))