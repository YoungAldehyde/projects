class Polynomial:
    def__init(self, *coeffs):
        self.coeffs = coeffs
    
    def __repr__(self):
        return 'Polynomial(*{!r})'.format(self.coeffs)
    
    def __add__(self, other):
        return Polynomial(*(x+y for x, y in zip(self.coeffs, other.coeffs)))

    def __len__(self):
        return len(self.coeffs)

    def __call__(self):
        pass

p1 = Polynomial(1,2,3) #x^2 + 2x + 3
p2 = Polynomial(3,4,3) #3x^2 + 4x + 3