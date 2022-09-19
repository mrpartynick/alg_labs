class Group_of_recruits:
    line = [1]
    crowd = [i for i in range(2,1000)]


    def binarySearch(arr, n):
        m = 0
        h = len(arr) - 1

        while m <= h:
            mid = m + h
            guess = arr[mid]

            if guess == n:
                return mid
            if guess > n:
                h = mid - 1
            if guess < n:
                m = mid + 1

        return -1


    def leave_line(self, pvt):
        index_of_pvt = self.line.index(pvt)

        self.crowd.append(self.line.pop(index_of_pvt))


    def left(self, i, j):
        index_of_j = self.line.index(j)
        index_of_i = self.crowd.index(i)

        self.line = self.line[:index_of_j] + [i] + self.line[index_of_j:]
        self.crowd.pop(index_of_i)


    def right(self, pvt_in_line, pvt_in_crowd):
        index_of_pvt_in_line = self.line.index(pvt_in_line)
        index_of_pvt_in_crowd = self.crowd.index(pvt_in_crowd)

        self.line = self.line[:index_of_pvt_in_line+1] + [pvt_in_crowd] + self.line[index_of_pvt_in_line+1:]
        self.crowd.pop(index_of_pvt_in_crowd)

    def name(self, pvt):
        index_of_pvt = self.line.index(pvt)

        if index_of_pvt != 0:
            if pvt != self.line[-1]:
                print(self.line[index_of_pvt-1], self.line[index_of_pvt+1])
            else:
                print(self.line[index_of_pvt-1], 0)
        else:
            print(0, self.line[index_of_pvt+1])

group = Group_of_recruits()

group.left(2,1)
print(group.line)
group.right(1,3)
print(group.line)
group.leave_line(1)
print(group.line)
group.name(2)

