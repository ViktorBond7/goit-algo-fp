from merge_sorted_lists import merge_sorted_lists

def sort_list(head):
    if not head or not head.next:
        return head

    # Пошук середини списку
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None

    left = sort_list(head)
    right = sort_list(mid)

    return merge_sorted_lists(left, right)
