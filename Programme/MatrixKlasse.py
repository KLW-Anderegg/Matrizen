import math

class matrix2x2:
    def __init__(self, a, b, c, d):
        self.a11 = a
        self.a12 = b
        self.a21 = c
        self.a22 = d
        self.det = a*d - b*c
    
    def __str__(self):
        return "( " + str(self.a11) + " " + str(self.a12) + " \n  " +  str(self.a21) + " " + str(self.a22) + " )"
    
    def mal_vec(self, v):
        return vect2(self.a11 * v.v1 + self.a12 * v.v2, self.a21 * v.v1 + self.a22 * v.v2)

    def mal_mat(self, b):
        c11 = self.a11 * b.a11 + self.a12 * b.a21 
        c12 = self.a11 * b.a12 + self.a12 * b.a22
        c21 = self.a21 * b.a11 + self.a22 * b.a21  
        c22 = self.a21 * b.a12 + self.a22 * b.a22
        return matrix2x2(c11, c12, c21 , c22)

    def inv(self):
        if self.det == 0:
            return None
        return matrix2x2(self.a22 / self.det, -self.a21 / self.det, -self.a12 / self.det, self.a11 / self.det)


class vect2:
    def __init__(self, a, b):
        self.v1 = a
        self.v2 = b
    def __str__(self):
        return "( " + str(self.v1) +" \n  " +  str(self.v2) + " )"

class drehmatrix2x2(matrix2x2):
    def __init__(self, winkel):
        super().__init__(math.cos(winkel), -math.sin(winkel), math.sin(winkel), math.cos(winkel))
        self.winkel = winkel
    
d = drehmatrix2x2(math.pi/4)
print(d)

a = matrix2x2(1, 2, 3, 4)
print(d.mal_mat(a))


print(a)
print(a.inv())

v = vect2(1,2)
print(v)

print(a.mal_vec(v))

print(a.mal_mat(a))

