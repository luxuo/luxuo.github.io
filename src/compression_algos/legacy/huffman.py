from collections import Counter
import heapq
from ..compressor import Compressor
# code partiellement adapté de https://www.geeksforgeeks.org/dsa/huffman-coding-in-python/
class Node:
    def __init__(self, symbol='', frequency=0):
        self.symbol = symbol
        self.code = None
        self.frequency:int = frequency
        self.zero:Node|None = None
        self.one:Node|None = None

    def __lt__(self, other):
        return self.frequency < other.frequency

class Huffman(Compressor):
    def create_root(self, counter: Counter[str]) -> None:
        # create nodes
        nodes:list[Node] = []
        for key in counter.keys():
            nodes.append(Node(symbol=key, frequency=counter[key]))
        # merge all nodes
        heapq.heapify(nodes)
        while len(nodes) > 1:
            zero_child:Node = heapq.heappop(nodes)
            one_child = heapq.heappop(nodes)
            merged_node = Node(frequency=zero_child.frequency + one_child.frequency)
            merged_node.zero = zero_child
            merged_node.one = one_child
            heapq.heappush(nodes, merged_node)
        self.root = nodes[0]

    def generate_codes(self) -> None:
        code_dict:dict[str,str] = {}
        for symbol,code in self.dfs(self.root):
            code_dict[symbol] = code
        self.code_dict = code_dict

    def dfs(self, root:Node|None, code:str = '') -> list[tuple[str,str]]:
        if root is None:
            return []
        if root.symbol == '':
            return self.dfs(root.zero, code + '0') + self.dfs(root.one, code + '1')
        # symbol exists, must be leaf
        return [(root.symbol,code)]
        

    def C(self, str:str) -> str:
        counter = Counter(str)
        self.create_root(counter)
        self.generate_codes()
        compressed_str = ''
        for c in str:
            compressed_str = compressed_str + self.code_dict[c]

        return compressed_str
    
    def D(self, str:str) -> str:
        if self.root is None:
            raise Exception('No huffman tree. Compress text before decompressing')
        decompressed_str = ''
        pointer:Node = self.root
        for c in str:
            if c == '0' and pointer.zero: # zero tree traversal
                pointer = pointer.zero
                if pointer.symbol != '': # leaf node
                    # concat decompressed string
                    decompressed_str = decompressed_str + pointer.symbol
                    # reset pointer
                    pointer = self.root
            elif c == '1' and pointer.one: # one tree traversal
                pointer = pointer.one
                if pointer.symbol != '': # leaf node
                    # concat decompressed string
                    decompressed_str = decompressed_str + pointer.symbol
                    # reset pointer
                    pointer = self.root
            else:
                raise Exception('Tree issue or invalid compressed text')
        return decompressed_str
