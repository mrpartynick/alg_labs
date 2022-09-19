def binarySearch(arr, n):
    m = 0
    h = len(arr)-1

    while m <= h:
        mid = m+h
        guess = arr[mid]

        if guess == n:
            return mid
        if guess > n:
            h = mid - 1
        if guess < n:
            m = mid+1

    return -1

l = [1, 5, 8, 12, 13]
elem_for_search = [8, 1, 23, 1, 11]

for elem in elem_for_search:
    print(binarySearch(l, elem))
