'''
Given a sequence of words, and a limit on the number of characters that can be put in one line (line width). Put line breaks in the given sequence such that the lines are printed neatly. Assume that the length of each word is smaller than the line width. When line breaks are inserted there is a possibility that extra spaces are present in each line. The extra spaces includes spaces put at the end of every line except the last one.
The problem is to minimize the following total cost.
Total cost = Sum of cost of all lines, where cost of line is = (Number of extra spaces in the line)^2.
For example, consider the following string and line width M = 15
“Geeks for Geeks presents word wrap problem”
Following is the optimized arrangement of words in 3 lines
Geeks for Geeks
presents word
wrap problem
The total extra spaces in line 1 and line 2 are 0 and 2. Space for line 3 is not considered as it is not extra space as described above. So optimal value of total cost is 0 + 2*2 = 4.
Examples:
Input format: Input will consists of array of integers where each array element represents length of each word of string. For example, for string S = "Geeks for Geeks", input array will be arr[] = {5, 3, 5}.
Output format: Output consists of a series of integers where two consecutive integers represent
starting word and ending word of each line.

Input : arr[] = {3, 2, 2, 5}
Output : 1 1 2 3 4 4
Line number 1: From word no. 1 to 1
Line number 2: From word no. 2 to 3
Line number 3: From word no. 4 to 4

Input : arr[] = {3, 2, 2}
Output : 1 1 2 2 3 3
Line number 1: From word no. 1 to 1
Line number 2: From word no. 2 to 2
Line number 3: From word no. 3 to 3



Recommended: Please solve it on “PRACTICE” first, before moving on to the solution.

Approach: We have discussed a Dynamic Programming based solution of word wrap problem. The solution discussed used O(n^2) auxiliary space. The auxiliary space used can be reduced to O(n). The idea is to use two 1-D arrays dp[] and ans[], where dp[i] represents minimum cost of the line in which arr[i] is the first word and ans[i] represents index of last word present in line in which word arr[i] is the first word. Let k represents limit on number of characters in each line. Suppose for any line l the first word in that line is at index i in arr[]. The minimum cost of that line is stored in dp[i]. The last word in that line is at index j in arr[], where j can vary from i to n. Iterate over all values of j and keep track of number of characters added so far in line l. If number of characters are less than k then find cost of current line with these number of characters. Compare this cost with minimum cost find so far for this line in dp[i] and update dp[i] and ans[i] accordingly. Repeat above procedure for each value of i, 1 <= i <= n. The starting and ending words of each line will be at index i and index ans[i], where next value of i for line l+1 is ans[i] + 1.
'''
import sys


def solveWordWrap(arr, n, k):
    dp = [0] * n
    ans = [0] * n
    dp[n - 1] = 0
    ans[n - 1] = n - 1
    for i in range(n - 2, -1, -1):
        currlen = -1
        dp[i] = sys.maxsize
        for j in range(i, n):
            currlen += (arr[j] + 1)
            if currlen > k:
                break
            if j == n - 1:
                cost = 0
            else:
                cost = ((k - currlen) * (k - currlen) + dp[j + 1])
            if cost < dp[i]:
                dp[i] = cost
                ans[i] = j
    i = 0
    while i < n:
        print(i + 1, ans[i] + 1, end=" ")
        i = ans[i] + 1


if __name__ == "__main__":
    arr = [3, 2, 2, 5]
    n = len(arr)
    M = 6
    solveWordWrap(arr, n, M)