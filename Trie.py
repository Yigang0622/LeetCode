# LeetCode
# Trie 
# Created by Yigang Zhou on 2020/7/27.
# Copyright © 2020 Yigang Zhou. All rights reserved.

# 前缀树
# https://leetcode-cn.com/explore/interview/card/top-interview-questions/275/string/1140/
from typing import List


class Trie:


    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.is_end = False
        self.next = [None for _ in range(26)]



    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        root = self
        for each_char in word:
            idx = int(ord(each_char)) - 97
            if root.next[idx] is None:
                root.next[idx] = Trie()
            root = root.next[idx]
        root.is_end = True



    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        if not word:
            return True
        root = self
        for each_char in word:
            idx = int(ord(each_char)) - 97
            if root.next[idx] is not None:
                root = root.next[idx]
            else:
                return False
        return root.is_end



    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        if not prefix:
            return True
        root = self
        for each_char in prefix:
            idx = int(ord(each_char)) - 97
            if root.next[idx] is not None:
                root = root.next[idx]
            else:
                return False
        return True


t = Trie()
t.insert('helloworld')
t.insert('hel')
t.insert('abc')
t.insert('abcd')
print(t.search('helloworld'))
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

