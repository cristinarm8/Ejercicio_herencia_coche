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
        return "El vehículo es de color {} y tiene {} ruedas".format(self.color, self.ruedas)

class Coche(Vehiculo):

    # Método constructor:
    def __init__(self, color, ruedas, velocidad, cilindrada):
        # super (). nos devuelve uun objeto temporal de la superclase que permite invocar a los atributos y métodos definidos en la misma.
        super().__init__(color, ruedas)
        # Atributos de una instancia sólo para objetos de la clase Coche.
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    
    def __str__(self):
        return super().__init__ + "tiene una velocidad de {} y una cilindrada de {}".format(self.velocidad, self.cilindrada)

coche_prueba = Coche("negro", 4, 190, 1150)


