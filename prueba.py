class articulos:

    id = 0
    nombre = ""


    def __init__(self,id,nombre):

        self.id = id
        self.nombre = nombre
    
    def mostrar(self):

        print(self)

class antiguedades(articulos):
    anios = 0
    

    def __init__(self,id,nombre,anios):
        articulos.__init__(self,id,nombre)
        self.anios = anios



    def __str__(self):

        print(f"id: {self.id}")
        print(f"nombre: {self.nombre}")
    
    def mostrar(self):
        
        print(self)

        
tres = antiguedades(2,"pedro",22)
antiguedades.__str__(tres)
articulos.mostrar(tres)
antiguedades.mostrar(tres)
