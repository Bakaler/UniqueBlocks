def uniqueBlocks(n : int, sizes : int) -> int:
      '''
      :param n: Length
      :param sizes: lengths 1 through sizes
      :return: total number of unique sizes
      '''
      memo = [-1 for x in range(n+1)]
      memo[0]= 0
      return helper(n, sizes, memo)


def helper(n : int, sizes: int, memo: list) -> int:
      '''
      Helper function for the recursive DP implementation
      :param n: Length
      :param sizes: lengths 1 through sizes
      :param memo: Stores information of previously found combinations
      :return: Integer with the total combinations of size n
      '''
      if n == 0:
            return n+1
      if memo[n] != -1:
            return memo[n]


      units = []
      for size in range(1, sizes+1):
            if n-size >= 0:
                  units.append(helper(n-size, sizes, memo))

      temp = 0
      for x in range(len(units)):
            temp += units[x]

      memo[n] = temp

      return memo[n]