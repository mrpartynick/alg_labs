class Linked_List:
    value_of_elements = 0

    def __init__(self, *args):
        for data in args:
            self.add_last_elem(data)

    # Функции добавления элемента
    def add_first_elem(self, data):
        elem_for_adding = Elem_Of_Linked_List(data)
        elem_for_adding.next_elem = self.head
        self.head = elem_for_adding
        self.value_of_elements += 1

    def add_last_elem(self, data):
        elem_for_adding = Elem_Of_Linked_List(data)

        if self.value_of_elements == 0:
            self.head = elem_for_adding
            self.tail = elem_for_adding
        else:
            self.tail.next_elem = elem_for_adding
            self.tail = elem_for_adding

        self.value_of_elements += 1

    def add_elem_on_key(self, data, key):
        element = self.head
        while (element):
            if element.data == key:
                elem_for_adding = Elem_Of_Linked_List(data)
                elem_for_adding.next_elem = element.next_elem
                element.next_elem = elem_for_adding
                break
            else:
                element = element.next_elem

    def remove_first_elem(self):
        self.head = self.head.next_elem

    def remove_elem_for_key(self, key):
        element = self.head
        while (element):
            if element.data == key:
                elem_for_deleting = element.next_elem
                if elem_for_deleting.next_elem != None:
                    element.next_elem = elem_for_deleting.next_elem
                else:
                    element.next_elem = None
                break
            else:
                element = element.next_elem

    def search(self, data):
        index_of_element = 0
        element = self.head
        while (element):
            if element.data == data:
                return index_of_element
            else:
                index_of_element += 1
                element = element.next_elem
        print("Elem not in list ")

    def print_list(self):
        s = ""
        element = self.head
        while (element):
            s += str(element.data) + " "
            element = element.next_elem
        print(s)


class Elem_Of_Linked_List:

    def __init__(self, data):
        self.data = data
        self.next_elem = None


linked_list = Linked_List(1, 2, 3)

linked_list.add_first_elem(4)
linked_list.add_elem_on_key(5, 2)
linked_list.remove_elem_for_key(2)

linked_list.print_list()
