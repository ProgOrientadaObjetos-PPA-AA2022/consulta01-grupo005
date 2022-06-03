class NombreApe:
    def __init__(self, nomb = "Byron Josue", ape = "Castillo Paladines"):
        self.name = nomb
        self.name2 = ape
    def show(self):
        print("Nombres Completos:",self.name,"",self.name2)
if __name__ == "__main__":
    n1 = NombreApe()
    n1.show()
