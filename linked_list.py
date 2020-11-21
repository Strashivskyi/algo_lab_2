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
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_element
        self.length += 1

    def merge(self, left, right):
        if left is None:
            return right
        elif right is None:
            return left

        if left.value <= right.value:
            result = left
            result.next = self.merge(left.next, right)
        else:
            result = right
            result.next = self.merge(left, right.next)
        return result

    @staticmethod
    def get_middle(head):
        middle = head
        fast_node = head
        while (fast_node.next is not None and
               fast_node.next.next is not None):
            middle = middle.next
            fast_node = fast_node.next.next
        return middle

    def sort(self, head: Node):
        if head is None or head.next is None:
            return head

        middle = LinkedList.get_middle(head)

        next_to_middle = middle.next
        middle.next = None

        left = self.sort(head)
        right = self.sort(next_to_middle)

        sorted_list = self.merge(left, right)

        return sorted_list
