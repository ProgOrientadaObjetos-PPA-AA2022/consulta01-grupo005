class Persona:
    sexo = "Masculino"
    def __init__(self,nomb ="Eduardo",apell="Perez",nid ="1105426389" ,sx ="Masculino"):
        self.nombre = nomb
        self.apellidos = apell
        self.iD = nid
        self.sexo = sx
    def show(self):
        print("Mi nombre es "+self.nombre+" "+self.apellidos+
              " con una ID de "+self.iD+" y mi sexo es "+self.sexo)

if __name__ == "__main__":
    p1 = Persona()
    p1.show()

