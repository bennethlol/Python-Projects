def peri(r = 1):
    circum = (2)*(3.14)*(r)
    return circum

circle1 = peri()
circle2 = peri(9)
print('The default circumference of a circle is', circle1,'units')
print('The circumference of a circle with a radius of 9 is',circle2,'units')