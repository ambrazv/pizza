from elegir_masa import elegir_masa
from elegir_salsa import elegir_salsa
from modificar_ingredientes import modificar_ingredientes
from calcular_tiempo import calcular_tiempo
from mostrar_ingredientes import mostrar_ingredientes

def pedidopizza():
    """Esta función, permite al usuario realizar un pedido de PizzaJat. El usuario eligen la masa, salsa e ingredientes de la pizza y luego pueden confirmar o cancelar el pedido.
    Parámetros
    ----------
        None
            No tiene, porque interactúa con el cliente a través de entradas de la consola.
    Returns
    -------
        None
            Esta función no retorna valor, ya que imprime los resultados del pedido y mensajes al cliente.
    """
    while True:
        print("\n----Bienvenido a Pizza JAT----")
        print("Elige como quieres tu pizza. Todas nuestras pizzas vienen con queso como ingrediente base.")
        pedido = {}
        pedido["Masa"] = elegir_masa()
        print(f"\nHaz elegido {pedido["Masa"]}.")
        pedido["Salsa"] = elegir_salsa()
        print(f"\nHaz elegido {pedido["Salsa"]}.")
        ingredientes = ["Queso"]
        pedido["Ingredientes"] = modificar_ingredientes(ingredientes)
        mostrar_ingredientes(pedido["Ingredientes"])
        #Para confirmar el pedido
        confirmar = input("\n¿Desea confirmar el pedido) (sí/no): ").lower()
        if confirmar in ["sí", "si", "s"]:
            tiempo_estimado = calcular_tiempo(pedido["Ingredientes"])
            print(f"\nPedido confirmado. Tu pizza estará lista en aproximadamente {tiempo_estimado} minutos")
            print("Gracias por preferirnos")
            break
        else:
            print("\nPedido cancelado. Puedes comenzar de nuevo si lo deseas")
            break

if __name__ == "__main__":
    pedidopizza()