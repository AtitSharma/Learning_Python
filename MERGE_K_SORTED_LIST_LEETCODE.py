# https://leetcode.com/problems/merge-k-sorted-lists/

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):

        new_list = self.get_sorted_list(lists)
        dummy_head = ListNode(0)
        current = dummy_head
        for i in new_list:
            current.next = ListNode(i)
            current = current.next
        return dummy_head.next

    def get_sorted_list(self,head):
        new_arr = []
        for i in head :
            new_head = i 
            while new_head is not None :
                new_arr.append(new_head.val)
                new_head = new_head.next
        new_arr.sort()
        return new_arr





        