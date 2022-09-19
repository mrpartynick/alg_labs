class Queue:
    queue = []

    def add_elem_in_queue(self, object):
        self.queue.append(object)

    def delete_object_from_queue(self):
        self.queue.pop(-1)


class Solution:
    open_brackets = ["[", "/n", "(", "/"]
    close_brackets = ["]","/", ")" "/"]

    open_queue = Queue()

    def find_mistake(self, s):
        for elem in s:
            if elem in self.open_brackets:
                self.open_queue.add_elem_in_queue(elem)
                if len(self.open_queue.queue) > 1 and elem != self.open_queue.queue[-2]:
                    return False
            else:
                if self.close_brackets.index(elem) == self.open_brackets.index(self.open_queue.queue[-1]):
                    self.open_queue.delete_object_from_queue()
                else:
                    return False
        if len(self.open_queue.queue) == 0:
            return True
        else:
            return False

sol = Solution()

s = "()["

print(sol.find_mistake(s))