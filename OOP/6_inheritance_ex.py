#inheritance exercise
import math

class Calculator:
  def __init__(self, number):
      self.n = number
      self.data = [0 for i in range(number)]

  def enterdata(self):
    self.data = [int(input('enter data ' + str(i+1) + ' = ')) for i in range(self.n)]

class Ops(Calculator):
  def __init__(self):
    Calculator.__init__(self,2)

  def add(self):
    a,b = self.data
    s = a + b
    print('the result is: ', s)

  def substract(self):
    a,b = self.data
    s = a - b
    print('the result is: ', s)

  def multiply(self):
      a,b = self.data
      s = a * b
      print('the result is: ', s)

  def divide(self):
      a,b = self.data
      s = a / b
      print('the result is: ', s)

class Root(Calculator):
  def __init__(self):
    Calculator.__init__(self,1)

  def square(self):
    a = self.data
    print('the result is: ', math.sqrt(a))

ex = Ops()
print(ex.enterdata())
print(ex.add())
