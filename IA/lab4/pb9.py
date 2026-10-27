class Complex_Number:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return f"({self.a},{self.b})"

    # def add(self,complex):
    #     self.a += complex.a
    #     self.b += complex.b
    #     return self
    # def subtract(self,complex):
    #     self.a -= complex.a
    #     self.b -= complex.b 
    #     return self

    # def multiply(self,complex):
    #     self.a *= complex.a
    #     self.b *= complex.b 
    #     return self   
    def __add__(self,complex):
        return Complex_Number(self.a + complex.a , self.b + complex.b)
    def __sub__(self, complex):
        return Complex_Number(self.a - complex.a, self.b - complex.b)
    def __mul__(self, other):
        real = self.a * other.a - self.b * other.b
        imag = self.a * other.b + self.b * other.a
        return Complex_Number(real, imag)
        
no1 = Complex_Number(1,2)
no2 = Complex_Number(2,3)
# #print(no1.add(no2))
# #print(no1.subtract(no2))
# print(no1.multiply(no2))
print(no1 + no2)
print(no1 - no2)
print(no1 * no2)