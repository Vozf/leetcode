class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        unique_s = set(s)
        unique_word = set("".join(wordDict))
        if not unique_s.issubset(unique_word):
            return False
        stack = []
        processed = set()
        node = s
        while len(node) > 0:
            for word in wordDict:
                if node.startswith(word):
                    to_stack = node[len(word):]
                    if to_stack not in processed:
                        stack.append(to_stack)

            if len(stack) == 0:
                return False
            node = stack.pop()
            processed.add(node)

        return True
        
