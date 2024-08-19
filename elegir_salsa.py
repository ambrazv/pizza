def elegir_salsa():
    """
    Permite al usuario elegir el tipo de salsa para su pizza.
    Parámetros:
    -----------
    None
            Esta función no tiene parámetros, ya que interactúa con el usuario a través de la consola.
    Returns:
    --------
    str
        El tipo de salsa seleccionada por el usuario.
    """
    while True:
        print("\nElige el tipo de salsa que quieres para tu pizza: ")
        print("1.Salsa de tomate")
        print("2.Salsa Alfredo")
        print("3.Salsa Barbecue")
        print("4.Salsa Pesto")

        eleccion = input("Ingresa el número de tu elección: ")
        if eleccion == "1":
            return "Salsa de tomate"
        elif eleccion == "2":
            return "Salsa Alfredo"
        elif eleccion == "3":
            return "Salsa Barbecue"
        elif eleccion == "4":
            return "Salsa Pesto"
        else:
            # Si el usuario ingresa otro número diferente a 1,2 o 3, muestra un mensaje de error y le volverá a solicitar la elección.
            print("Número no válido, por favor ingresa 1,2 o 3")