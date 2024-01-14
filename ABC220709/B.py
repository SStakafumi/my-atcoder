import math

a, b, d = map(float, input().split())

cos_sita = math.cos(d*math.pi/180)
sin_sita = math.sin(d*math.pi/180)

X = cos_sita*a - sin_sita*b
Y = sin_sita*a + cos_sita*b

print(X, Y)
