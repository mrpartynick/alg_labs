l = [1, 3, 2, 5, 4]

class BinaryTreeSort:
    heap = []

    def binary_sort(self, arr):
        l = []
        for elem in arr:
            self.insert(elem)
        for i in range(len(arr)-1):
            l.append(self.remove_max())
        l.append(self.heap[-1])
        return l

    def swap(self, ind_of_fir, ind_of_sec):
        self.heap[ind_of_fir],  self.heap[ind_of_sec] = self.heap[ind_of_sec], self.heap[ind_of_fir]

    def insert(self, elem):
        self.heap.append(elem)
        ind_of_el = len(self.heap) - 1

        while ind_of_el > 0 and self.heap[ind_of_el] > self.heap[(ind_of_el - 1)//2]:
            self.swap(ind_of_el, (ind_of_el - 1)//2)
            ind_of_el = (ind_of_el - 1) // 2

    def remove_max(self):
        self.swap(0, -1)
        deleted_max = self.heap.pop(-1)
        i = 0


        while True:
            first_child, second_child = 2 * i + 1, 2 * i + 2

            #Если есть оба ребенка
            if first_child < len(self.heap) and second_child < len(self.heap):
                #Находим максимального ребенка
                if self.heap[first_child] > self.heap[second_child]:
                    #Если максимальный ребенок больше родителя
                    if self.heap[i] < self.heap[first_child]:
                        self.swap(i,first_child)
                        i = first_child
                    else:
                        break
                else:
                    if self.heap[i] < self.heap[second_child]:
                        self.swap(i,second_child)
                        i = second_child
                    else:
                        break
            #Если один ребенок
            elif first_child < len(self.heap):
                if self.heap[i] < self.heap[first_child]:
                    self.swap(i,first_child)
                    i = first_child
                else:
                    break
            else:
                break
        return deleted_max


        #return deleted_max

def is_heap(arr, size):
    for i in range(size):
        root = arr[i]
        index_of_first_child = 2*i+1
        index_of_second_cild = 2*i+2
        if index_of_first_child < size and index_of_second_cild < size:
            first_child, second_child = arr[index_of_first_child], arr[index_of_second_cild]
            if first_child < root or second_child < root:
                continue
            else:
                print("NO")
                return 0
    print("Yes")


a = BinaryTreeSort()
l = a.binary_sort(l)
print(l)

is_heap(l, len(l))



