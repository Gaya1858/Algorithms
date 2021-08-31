def merge_sorted(head1, head2):
# if both lists are empty then merged list is also empty
# if one of the lists is empty then other is the merged list
    if head1 == None:
        return head2
    elif head2 == None:
        return head1

    mergedHead = None;
    if head1.data <= head2.data:
        mergedHead = head1
        head1 = head1.next
    else:
        mergedHead = head2
        head2 = head2.next

    mergedTail = mergedHead

    while head1 != None and head2 != None:
        temp = None
        if head1.data <= head2.data:
            temp = head1
            head1 = head1.next
        else:
            temp = head2
            head2 = head2.next

        mergedTail.next = temp
        mergedTail = temp

    if head1 != None:
        mergedTail.next = head1
    elif head2 != None:
        mergedTail.next = head2

    return mergedHead

print()

def deep_copy_arbitrary_pointer(head):
    if head == None:
        return None

    current = head;
    new_head = None
    new_prev = None
    ht = dict()

    # create copy of the linked list, recording the corresponding
    # nodes in hashmap without updating arbitrary pointer
    while current != None:
        new_node = LinkedListNode(current.data)

        # copy the old arbitrary pointer in the new node
        new_node.arbitrary = current.arbitrary;

        if new_prev != None:
            new_prev.next = new_node
        else:
            new_head = new_node

        ht[current] = new_node

        new_prev = new_node
        current = current.next

    new_current = new_head

    # updating arbitrary pointer
    while new_current != None:
        if new_current.arbitrary != None:
            node = ht[new_current.arbitrary]

            new_current.arbitrary = node

        new_current = new_current.next

    return new_head