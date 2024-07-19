import unittest
import AreaCalculator as ac

class TestAreaCalculator(unittest.TestCase):

  def setUp(self):
    self.triangle = ac.triangle(15,13,4)
    self.circle = ac.circle(10)
  
  def test_TriangleThreeSidesArea(self):
    self.assertEqual(self.triangle.TriangleThreeSidesArea(), 24)
  
  def test_IsTriangleRight(self):
    self.assertEqual(self.triangle.IsTriangleRight(), False)
  
  def test_CircleRadiusArea(self):
    self.assertEqual(self.circle.CircleRadiusArea(), 314)
  
if __name__ == '__main__':
  unittest.main()