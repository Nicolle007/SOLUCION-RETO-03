
class MenuItem:
     def __init__(self, nombre, precio=int):
          self.nombre=nombre
          self.precio=precio

class Sopa(MenuItem):
     def __init__(self, nombre, precio,tipo):
        super().__init__(nombre,precio)
        self.tipo = tipo

class Bebida(MenuItem):
     def __init__(self, nombre, precio,temperatura):
        super().__init__(nombre,precio)
        self.temperatura = temperatura

class Postre(MenuItem):
     def __init__(self, nombre, precio,helado):
        super().__init__(nombre,precio)
        self.helado = helado

class Fruta(MenuItem):
     def __init__(self, nombre, precio,tipo):
        super().__init__(nombre,precio)
        self.tipo = tipo

class Ensalada(MenuItem):
     def __init__(self, nombre, precio,gusto):
        super().__init__(nombre,precio)
        self.gusto = gusto

class Proteina(MenuItem):
     def __init__(self, nombre, precio,gramaje):
        super().__init__(nombre,precio)
        self.gramaje = gramaje

class Entradas(MenuItem):
     def __init__(self, nombre, precio,lugar):
        super().__init__(nombre,precio)
        self.lugar = lugar

class Adicion(MenuItem):
     def __init__(self, nombre, precio,tipo):
        super().__init__(nombre,precio)
        self.tipo = tipo

class Infantil(MenuItem):
     def __init__(self, nombre, precio,contenido):
        super().__init__(nombre,precio)
        self.contenido = contenido
  

class Quesos(MenuItem):
     def __init__(self, nombre, precio,tipo):
        super().__init__(nombre,precio)
        self.tipo = tipo


class Orden:
    global descuento
    descuento=0
    def __init__(self,contenido=list):
     self.contenido=contenido

    def agregar_articulos(self, Item):
        self.contenido.append(Item)

    def total(self):
        suma=0
        for i in self.contenido:
            suma = i.precio + suma
        if descuento!=0:
            suma=suma*descuento
        print(suma)
            

    def descuentos(self,tipo):
        self.tipo = tipo
        match tipo:
            case "Proteina+Ensalada":
                    descuento=0.85
            case "Proteina+Fruta":
                descuento=0.80
            case "Postre+Postre":
                descuento=0.90
            case "Bebida+Adicion":
                descuento=0.90
            case "Infantil+Postre":
                descuento=0.75

    def Items(self):
        for i in self.contenido:
            print(i.nombre)
# Sopas
sopa1 = Sopa("Sopa de pollo", 5000, "clara")
sopa2 = Sopa("Sopa de lentejas", 5200, "espesa")
sopa3 = Sopa("Sopa de verduras", 4800, "ligera")

# Bebidas
bebida1 = Bebida("Limonada", 3000, "fría")
bebida2 = Bebida("Chocolate caliente", 3500, "caliente")
bebida3 = Bebida("Jugo de mango", 3200, "fría")

# Postres
postre1 = Postre("Flan", 4000, False)
postre2 = Postre("Helado de vainilla", 4500, True)
postre3 = Postre("Torta de chocolate", 5000, False)

# Frutas
fruta1 = Fruta("Manzana", 2500, "roja")
fruta2 = Fruta("Banano", 2200, "maduro")
fruta3 = Fruta("Uvas", 2700, "verdes")

# Ensaladas
ensalada1 = Ensalada("Ensalada César", 6000, "ligera")
ensalada2 = Ensalada("Ensalada griega", 5800, "fresca")
ensalada3 = Ensalada("Ensalada tropical", 6200, "dulce")

# Proteínas
proteina1 = Proteina("Pollo asado", 10000, "200g")
proteina2 = Proteina("Pescado al horno", 12000, "180g")
proteina3 = Proteina("Carne a la parrilla", 13000, "250g")

# Entradas
entrada1 = Entradas("Pan de ajo", 2500, "mesa")
entrada2 = Entradas("Mini empanadas", 3000, "cocina")
entrada3 = Entradas("Bastones de queso", 3200, "barra")

# Adiciones
adicion1 = Adicion("Papas a la francesa", 4000, "fritas")
adicion2 = Adicion("Arepa", 1500, "asada")
adicion3 = Adicion("Tajadas", 2000, "dulces")

# Infantil
infantil1 = Infantil("Combo dinosaurio", 8500, "hamburguesa, jugo, sorpresa")
infantil2 = Infantil("Caja mágica", 9000, "nuggets, papas, postre")
infantil3 = Infantil("Mini pizza kit", 8000, "pizza personal, jugo")

# Quesos
queso1 = Quesos("Queso mozzarella", 3500, "blando")
queso2 = Quesos("Queso azul", 3800, "fuerte")
queso3 = Quesos("Queso parmesano", 3600, "curado")
orden = Orden([])

orden.agregar_articulos(sopa1)
orden.agregar_articulos(bebida2)
orden.agregar_articulos(postre3)
orden.agregar_articulos(fruta1)
orden.agregar_articulos(ensalada2)
orden.agregar_articulos(proteina3)
orden.agregar_articulos(entrada1)
orden.agregar_articulos(adicion2)
orden.agregar_articulos(infantil3)
orden.agregar_articulos(queso1)
orden.total()
orden.Items()
orden.descuentos("Postre+Postre")
orden.total()
 