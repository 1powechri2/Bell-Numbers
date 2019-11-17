class StirlingNumbers:

  def factorial(self, num):
    if num == 0:
      return 1
    else:
      sum = num
      while num >= 2:
        num = num - 1
        sum = sum * num
      return sum

  def one_over_subgroup(self, k):
    a = self.factorial(k)
    return 1 / float(a)

  def negative_one_to_the_power_of_the_iterator(self, i):
    return (-1) ** i

  def binomial_coefficient(self, n, k):
    a = self.factorial(n)
    b = self.factorial(n - k) * self.factorial(k)
    return a/b

  def subgroup_minus_iterator_to_the_power_of_the_set_number(self, k, i, n):
    return (k - i) ** n

  def stirling_numbers(self, n, k):
    sub_per = self.one_over_subgroup(k)
    sum = 0
    i = 0
    while i <= k:
      a = self.negative_one_to_the_power_of_the_iterator(i)
      b = self.binomial_coefficient(k, i)
      c = self.subgroup_minus_iterator_to_the_power_of_the_set_number(k, i, n)
      sum += a * b * c
      i += 1
    return sub_per * sum
