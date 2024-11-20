# Paso 1: Definir la clase Controlador
# Esta clase se encarga de coordinar los componentes y gestionar el flujo de ejecución.
class Controlador:

    def __init__(self):
        # Inicializar los componentes necesarios para el programa
        # Aquí se crean instancias de ComponenteA y ComponenteB, que serán usados más adelante.
        self.componente_a = ComponenteA()
        self.componente_b = ComponenteB()
        self.resultado = None  # Almacena el resultado de la ejecución de los componentes.

    def iniciar_programa(self):
        # Método para iniciar el programa
        print("Iniciando programa...")
        try:
            # Paso 1: Ejecutar componente A
            # Este método llamará a ejecutar_componente_a para iniciar el flujo.
            self.ejecutar_componente_a()

            # Paso 2: Ejecutar componente B solo si el componente A fue exitoso
            # Llamará a ejecutar_componente_b y pasará el resultado obtenido de A.
            self.ejecutar_componente_b()

            # Paso 3: Procesar el resultado final
            # Este método realiza una operación final con el resultado de B.
            self.procesar_resultado()

        except Exception as e:
            # Si ocurre un error en la ejecución de cualquier componente
            print(f"Ocurrió un error durante la ejecución: {e}")
        finally:
            # Se ejecuta siempre, independientemente de si ocurrió un error
            print("Programa finalizado.")

    def ejecutar_componente_a(self):
        # Ejecuta el primer componente (Componente A)
        print("Ejecutando Componente A...")
        self.resultado = self.componente_a.ejecutar()

    def ejecutar_componente_b(self):
        # Ejecuta el segundo componente (Componente B) usando el resultado del componente A
        print("Ejecutando Componente B...")
        self.resultado = self.componente_b.ejecutar(self.resultado)

    def procesar_resultado(self):
        # Procesa el resultado final después de ejecutar ambos componentes
        print("Procesando resultado final...")
        # Aquí puedes aplicar la lógica de procesamiento final con self.resultado
        print(f"Resultado final: {self.resultado}")

# Paso 2: Definir ComponenteA
# ComponenteA es una clase que representa una operación individual en el sistema.
class ComponenteA:

    def ejecutar(self):
        # Simula una operación realizada por el Componente A
        print("Componente A en ejecución")
        return "Resultado de A"

# Paso 3: Definir ComponenteB
# ComponenteB representa otro componente en el sistema que requiere datos de entrada.
class ComponenteB:

    def ejecutar(self, input_data):
        # Simula una operación realizada por Componente B usando input_data
        print("Componente B en ejecución")
        return f"{input_data} modificado por B"

# Paso 4: Ejemplo de ejecución del programa
# Aquí creamos una instancia de Controlador y ejecutamos el programa.
if __name__ == "__main__":
    controlador = Controlador()
    controlador.iniciar_programa()
