# Se declara una variable, con una serie de digitos.
numero= "1234"
# La función type nos dice que los digitos 1234 no son str, si no type
print(type(numero))
# Se convierte la cadena a int que es entero
numero=int(numero)
# De nuevo el tipo cambia.
print(type(numero))
# Se declara la salidala cual escribira el texto que escribimos y gracias a los {} se escribirán los digitos.
salida="El número utilizado es {}"
# Se imprimirá la salida con los digitos.
print(salida.format(numero))
