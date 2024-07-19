"""
Это всего лишь файл с основными функциями, которые должна выполнять библиотека,
но при необходимости я могу залить ее на PyPl
"""
import math as m

class triangle():


  def __init__(self, side_a=None, side_b=None, side_c=None):

    self.side_a = side_a
    self.side_b = side_b
    self.side_c = side_c

  #Вычисление площади треугольника по трем сторонам

  def TriangleThreeSidesArea(self):

    try:
      a, b, c = self.side_a, self.side_b, self.side_c
      s = (a+b+c)/2 # semi perimeter
      area = m.sqrt(s*(s-a)*(s-b)*(s-c))
      return area
    
    except ValueError:
      return 'something went wrong, try to chek your values.'

  #Проверка является ли треугольник прямоугольным

  def IsTriangleRight(self):

    try:
      a, b, c = self.side_a, self.side_b, self.side_c
      a, b, c = sorted([a, b, c])

      if a**2 + b**2 == c**2:
        return True
      else:
        return False
    
    except ValueError:
      print('something went wrong, try to chek your values.')

class circle():

  def __init__(self, radius):

    self.radius = radius

  #Вычисление площади круга через радиус

  def CircleRadiusArea(self):

      r = self.radius
      area = 3.14*m.pow(r,2)
      return area
