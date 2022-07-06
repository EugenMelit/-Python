import math
PI = math.pi

def radius():
    n = float(input('Введите размер диаметра в см:'))
    n /= 2
    return n
def hight():
    h = float(input('Введите размер высоты в см:'))
    return h


def volume():
    t = radius()
    y = hight()
    S = PI*t**2
    V = S*y
    return V
print('Щбьем цилиндра:',volume() , 'см.куб')
    
