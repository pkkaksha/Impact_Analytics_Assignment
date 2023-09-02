import sys
class Solution:
  
  def __init__(self, days,continuous_days):
    self.days = days
    self.continuous_days = continuous_days


  def util(self):
    
    """
    Time Complexity: O(days * continuous_days)
    Space Complexity: O(continuous_days)
    """

    days, continuous_days = self.days, self.continuous_days
    dp = [1] * (continuous_days + 1)
    dp[continuous_days] = 0
    temp = []

    for i in range(1, days + 1):
        temp = [0] * (continuous_days + 1)
        for j in range(continuous_days - 1, -1, -1):
            temp[j] = dp[0] + dp[j + 1]

        temp, dp = dp, temp

    the_prob_that_you_will_miss_your_graduation_ceremony = dp[0]  # total number of valid way to attend classes
    the_number_of_ways_to_attend_classes_over_N_days = temp[1]  # total number of way to miss last day

    return f"{the_number_of_ways_to_attend_classes_over_N_days}/{the_prob_that_you_will_miss_your_graduation_ceremony}"


if __name__ == "__main__":
  
  try:
    days = int(input("No of Days (N) = "))
    continuous_days = int(input("No of consecutive days (for 4 consecutive days press Enter or enter your input) = ") or "4")
  except Exception as e:
      print(e)
  else:
      solution = Solution(days,continuous_days)
      print("The number of ways to attend classes over N days/The probability that you will miss your graduation ceremony. {}".format(solution.util()))
