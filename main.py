import AreaCalculator as ac
from unittest import main

tr = ac.triangle(12,8,5)
crcl = ac.circle(7)

print(tr.TriangleThreeSidesArea())
print(tr.IsTriangleRight())
print(crcl.CircleRadiusArea())


main(module='test_module', exit = False)