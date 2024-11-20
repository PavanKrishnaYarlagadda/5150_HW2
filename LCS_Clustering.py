import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create a distance matrix based on LCS lengths
num_sequences = len(sequences)
lcs_matrix = np.zeros((num_sequences, num_sequences))

for i in range(num_sequences):
    for j in range(num_sequences):
        if i > j:
            header1 = sequences[i][0]
            header2 = sequences[j][0]
            lcs_length = lcs_results.get((header1, header2), lcs_results.get((header2, header1), 0))
            lcs_matrix[i][j] = lcs_length
        elif i == j:
            lcs_matrix[i][j] = len(sequences[i][1])  # Length of the sequence itself

# Mask the upper triangle and diagonal
mask = np.triu(np.ones_like(lcs_matrix, dtype=bool))

# Create a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(lcs_matrix, annot=True, fmt=".0f", mask=mask, xticklabels=[seq[0] for seq in sequences], yticklabels=[seq[0] for seq in sequences], cmap="YlGnBu")
plt.title('Longest Common Subsequences (between each sequence)')
plt.xticks(rotation=90)
plt.yticks(rotation=0)
plt.show()


# Creating groups based on a threshold (we took 0.5 * max_LCS)
threshold = 0.5 * max_lcs
clusters = fcluster(linked, threshold, criterion='distance')

# Grouping organisms based on clustering results
groups = {}
for idx, cluster_id in enumerate(clusters):
    groups.setdefault(cluster_id, []).append(organisms[idx])

for group_id, members in groups.items():
    print(f"Group {group_id}: {', '.join(members)}")
