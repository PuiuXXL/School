class ComplexNumber:
    def __init__(self,real,imag):
        self.real = real
        self.imag = imag
    def __add__(self,complex):
        return ComplexNumber(self.real + complex.real, self.imag + complex.imag)
    def __sub__(self,complex):
        return ComplexNumber(self.real - complex.real, self.imag - complex.imag)
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return ComplexNumber(real, imag)
    def __str__(self):
        return f"({self.real},{self.imag})"

no1 = ComplexNumber(3,2)
no2 = ComplexNumber(5,6)
print(no1 + no2)
print(no1 - no2)
print(no1 * no2)