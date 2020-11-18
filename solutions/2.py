# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node1 = l1
        node2 = l2
        out = ListNode()
        cur_out = out
        plus_one = False

        while True:
            d1 = node1.val
            d2 = node2.val
            

            to_add = d1+d2
            if plus_one: 
                to_add +=1
                plus_one = False
            if to_add >= 10:
                plus_one = True
                to_add -= 10
            cur_out.val = to_add


            if node1.next is None and node2.next is None:
                break
            node1 = node1.next if node1.next is not None else ListNode()
            node2 = node2.next if node2.next is not None else ListNode()

            new_out = ListNode()
            cur_out.next = new_out
            cur_out = new_out
        if plus_one:
            cur_out.next = ListNode(1)

        return out
