# Se declaran las variables
acumulado=int(0)
numero=str("")

#Se puede formar un ciclo infinito si colocamos True como condicion de While.
while True:
    numero=input("Dame un numero entero: ")
    if numero=="":
        # Numero vacio, reporta y sale del programa.
        print("Vacio. Salida del programa")
        break
    else:
        acumulado+=int(numero)
        salida="Monto acumulado: {}"
        print(salida.format(acumulado))
        