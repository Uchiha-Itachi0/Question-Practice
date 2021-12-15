def intersection_point(headA, headB):
    """
    Time Complexity : O(n + m)
    Auxiliary space : O(n or m)
    """
    storage = set()
    while headA:
        storage.add(headA)
        headA = headA.next
    while headB:
        if headB in storage:
            return headB.data
        headB = headB.next
    return


def intersection_point_2(headA, headB):
    """
    Time Complexity : O(n + m)
    Auxiliary space : O(1)
    """
    if headA is None or headB is None:
        return
    head1 = headA
    head2 = headB
    while head1 is not head2:
        head1 = headB if head1 is None else head1.next
        head2 = headA if head1 is None else head2.next
    return head1
