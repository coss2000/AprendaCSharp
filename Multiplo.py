numero=int(input("Dame un numero entero: "))
# Si el residual es igual a 0 una vez almacenado en valor booleano, quiere decir que el numero es multiplo.
esMultiplo3=((numero%3)==0)
esMultiplo5=((numero%5)==0)
esMultiplo7=((numero%7)==0)
# Segun la tabla de and, el resultado es verdadero si todas las condiciones son verdaderas.
# Segun la tabla de or, el resultado es verdadero si una de las condiciones es verdadera.
if ((esMultiplo3 and esMultiplo5) or esMultiplo7):
    print("Correcto.")
else:
    print("Incorrecto.")
    