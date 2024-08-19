def modificar_ingredientes(ingredientes):
    """Permite al usuario modificar la lista de ingredientes de la pizza, ya sea agregando o eliminando.
    Parámetros
    ----------
    ingredientes
        list de str
        Lista de ingredientes actuales de la pizza.
    Return
    ------
        list de str
        Lista actualizada de ingredientes después de las modificaciones realizadas por el usuario.
    """

    while True:
        # Muestra las opciones al usuarios.
        print("\n¿Quieres modificar o agregar algún ingrediente?")
        print("1.Agregar ingrediente")
        print("2.Eliminar ingrediente")
        print("3.No quiero modificar ni agregar nada")

        # Lee la opción seleccionada por el usuario.
        eleccion = input("Ingrese el número de tu elección: ")

        if eleccion == "1":
            print("\nIngrendientes disponibles para agregar:")
            print(
                "Tomate, Champiñones, Aceituna, Cebolla, Pollo, Jamón, Carne, Tocino, Queso"
            )
            # Lee el ingrediente que el usuario agrega.
            nuevo_ingrediente = input(
                "Ingresa el ingrediente que deseas agregar: "
            ).capitalize()

            # Verifica si el ingrediente ya está en la lista.
            if nuevo_ingrediente in ingredientes:
                print(f"{nuevo_ingrediente} ya está en la pizza.")
            else:
                # Agrega nuevo ingrediente a la lista.
                ingredientes.append(nuevo_ingrediente)
                print(f"{nuevo_ingrediente} agregado a la pizza.")

        elif eleccion == "2":
            # Muestra los ingredientes actuales de la pizza.
            print("\nIngredientes actuales:", ingredientes)
            # Leer el ingrediente que el usuario quiere eliminar.
            eliminar_ingrediente = input(
                "Ingresa ingrediente que deseas eliminar: "
            ).capitalize()

            # Verificar si el ingrediente está en la lista.
            if eliminar_ingrediente in ingredientes:
                # Eliminar el ingrediente de la lista.
                ingredientes.remove(eliminar_ingrediente)
                print(f"{eliminar_ingrediente} ha sido eliminado de la pizza")
            else:
                print(f"{eliminar_ingrediente} no está en la pizza")

        elif eleccion == "3":
            # Salir del bucle si el usuario no quiere hacer más cambios.
            break

        else:
            # Muestra mensaje de error para opciones inválidas.
            print("Opción no válida. Intenta de nuevo")

    # Devuelve la lista actualizada de ingredientes
    return ingredientes