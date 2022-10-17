class Articulo():
    dicc={}
    def __init__(self, cod_articulo,nombre,descripcion,precio):
        self.cod_articulo = cod_articulo
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.dicc["codigo"]= self.cod_articulo
        self.dicc["nombre"]= self.nombre
        self.dicc["descripcion"]= self.descripcion
        self.dicc["precio"]= self.precio
        

class Compra:
    compra = []
    
    def agregar(self, nuevoArticulo):
        self.compra.append(nuevoArticulo.dicc)
        
    def listar(self):
        for articulo in self.compra:
            print("Codigo", articulo["codigo"])
            print("Nombre", articulo["nombre"])
            print("Descripcion", articulo["descripcion"])
            print("Precio", articulo["precio"],"\n")
        
    def baja(self,codigo):
        for i in range (len(self.compra)):
            if self.compra[i]["codigo"] == codigo:
                self.compra.remove(self.compra[i])
            
    def buscar(self,codigo_busq):
        for articulo in self.compra:
            if articulo["codigo"] == codigo_busq:
                print("Codigo", articulo["codigo"])
        
    def modificar(self,codigo_mod):
        for articulo in self.compra:
            if articulo["codigo"] == codigo_mod:
                articulo["codigo"] =input("introduce el codigo del producto:")
                articulo["nombre"] =input("introduce el nombre del producto:")
                articulo["descripcion"] =input("introduce la descripcion del producto:")
                articulo["precio"] = int(input("introduce el precio del producto:"))
                print("Codigo", articulo["codigo"])
                print("Nombre", articulo["nombre"])
                print("Descripcion", articulo["descripcion"])
                print("Precio", articulo["precio"],"\n")
            else:
                print("No se ha modificado el producto")
    
#Comprobaciones de cada uno de los metodos
nuevoArticulo= Articulo("cod2","ordenador","14","es un ordenador")
compra1 = Compra()
compra1.agregar(nuevoArticulo)
compra1.listar()
compra1.buscar("cod2")
compra1.modificar("cod2")
compra1.baja("cod2")

