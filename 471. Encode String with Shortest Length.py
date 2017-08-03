'''
Problem:

Given a non-empty string, encode the string such that its encoded length is the shortest.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times.

Note:
k will be a positive integer and encoded string will not be empty or have extra space.
You may assume that the input string contains only lowercase English letters. The string's length is at most 160.
If an encoding process does not make the string shorter, then do not encode it. If there are several solutions, return any of them is fine.


Example 1:
Input: "aaa"
Output: "aaa"
Explanation: There is no way to encode it such that it is shorter than the input string, so we do not encode it.


Example 2:
Input: "aaaaa"
Output: "5[a]"
Explanation: "5[a]" is shorter than "aaaaa" by 1 character.


Example 3:
Input: "aaaaaaaaaa"
Output: "10[a]"
Explanation: "a9[a]" or "9[a]a" are also valid solutions, both of them have the same length = 5, which is the same as "10[a]".


Example 4:
Input: "aabcaabcd"
Output: "2[aabc]d"
Explanation: "aabc" occurs twice, so one answer can be "2[aabc]d".


Example 5:
Input: "abbbabbbcabbbabbbc"
Output: "2[2[abbb]c]"
Explanation: "abbbabbbc" occurs twice, but "abbbabbbc" can also be encoded to "2[abbb]c", so one answer can be "2[2[abbb]c]".
'''


class Solution(object):
  def encode (self, s):
    """Encodes the given string with optimal encoding.
    Args:
      s: string to encode.
    """
    # dp[i][j] = optimal encoding for substring s[i:j+1]
    dp = [[''] * len(s) for _  in range(len(s))]

    for l in range(len(s)):
      #Each outer loop will compute optimal encoding for all substring of length l.
      for i in range(len(s) - l):
        j = i + l
        substr = s[i:j + 1]
        dp[i][j] = substr
        # Skip if substr length < 5. In that case, we know that encoding will
        # not help.
        if l >= 4:
          # Loop for trying all results that we get after dividing the substr into 2
          # pieces, and combine the results for the pieces.
          for k in range(i, j):
            # k is the split point of the 2 pieces of the substring. We only need to
            # cut *once*, because dp[i][k] is already the optimal encoding for
            # substr[i:k+1], which in itself may include multiple x[yzk] encodings.
            if len(dp[i][k] + dp[k + 1][j]) < len(dp[i][j]):
              # Split at k is better. Update existing solution.
              dp[i][j] = dp[i][k] + dp[k + 1][j]

          # Loop for checking if the substring can itself found some pattern in
          # it which could be repeated. This is the base case for initiating the
          # encoding. We only check for single-pattern encodings, i.e. encodings
          # where there is exactly one pair of []. This is because we start l from
          # low to high, so if the optimal solution has multiple pairs of [], it
          # will be covered in the previous if block (L23-L25).
          for k in range(len(substr)):
            repeat_str = substr[0:k + 1]
            multiple = len(substr) / len(repeat_str)
            if substr == repeat_str * multiple:
              ss = '{0}[{1}]'.format(multiple, dp[i][i+k])
              if len(ss) < len(dp[i][j]):
                dp[i][j] = ss
    return dp[0][len(s) - 1]
