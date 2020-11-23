class Solution:
    def check_open(self, nest, char):
        nest.append(char)
        return nest

    def check_close(self, nest, char, opening_char):
        if nest[-1] == opening_char:
            return nest[:-1]
        else:
            raise Exception("zdarova")

    def isValid(self, s: str) -> bool:
        c1, c2, c3 = 0, 0, 0
        nest = []
        try:
            for char in s:
                if char == "(":
                    nest = self.check_open(nest, char)
                elif char == ")":
                    nest = self.check_close(nest, char, "(")
                elif char == "{":
                    nest = self.check_open(nest, char)
                elif char == "}":
                    nest = self.check_close(nest, char, "{")
                elif char == "[":
                    nest = self.check_open(nest, char)
                elif char == "]":
                    nest = self.check_close(nest, char, "[")
        except Exception as e:
            print(e)
            return False

        if len(nest) == 0:
            
            return True
        else:
            print(nest)
            return False

    
        
