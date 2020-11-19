class Node:

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, value, next_node):
        new_element = Node(value, next_node)
        if self.length == 0:
            self.head = new_element
        elif self.length == 1:
            self.head.next = new_element
        else:
            current = self.head.next
            while current.next:
                current = current.next
            current.next = new_element
        self.length += 1

    def __merge(self, left, right):
        if left is None:
            return right
        elif right is None:
            return left

        if left.value <= right.value:
            result = left
            result.next = self.__merge(left.next, right)
        else:
            result = right
            result.next = self.__merge(left, right.next)
        return result

    @staticmethod
    def _get_middle(head):
        middle = head
        next_peek = head
        while (next_peek.next is not None and
               next_peek.next.next is not None):
            middle = middle.next
            next_peek = next_peek.next.next
        return middle

    def sort(self, head: Node):
        if head is None or head.next is None:
            return head

        middle = LinkedList._get_middle(head)

        next_to_middle = middle.next
        middle.next = None

        left = self.sort(head)
        right = self.sort(next_to_middle)

        sorted_list = self.__merge(left, right)

        return sorted_list
