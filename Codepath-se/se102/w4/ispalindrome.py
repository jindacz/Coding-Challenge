def isPalindrome(node):
    fullLength = getLength(node)

    firstHalf = []
    currentNode = 0
    
    while currentNode < (fullLength // 2):
        firstHalf.append(node.val)
        node = node.next
        currentNode += 1

    if fullLength % 2 == 1:
      node = node.next

    while node:
        currentNode -= 1
        if node.val != firstHalf[currentNode]:
            return False

        node = node.next

    return True