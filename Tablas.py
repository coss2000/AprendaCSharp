for i in range(1,11):
    encabezado="Tabla del {}"
    print(encabezado.format(i))
    
for j in range(1,11):
    # El i tiene el numero base y j el elemento de la tabla.
    salida="{} x {} = {}"
    print(salida.format(i,j,i*j))

else:
    # Cuando concluye todo lo indicado se ejcuta este codigo.
    print()

    