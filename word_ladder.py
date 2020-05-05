from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if (beginWord == '') | (endWord == '') | (len(beginWord) != len(endWord)) | (wordList == []):
            return 0

        if (beginWord is None) | (endWord is None) | (wordList is None):
            return 0

        queue = deque([beginWord])
        visited = set([beginWord])
        n_step = 1

        while queue:
            n_step += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node == endWord:
                    return n_step
                for next_word in self.get_next_word(node, wordList):
                    if next_word in visited:
                        continue
                    queue.append(next_word)
                    visited.add(next_word)

        return 0

    def get_next_word(self, word, wordlist):
        # note that the word list could be very large
        alphenatic = 'abcdefghijklmnopqrstuvwxyz'
        next_word_list = []
        for i in range(len(word)):
            for letter in alphenatic:
                next_word = word[:i] + letter + word[(i + 1):]
                if next_word in wordlist:
                    next_word_list.append(next_word)

        return next_word_list

    def get_next_word(self, word, wordlist):
        # note that the word list could be very large
        next_word_list = []
        for target_word in wordlist:
            counter = 0
            for (w, t) in zip(word, target_word):
                if w != t:
                    counter += 1
                    if counter > 1:
                        break
            if counter == 1:
                next_word_list.append(target_word)

        return next_word_list
