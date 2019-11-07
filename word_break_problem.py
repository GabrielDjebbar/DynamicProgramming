# O(n^3) solution(without assumptions on the length of the words of the dictionary)

dictionary = {"i": True, "like": True, "sam": True, "sung": True, "ko": True}

theString = "sungkolike"
theString2 = "ilikesamsung"

DP = [[False for _ in range(len(theString))] for _ in range(len(theString))]

states = [(i, j) for i in range(len(theString)) for j in range(len(theString)) if i <= j]
states.sort(key=lambda x: x[1] - x[0])

for state in states:
    i, j = state
    if theString[i:j + 1] in dictionary:
        DP[i][j] = True
    else:
        DP[i][j] = any([DP[i][k] and DP[k + 1][j] for k in range(i, j) if k + 1 <= j])
print(DP[0][len(theString) - 1])
