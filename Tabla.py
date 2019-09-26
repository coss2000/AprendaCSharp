numero=input("Dame un numero del 1 al 9: ")
numero=int(numero)
# El usuario debe dar un numero.
# For permite ejecutarun bloque de código determinadas veces.
for i in range(1,11):
    # i varia segun cada iteracion.
    salida="{} x {} = {}"
    print(salida.format(numero,i,i*numero))
