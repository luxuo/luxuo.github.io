from .compressor import Compressor
import math

class LZW(Compressor):
    def C(self, str:str) -> str:
        # init dictionnary, not exaclty lzw loyal, but that's what it's gonna be
        char_dict = {}
        for c in str:
            if c not in char_dict:
                char_dict[c] = ord(c)
        self.char_dict = char_dict
        
        # 
        output = []
        new_order = max(char_dict.values()) + 1 # 256
        p = str[0]
        for i in range(1,len(str)):
            c = str[i]
            if p + c in char_dict:
                p = p + c
            else:
                output.append(char_dict[p])
                # insert p + c to dict
                char_dict[p+c] = new_order
                new_order += 1
                # next char
                p = c
        # last char
        output.append(char_dict[p])
        self.output = output
        return ''.join([chr(o) for o in output])

    def D(self, str:str) -> str:

        return ''

    def C_len(self, str:str) -> float:
        if len(str) == 0:
            return 0.0
        self.C(str)
        return math.ceil(math.log2(max(self.output))) * len(self.output)