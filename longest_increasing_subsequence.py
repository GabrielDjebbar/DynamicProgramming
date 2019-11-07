# O(n^2) time for longest increasing subsequence (not necessary contiguous)
sequence = [10, 8, 2, 8, 4, 17, 39, 5]
LIS = [1 for _ in sequence]

for i in range(len(sequence)):
    if i == 0:
        continue
    LIS[len(sequence) - 1 - i] = max([1 + LIS[j] if sequence[len(sequence) - 1 - i] <= sequence[j] else 1 for j in
                                      range(len(sequence) - 1 - i + 1, len(sequence))])

print(max(LIS))
