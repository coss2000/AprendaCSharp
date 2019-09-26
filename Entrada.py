entrada=input()
print(type(entrada))
# Se verifica si lo capturado es un digito y si tiene un punto se indicara que es un numero con decimales.
esEntero=(entrada.isdigit( and estrada.find("."==-1))
if (esEntero):
    #True
    print("Dato entero.¡Muy bien!")

else:
    # Se cumplirá esta linea si la condicion es falsa.
    print("Dato no es entero. Intentar nuevamente.")