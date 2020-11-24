class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        unique_s = set(s)
        unique_word = set("".join(wordDict))
        if not unique_s.issubset(unique_word):
            print("non_uni")
            return []
        stack = [(s, ())]
        outputs = []

        node = s
        while len(stack) > 0:
            node, words = stack.pop()

            if len(node) == 0:
                outputs.append(" ".join(words))
                continue

            for word in wordDict:
                if node.startswith(word):
                    to_stack = node[len(word):]
                    new_words = (*words, word)
                    stack.append((to_stack, new_words))


        return outputs
        
