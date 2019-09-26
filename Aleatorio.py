# Gracias a la instrucción import se puede importar un modulo en un programa.
import random

# Se define una variable con el nombre numero1 a la cual se define como flotante y se le es asignado un valor.
# Una variable flotante es un numero con decimales.
numero1=float(10.5)

# Una función es un conjunto de instrucciones y son declaradoas con def.
def miFuncion():
    # El numero generado se convierte a flotante.
    numero2=float(random.randrange(1,10))
    mensaje="La suma de {} y {} es {}"
    print(mensaje.format(numero1,numero2,numero1+numero2))

# Se ejecuta la funcion.
miFuncion()
