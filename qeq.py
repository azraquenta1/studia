import cmath
a = float(input("podaj a:"))
b = float(input("podaj b:"))
c = float(input("podaj c:"))
def delta(a,b,c):
    return b**2-4*a*c
d = delta(a,b,c)
if a == 0:
    print("Podano a=0")
else:
    x1 = (-b+cmath.sqrt(d))/(2*a)
    x2 = (-b-cmath.sqrt(d))/(2*a)
    if x1==x2:
        print("Jest jedno rozwiązanie:",x1)
    else:
        print("Są dwa rozwiązania")
        print("Pierwsze rozwiązanie:", x1)
        print("Drugie rozwiązanie:", x2)
