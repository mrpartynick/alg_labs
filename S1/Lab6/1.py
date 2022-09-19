l = [1,3,2,5,4]

def is_heap(arr, size):
    for i in range(size//2):
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

is_heap(l,5)


def swap(self, ind_of_fir, ind_of_sec):
    self.heap[ind_of_fir], self.heap[ind_of_sec] = self.heap[ind_of_sec], self.heap[ind_of_fir]

def insert(elem, arr):
    arr.append(elem)
    ind_of_el = len(arr) - 1

    while ind_of_el > 0 and arr[ind_of_el] < arr[(ind_of_el - 1) // 2]:
        swap(arr[ind_of_el], arr[(ind_of_el - 1) // 2])
        ind_of_el = (ind_of_el - 1) // 2
    return arr




