
# ver la fecha


# import datetime


# ahora = datetime.datetime.now()


# print(ahora)


#  Ejercicio 13: Crear una Cadena de Caracteres Multilínea


cadena = "loren jewfowfej owifjwefohi wpifrjsifj woeftu iwdji iqwjfifj  ijfeiewjf ijwefrijwi iwejfiwjfwef"

# Ejercicio 207: Restaurar un Texto a partir de la Versión Acortada del Texto


def restaurarTexto(acordado):
    resultado = ""
    indice = 0 
    loingitud = len(acordado)
    while indice < loingitud:
        if acordado[indice] == "#":
            resultado += acordado[indice +2] * int(acordado[indice + 1])


# ejercio POO
class alumno:
    #inicializamos los atributos
    def __init__(self,nombre, nota):
        self.nombre = nombre
        self.nota = nota
      
    def imprimir(self):
        print("alumno", self.nombre , "nota" , self.nota)
    
    def resultado(self):
        if self.nota > 5:
            print("aprobo " , self.nombre)
        else:
             print("NOOOO aprobo " , self.nombre)


alumno1 = alumno("arturo", 6)
alumno2 = alumno("dsf", 4)
alumno3 = alumno("artsdfuro", 6)
alumno4 = alumno("arsdfturo", 10)

alumno1.imprimir()

alumno1.resultado()
