from linked_list import LinkedList


def main():
    cards = LinkedList()
    jokers_number = 0
    max_sequence_length = 0

    for element in open('lngpok_in.csv').readline().split():
        if cards.length >= 10000:
            raise Exception('Too many cards')
        if int(element) > 1000000:
            raise Exception('The card value is too big')
        if int(element) < 0:
            raise Exception('Negative values are not allowed')
        if int(element) == 0:
            jokers_number += 1
        else:
            cards.add(int(element), None)
    if cards.length <= 1:
        max_sequence_length = jokers_number + cards.length
    else:
        cards.head = cards.sort(cards.head)

        current_element = cards.head

        while current_element is not None:
            sequence_length = 1
            jokers_size = jokers_number

            next_element = current_element.next
            prev_element = current_element
            while next_element is not None:
                space_size = (next_element.value - prev_element.value) - 1

                if space_size == 0:
                    sequence_length += 1

                if space_size > 0:
                    if jokers_size >= space_size:
                        sequence_length += space_size + 1
                        jokers_size -= space_size
                    else:
                        sequence_length += jokers_size
                        jokers_size = 0
                        break
                prev_element = next_element
                next_element = next_element.next

            sequence_length += jokers_size
            if sequence_length > max_sequence_length:
                max_sequence_length = sequence_length
            current_element = current_element.next
    open('lngpok_out.csv', 'w').write(str(max_sequence_length))


if __name__ == '__main__':
    main()
