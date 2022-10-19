class Contadores:
    @staticmethod
    def la_contacion():
        for i in range(0,5):
            x : int = i
            print(f"Acá, i tiene el valor de: {x}")
Contadores.la_contacion()