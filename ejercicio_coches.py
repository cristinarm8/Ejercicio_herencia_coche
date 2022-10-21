'''
Ejercicio coches

Utilizando esta nueva técnica extiende la clase Vehiculo y realiza la siguiente 
implementación:

Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
• Realiza una función llamada catalogar() que reciba la lista de vehiculos y los recorra mostrando el nombre de su clase y sus atributos.
• Modifica la función catalogar() para que reciba un argumento optativo ruedas, haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. 
También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.

Recordatorio

Puedes utilizar el atributo especial de clase name para recuperar el nombre de 
la clase de un objeto:

type(objeto).__name

'''
class Vehiculo:

    # Método constructor.
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        #return "Vehículo: ", type(self).__name__ ,"\n\tColor: {}\n\tRuedas".format(self.color, self.ruedas)
        return "El vehículo es de color {}, tiene {} ruedas".format(self.color, self.ruedas)

#vehiculo = Vehiculo("verde", 4)
#print(vehiculo)

class Coche(Vehiculo):

    # Método constructor:
    def __init__(self, color, ruedas, velocidad, cilindrada):
        # super (). nos devuelve uun objeto temporal de la superclase que permite invocar a los atributos y métodos definidos en la misma.
        super().__init__(color, ruedas)
        # Atributos de una instancia sólo para objetos de la clase Coche.
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__str__() + ", tiene una velocidad de {} k/m, una cilindrada de {}".format(self.velocidad, self.cilindrada)

coche = Coche("negro", 4, 190, 1150)
print(coche)

class Camioneta(Coche):

    # Método constructor:
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        super().__init__(color, ruedas, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + " y lleva una carga de {} kg".format(self.carga)

camioneta = Camioneta("azul", 4, 120, 1200, 1300)
print(camioneta)

class Bicicleta(Vehiculo):

    # Método contructor:
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + ", es del tipo {}".format(self.tipo)

bicicleta = Bicicleta("blanco", 2, "urbana")
print(bicicleta)


class Motocicleta(Bicicleta):

    # Método constructor:
    def __init__(self, color,ruedas,tipo,velocidad,cilindrada):
        super().__init__(color, ruedas, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + ", tiene una velocidad de {} y una cilindrada de {}".format(self.velocidad, self.cilinndrada)

motocicleta = Motocicleta("rojo", 2, "urbana", 120, 1000)
print(motocicleta)




