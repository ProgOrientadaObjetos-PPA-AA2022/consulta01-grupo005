class CalifiacionMate():
    def __init__(self,mater = "Matematicas",docen = "Eduardo"):
        self.materia = mater
        self.docente = docen
    def show(self):
        print("El nombre de la Materia es: ",self.materia)
        print("EL nombre del docente es: ",self.docente)
if __name__ == "__main__":
    p1 = CalifiacionMate()
    p1.show()
