def longest_palindrome(s):
  """
  Finds the longest palindromic substring in a string.

  Args:
      s: The string to search for palindromes in.

  Returns:
      The longest palindromic substring in the string.
  """

  n = len(s)
  # Create a DP table to store palindrome lengths
  dp = [[0] * n for _ in range(n)]

  # Base case: Single characters are palindromes
  for i in range(n):
    dp[i][i] = 1

  # Find the longest palindrome substring
  for i in range(n - 1, -1, -1):
    for j in range(i + 1, n):
      if s[i] == s[j]:
        dp[i][j] = dp[i + 1][j - 1] + 2
      else:
        dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

  # Return the longest palindrome substring
  return s[i:j + 1] if dp[0][n - 1] > 0 else ""

# Example usage
s1 = "babad"
s2 = "cbbd"
print(f"Longest palindrome in '{s1}': {longest_palindrome(s1)}")
print(f"Longest palindrome in '{s2}': {longest_palindrome(s2)}")
