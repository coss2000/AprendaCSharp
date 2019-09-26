numero1=input("Numero 1:")
numero2=input("Numero 2:")
salida="Numeros proporcionados: {} y {}. {}."
if(numero1==numero2):
    # Se cumple esta condicion si los 2 numeros son iguales.
    print(salida.format(numero1, numero2, "Los numeros son iguales"))
else:
    # Pueden entrar una de estas condiciones si el primero if no se cumple.
    if numero1>numero2:
        print(salida.format(numero1, numero2,"El mayor es el primero"))
    else:
        print(salida.format(numero1, numero2,"El mayor es el segundo"))

        