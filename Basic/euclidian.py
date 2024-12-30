class Euclid:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
    def gcd(self, a=None, b=None):
        if a is None or b is None:
            a, b = self.a, self.b
        
        while b:
            a, b = b, a % b
        return a

# Contoh penggunaan
if __name__ == "__main__":
    euc = Euclid(48, 18)
    print(f"GCD dari {euc.a} dan {euc.b} adalah {euc.gcd()}")