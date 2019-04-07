# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class Trapeze:
    def __init__(self, A, B, C, D):
        self.A = A
        self.B = B
        self.C = C
        self.D = D


    def long_party(self):
        AB = ((self.B[0] - self.A[0])**2 + (self.B[1] - self.A[1])**2)**(1/2)
        BC = ((self.C[0] - self.B[0])**2 + (self.C[1] - self.B[1])**2)**(1/2)
        CD = ((self.D[0] - self.C[0])**2 + (self.D[1] - self.C[1])**2)**(1/2)
        AD = ((self.D[0] - self.A[0])**2 + (self.D[1] - self.A[1])**2)**(1/2)
        return (AB,BC,CD,AD)


    def perimetr(self):
        longs = self.long_party()
        i = 0
        P = 0
        while i < len(longs):
            P += longs[i]
            i += 1
        return P


    def square(self):
        longs = self.long_party()
        AB = longs[0]
        BC = longs[1]
        CD = longs[2]
        AD = longs[3]
        S = ((AD + BC)/2)*(AB**2 - (((AD - BC)**2 + AB**2 - CD**2)/(2*(AD - BC)))**2)**(1/2)
        print(f'Площадь равна\nS= {S}')

    def eq_trap(self):
        longs = self.long_party()
        sloup1 = (self.C[1] - self.B[1]) / (self.C[0] - self.B[0])
        sloup2 = (self.D[1] - self.A[1]) / (self.D[0] - self.A[0])
        if sloup1 != sloup2:
            print("Это вообще не трапеция")
        if longs[0] == longs[2]:
            print("Это равнобочная трапеция")
        else:
            print("Это не равнобочная трапеция")



class Treangle(Trapeze):
    def __init__(self, A, B, C):
        self.A = A
        self.B = B
        self.C = C


    def long_party(self):
        AB = ((self.B[0] - self.A[0]) ** 2 + (self.B[1] - self.A[1]) ** 2) ** (1 / 2)
        BC = ((self.C[0] - self.B[0]) ** 2 + (self.C[1] - self.B[1]) ** 2) ** (1 / 2)
        AC = ((self.C[0] - self.A[0]) ** 2 + (self.C[1] - self.A[1]) ** 2) ** (1 / 2)
        return (AB, BC, AC)

    def hight(self):
        longs = self.long_party()
        P = self.perimetr()
        h = ((P / 2 * (P/2 - longs[0]) * (P/2 - longs[1]) * (P/2 - longs[2]))**(1/2))/longs[0]
        return  h

    def square(self):
        longs = self.long_party()
        h = self.hight()
        S = (longs[2] * h)/2
        print(f'Площадь равна\nS= {S}')

trap = Trapeze((0,5),(-2,4),(4,2),(3,4))
trap.eq_trap()
print(f'Длины сторон:\nAB= {trap.long_party()[0]}\nBC= {trap.long_party()[1]}\nCD= {trap.long_party()[2]}\nAD= {trap.long_party()[3]}\n')
print(f'Периметр равен\nP= {trap.perimetr()}')
trap.square()

tri = Treangle((3,4),(2,-1),(-5,0))
print(f'\nДлины сторон треугольника:\nAB= {tri.long_party()[0]}\nBC= {tri.long_party()[1]}\nAC= {tri.long_party()[2]}\n')
print(f'Периметр треугольника равен\nP= {tri.perimetr()}')
print(f'Высота треугольника равна: {tri.hight()}\n')
tri.square()
