## top down approach ##
def dp_1(i):
    if i <= 2:
        return i
    if i not in memo:
        memo[i] = dp_1(i - 1) + dp_1(i - 2)
    return memo[i]

## bottom-up approach ##

def dp_2(n):
    if n == 1:
        return 1

     # An array that represents the answer to the problem for a given state
    dp_2 = [0] * (n + 1)
    dp_2[1] = 1  # Base cases
    dp_2[2] = 2  # Base cases

    for i in range(3, n + 1):
        dp_2[i] = dp_2[i - 1] + dp_2[i - 2]  # Recurrence relation

    return dp_2[n]


# for test #
n = int(input())
memo = {}
print(dp_1(n))
print(dp_2(n))
