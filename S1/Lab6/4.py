
def swap(arr, i,j):
    arr[i], arr[j] = arr[j], arr[i]

def make_heap(arr):
    l = []
    for elem in arr:
        l.append(elem)

        ind_of_el = len(l) - 1

        while ind_of_el < 0 and l[ind_of_el] < l[(ind_of_el - 1) // 2]:
            swap(l,ind_of_el, (ind_of_el - 1) // 2)
            ind_of_el = (ind_of_el - 1) // 2
    return l

def is_heap(arr, size):
    for i in range(size):
        root = arr[i]
        index_of_first_child = 2*i+1
        index_of_second_cild = 2*i+2
        if index_of_first_child < size and index_of_second_cild < size:
            first_child, second_child = arr[index_of_first_child], arr[index_of_second_cild]
            if first_child > root or second_child > root:
                continue
            else:
                print("NO")
                return 0
    print("Yes")


l = [1, 3, 2, 5, 4]

l = make_heap(l)
print(l)

is_heap(l,len(l))