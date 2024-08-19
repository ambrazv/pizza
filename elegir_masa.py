def elegir_masa():
    """
    Permite al usuario elegir el tipo de masa para su pizza.
    Parámetros:
    -----------
    None
            Esta función no tiene parámetros, ya que interactúa con el usuario a través de la consola.
    Returns:
    --------
    str
        El tipo de masa seleccionada por el usuario.
    """
    while True:
        print("\nElige el tipo de masa que quieres para tu pizza: ")
        print("1.Masa tradicional")
        print("2.Masa delgada")
        print("3.Masa con bordes de queso")

        eleccion = input("Ingresa el número de tu elección: ")
        if eleccion == "1":
            return "Masa tradicional"
        elif eleccion == "2":
            return "Masa delgada"
        elif eleccion == "3":
            return "Masa con bordes de queso"
        else:
            #Si el usuario ingresa otro número diferente a 1,2 o 3, muestra un mensaje de error y le volverá a solicitar la elección.
            print("Número no válido, por favor ingresa 1,2 o 3")