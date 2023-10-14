import heapq
from collections import defaultdict, Counter

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    char_freq = Counter(data)
    min_heap = [Node(char, freq) for char, freq in char_freq.items()]
    heapq.heapify(min_heap)

    while len(min_heap) > 1:
        left = heapq.heappop(min_heap)
        right = heapq.heappop(min_heap)
        internal_node = Node(None, left.freq + right.freq)
        internal_node.left = left
        internal_node.right = right
        heapq.heappush(min_heap, internal_node)

    return min_heap[0]

def build_huffman_codes(node, current_code, huffman_codes):
    if node is None:
        return

    if node.char is not None:
        huffman_codes[node.char] = current_code
        return

    build_huffman_codes(node.left, current_code + '0', huffman_codes)
    build_huffman_codes(node.right, current_code + '1', huffman_codes)

def huffman_encoding(data):
    if not data:
        return "", None

    root = build_huffman_tree(data)
    huffman_codes = {}
    build_huffman_codes(root, "", huffman_codes)
    encoded_data = ''.join([huffman_codes[char] for char in data])
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if not encoded_data:
        return ""
    
    decoded_data = []
    current_node = root

    for bit in encoded_data:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right

        if current_node.char is not None:
            decoded_data.append(current_node.char)
            current_node = root

    return ''.join(decoded_data)

if __name__ == "__main__":
    # Example usage:
    data = "this is an example for huffman encoding"
    
    encoded_data, tree = huffman_encoding(data)
    decoded_data = huffman_decoding(encoded_data, tree)
    
    print(f"Original data: {data}")
    print(f"Encoded data: {encoded_data}")
    print(f"Decoded data: {decoded_data}")
