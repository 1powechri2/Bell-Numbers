from stirling_numbers import StirlingNumbers as sn

class BellNumbers:

  def bell_numbers(self, num):
    sum = 0
    i = 0
    while i <= num:
      sum += sn().stirling_numbers(num, i)
      i += 1
    return sum

  def bell_numbers_list(self, num):
      bank = []
      i = 0
      while i <= num:
        bank.append(self.bell_numbers(i))
        i += 1
      return bank
