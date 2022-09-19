class Queue:
    queue = []

    def add_person_in_queue(self, person):
        self.queue = [person] + self.queue

    def remove_person_from_queue(self):
        self.queue.pop(-1)

    def take_person_in_begin_of_queue(self, person):
        self.remove_person_from_queue()
        self.add_person_in_queue(person)


class MinistryOfBureaucracy:
    value_of_reference = 0
    queue_for_reference = Queue()

    def __init__(self, value_of_references, *args):
        self.queue_for_reference.queue = [*args]
        self.value_of_reference = value_of_references

    def work_day(self):
        references = self.value_of_reference

        for i in range(self.value_of_reference+1):
            self.queue_for_reference.queue[-1] -= 1
            references -= 1
            if self.queue_for_reference.queue[-1] == 0:
                self.queue_for_reference.remove_person_from_queue()
            else:
                self.queue_for_reference.take_person_in_begin_of_queue(self.queue_for_reference.queue[-1])
            if references == 0:
                break

        if self.queue_for_reference.queue == []:
            print(-1)
        else:
            print(len(self.queue_for_reference.queue))


ministry = MinistryOfBureaucracy(2,1,2,3)
ministry.work_day()