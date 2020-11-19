import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_add(self):
        test_list = LinkedList()
        test_list.add(5, None)
        self.assertEqual(test_list.head.value, 5)
        test_list.add(7, None)
        self.assertIsNotNone(test_list.head.next)
        self.assertEqual(test_list.head.next.value, 7)

    def test_sort(self):
        test_list = LinkedList()
        test_list.add(5, None)
        test_list.add(1, None)
        test_list.add(13, None)
        test_list.add(7, None)
        test_list.head = test_list.sort(test_list.head)
        self.assertEqual(test_list.head.value, 1)
        self.assertEqual(test_list.head.next.value, 5)
        self.assertEqual(test_list.head.next.next.value, 7)
        self.assertEqual(test_list.head.next.next.next.value, 13)

    def test_main(self):
        test_list = list()
        for element in open('max_sequence_length_result.csv', 'r').readline().split():
            test_list.append(element)
        self.assertEqual('8', test_list[0])
        self.assertEqual(1, len(test_list))
