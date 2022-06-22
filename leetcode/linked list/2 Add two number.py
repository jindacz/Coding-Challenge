# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1) 
        curr = dummy
        p = l1
        q = l2
        carry = 0
   
        while p or q:
            x = 0 if not p else p.val 
            y = 0 if not q else q.val
            
            sum  = (x + y + carry)
            carry = sum // 10
            
            curr.next = ListNode(sum % 10) # return digit from left to right
            curr = curr.next # move curr 

            if p:  # move p, q pointer
                p = p.next 
            if q:
                q = q.next
        
        if carry != 0:
            curr.next = ListNode(carry) # if there is carry affect the right most digit
        
        return dummy.next
            
