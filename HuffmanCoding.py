import heapq
from collections import defaultdict
import re

# Given file in assignment contains tab spaces
# We are removing the tab spaces - since these are being considered as a character.
def extract_sequence_from_rtf(file_path):
    with open(file_path, 'r') as file:
        rtf_content = file.read()
    
    # Regular expression to remove tab and new lines
    seq = re.sub(r'[\t\n\r\s]', '', rtf_content)
    return seq.upper()

# Calculating the frequency of characters
def calculate_frequency(seq):
    freq = defaultdict(int)
    for char in seq:
        freq[char] += 1
    return freq

# Binary coding
def binary_compress(seq, n_unique_letters):
    bit_length = n_unique_letters.bit_length()  # Log base 2 of n unique letters
    letter_to_binary = {letter: format(i, f'0{bit_length}b') for i, letter in enumerate(sorted(set(seq)))}
    compressed = ''.join([letter_to_binary[char] for char in seq])
    return compressed, letter_to_binary

# Huffman coding
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_compress(seq):
    freq = calculate_frequency(seq)
    heap = [HuffmanNode(char, freq) for char, freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        node = HuffmanNode(None, left.freq + right.freq)
        node.left = left
        node.right = right
        heapq.heappush(heap, node)

    def generate_codes(node, current_code=""):
        if node is None:
            return {}
        if node.char is not None:
            return {node.char: current_code}
        codes = {}
        codes.update(generate_codes(node.left, current_code + "0"))
        codes.update(generate_codes(node.right, current_code + "1"))
        return codes

    codes = generate_codes(heap[0])
    compressed = ''.join([codes[char] for char in seq])
    return compressed, codes

# Calculating memory usage
def calculate_memory_usage(seq, compressed, method):
    seq_size = len(seq) * 8
    compressed_size = len(compressed)
    return seq_size, compressed_size

# Loading the sequence from the given file
file_path = "Downloads/PROT_SEQ.txt"  # Path (Replace this file for Protein and DNA Sequences)
DNA_SEQ = extract_sequence_from_rtf(file_path)

# Binary coding
binary_dna_compressed, binary_dna_mapping = binary_compress(DNA_SEQ, len(set(DNA_SEQ))-1)

# Huffman coding
huffman_dna_compressed, huffman_dna_codes = huffman_compress(DNA_SEQ)

# Memory usage comparison
dna_binary_size, dna_binary_compressed_size = calculate_memory_usage(DNA_SEQ, binary_dna_compressed, "binary")
dna_huffman_size, dna_huffman_compressed_size = calculate_memory_usage(DNA_SEQ, huffman_dna_compressed, "huffman")

# Output
print("Binary Compression Size:", dna_binary_compressed_size, "bits")
print("Huffman Compression Size:", dna_huffman_compressed_size, "bits")

# Frequency
print("\nFrequency of character in PROTEIN sequence:")
dna_freq = calculate_frequency(DNA_SEQ)
for char, freq in dna_freq.items():
    print(f"Character: {char} - Frequency: {freq}")

# Codes used for each character in Binary coding
print("\nBinary Codes for Protein Sequence:")
for char, code in binary_dna_mapping.items():
    print(f"Character: {char} - Code: {code}")

# Codes used for each character in Huffman coding
print("\nHuffman Codes for Protein Sequence:")
for char, code in huffman_dna_codes.items():
    print(f"Character: {char} - Code: {code}")
