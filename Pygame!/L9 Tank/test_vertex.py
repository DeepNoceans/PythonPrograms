import math

angleA_X, angleA_Y = (0,0)
angleB_X, angleB_Y = (1,1)

deltaX = angleB_X - angleA_X
deltaY = angleB_Y - angleA_Y

tan = deltaX/deltaY

formula = math.atan(tan)

formula = formula ** 2
formula = math.sqrt(formula)

formula = math.degrees(formula)

print(formula)
