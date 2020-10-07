# LeetCode
# numComponents 
# Created by Yigang Zhou on 2020/10/7.
# Copyright © 2020 Yigang Zhou. All rights reserved.
from common.linkedListCommon import *


class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        G = set(G)
        # print(G)
        ans = [[]]
        while head:
            if head.val in G:
                ans[-1].append(head.val)
            else:
                if len(ans[-1]):
                    ans.append([])
            head = head.next
        if len(ans) and len(ans[-1]) == 0:
            return len(ans) - 1
        else:
            return len(ans)



head = generateLinkedList([0, 1, 2, 3,4])
G = [0, 3, 1, 4]
r = Solution().numComponents(head, G)
