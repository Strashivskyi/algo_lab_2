import unittest

from linked_list import LinkedList


class TestLinkedList(unittest.TestCase):

    def test_add(self):
        test_list = LinkedList()
        test_list.add(8, None)
        self.assertEqual(test_list.head.value, 8)
        test_list.add(20, None)
        self.assertIsNotNone(test_list.head.next)
        self.assertEqual(test_list.head.next.value, 20)

    def test_sort(self):
        test_list = LinkedList()
        test_list.add(12, None)
        test_list.add(7, None)
        test_list.add(40, None)
        test_list.add(20, None)
        test_list.head = test_list.sort(test_list.head)
        self.assertEqual(test_list.head.value, 7)
        self.assertEqual(test_list.head.next.value, 12)
        self.assertEqual(test_list.head.next.next.value, 20)
        self.assertEqual(test_list.head.next.next.next.value, 40)

    def test_main(self):
        test_list = list()
        for element in open('lngpok_out.csv', 'r').readline().split():
            test_list.append(element)
        self.assertEqual('8', test_list[0])
        self.assertEqual(1, len(test_list))
