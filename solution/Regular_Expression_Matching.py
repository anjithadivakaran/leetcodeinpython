def isMatch(s, p):
    memo = {}
    def dp(i, j):
        print("In the function dp")
        print(i,j)
        if (i, j) not in memo:
            print("In not in memo function")
            if j == len(p):
                print("In not in memo function if j == len(p)")
                ans = i == len(s)
            else:
                print("In not in memo function else j != len(p)")
                first_match = i<len(s) and p[j] in {s[i], '.'}
                if j+1 < len(p) and p[j+1] == '*':
                    print("j+1 < len(p) and p[j+1] == '*'")
                    ans = dp(i, j+2) or first_match and dp(i+1, j)
                else:
                    print("else")
                    ans = first_match and dp(i+1, j+1)

            memo[i, j] = ans
        return memo[i, j]

    return dp(0, 0)


s = input("Enter the string: ")
p = input("Enter the pattern: ")

print(isMatch(s, p))