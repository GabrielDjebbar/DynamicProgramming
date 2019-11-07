# O(n) time, O(n) space solution for longest increasing contiguous subsequence.
# The idea : You don't where your longest subsequence begin. So, try all possibilities. Consider LIS[i] the value of the longest subsequence beginning
# index i. To compute it, we only need to know the value of LIS[i+1].

sequence = [10, 8, 2, 8, 4, 17, 39, 5]
LIS = [1 for _ in sequence]

for j in range(len(sequence)):
    if j == 0:
        continue

    LIS[len(sequence) - 1 - j] = 1 + LIS[len(sequence) - 1 - j + 1] if sequence[len(sequence) - 1 - j] <= sequence[
        len(sequence) - 1 - j + 1] else 1

print(max(LIS))
