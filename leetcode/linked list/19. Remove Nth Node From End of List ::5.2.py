# 19. Remove Nth Node From End of List

# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 
def removeNthFromEnd(self, head, n):
        #         '''
#         P: ll, number
#         R: lll
#         E: 
#         1-2-3-4-5, n = 1 
#         1-2-3-4
        
#         1-2-3-4-5, n = 5  
#         2-3-4-5
        
#         1-2-3-4-5, n = 3  
#         1-2-4-5
        
#         P:
#         multipass:
#         get length of ll in one-pass, increment pointer length-n times. you are    at the node you want to delete. keep track of previous node, remove the node you are at.
        
#         dummyhead + twoPointer:
#         seperate two ptr by n node, once left pointer reaches the end of the list,   then the left ptr's next node is the node you want to delete. To make it easy deleting the head of the list. use a dummy head
#         '''
        if head == None:
            return None
        dummyHead = ListNode(-1)
        dummyHead.next = head
        
        left = right = dummyHead
        # move right ptr n nodes apart
        for i in range(n):
            right = right.next
        # move both ptr until right ptr to the end of ll    
        while right.next != None:
            left = left.next
            right = right.next
        left.next = left.next.next
        
        return dummyHead.next
    
        # test your code, go through test cases, line by line
        # evaluate time space, o(n)T, o(1)S