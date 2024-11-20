# Longest Common Subsequence
def lcs(X, Y):
    m = len(X) # Length of First Sequence
    n = len(Y) # Length of Second Sequence
    
    L = [[None] * (n + 1) for i in range(m + 1)]
    
    # Building the LCS length array
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i-1] == Y[j-1]:
                L[i][j] = L[i-1][j-1] + 1
            else:
                L[i][j] = max(L[i-1][j], L[i][j-1])
    
    # The length of the LCS is L[m][n]
    return L[m][n]

# Function to read the sequences from the file
def read_sequences(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        content = file.read().split('>')
        for entry in content:
            if entry:
                lines = entry.strip().split('\n')
                header = lines[0]
                sequence = ''.join(lines[1:])
                sequences.append((header, sequence))
    return sequences

# Read sequences from the given file
sequences = read_sequences('Downloads/tulp3_relatives-2-1.rtf')

# Compute the LCS for each pair of sequences
lcs_results = {}
for i in range(len(sequences)):
    for j in range(i + 1, len(sequences)):
        seq1 = sequences[i][1]
        seq2 = sequences[j][1]
        lcs_length = lcs(seq1, seq2)
        lcs_results[(sequences[i][0], sequences[j][0])] = lcs_length

# Print the LCS results for each pair
for pair, length in lcs_results.items():
    print(f'LCS length between {pair[0]} and {pair[1]}: {length}')
